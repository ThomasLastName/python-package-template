
### ~~~
## ~~~ Originally from https://github.com/maet3608/minimal-setup-py/blob/master/setup.py
### ~~~ 

from setuptools import setup, find_packages

setup(
    name = 'python_package_template',        # ~~~ NOTE: this must be the same as the name of the folder containing the `__init__.py` file
    version = '0.3.3',                       # ~~~ replace this
    url = 'https://github.com/ThomasLastName/python-package-template',   # ~~~ replace this
    author = 'Thomas Winckelman',            # ~~~ replace this
    author_email = 'fake_email@gmail.com',   # ~~~ replace this
    description = 'Python package template', # ~~~ replace this
    packages = find_packages(),
    install_requires = ["requests"]          # ~~~ when you pip install `python_package_template`, pip will also install `requests` or whatever else from this list
)
