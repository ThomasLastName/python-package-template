
### ~~~
## ~~~ Originally from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

setup(
    name = 'python_package_template',
    version = '0.0.2',
    url = 'https://github.com/ThomasLastName/python-package-template',
    author = 'Thomas Winckelman',
    author_email = 'winckelman@tamu.edu',
    description = 'Python package template',
    packages = find_packages(),    
    install_requires = ["pyreadr"]    # ~~~ when you pip install `package_name`, pip will also install `pyreadr`
)
