from setuptools import setup, find_packages


setup(
    name='cc-helper',
    version='0.6.0',
    packages=find_packages(include=['cchelpers', 'cchelpers.*']),
    install_requires=[
        'markdown-it-py~=3.0.0',
        'beautifulsoup4~=4.12.3',
    ],
    entry_points={
        'console_scripts': [
            'cc_compresor=cchelpers.compresor:init',
            'cc_validator=cchelpers.validator:init',
        ],
    },
)
