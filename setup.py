
### ~~~
## ~~~ Originally from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

setup(
    name = 'python_package_template',
    version = '0.1.1',
    url = 'https://github.com/ThomasLastName/python-package-template',
    author = 'Thomas Winckelman',
    author_email = 'winckelman@tamu.edu',
    description = 'Python package template',
    packages = find_packages(),    
    install_requires = ["requests"]    # ~~~ when you pip install `python_package_template`, pip will also install `requests`
)
