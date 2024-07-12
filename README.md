# python-package-template

My (work in progress) template for a python package, with only the features I want, and none of the baggage I don't. This is basically an extension of the minimalist repo [slug](https://github.com/ThomasLastName/slug). Summary of features

 - `__init__.py` automatically defines the `__version__` dunder based on the package's `setup.py` file.
 - Whenever the package is imported, it compares the local version to the version in GitHub and warns the user if an update is available.
