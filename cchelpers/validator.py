import sys
import re

def parse_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

def check_example_file(content):
    errors = []

    comment_pattern = r'<!--(.*?)-->'
    comment_match = re.search(comment_pattern, content, re.DOTALL)

    if comment_match:
        comment_content = comment_match.group(1)

        # Sprawdź, czy w sekcji z komentarzem istnieje pole Miasto z odpowiednimi wartościami
        if not re.search(r'\bbump: (major|minor|patch)\b', comment_content):
            errors.append("Error: Allowed bump values: major, minor or patch.")
    else:
        errors.append("Error: Missing comment section.")

    # Sprawdź, czy w pliku występują następujące sekcje
    required_sections = ['Added', 'Changed', 'Removed', 'Fixed', 'Notice']
    found_sections = []

    for section in required_sections:
        section_header = f"### {section}"
        if section_header in content:
            # Dodaj sekcję do listy znalezionych sekcji
            found_sections.append(section)
        else:
            errors.append(f"Error: Missing section {section}.")

    # Sprawdź, czy przynajmniej jedna sekcja zawiera jakiś content
    filled_section_found = False
    for found_section in found_sections:
        section_header_index = content.find(f"### {found_section}")
        section_end_index = content.find("###", section_header_index + 1) if section_header_index != -1 else len(content)
        section_content = content[section_header_index + len(f"### {found_section}") : section_end_index].strip()

        if section_content:
            filled_section_found = True
            break

    if not filled_section_found:
        errors.append("Error: At least one section must contain some content.")

    return '\n'.join(errors)

def init():
    if len(sys.argv) < 2:
        print("Provide the path to the fragment Markdown file as a parameter.")
        sys.exit(1)
    else:
        file_paths = sys.argv[1:]
        for file_path in file_paths:
            content = parse_markdown_file(file_path)
            errors = check_example_file(content)
            if errors:
                print(errors)
                sys.exit(1)

if __name__ == "__main__":
    init()
