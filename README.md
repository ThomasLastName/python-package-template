# python-package-template

My (work in progress) template for a python package, with only the features I want, and none of the baggage I don't. This is basically an extension of the minimalist repo [slug](https://github.com/ThomasLastName/slug). Feature summary:

 - `__init__.py` automatically defines the `__version__` dunder based on the package's `setup.py` file.
 - Whenever the package is imported, it compares the local version to the version in GitHub and warns the user if an update is available.

# Usage

If you're building a package, then you'll need to:
 - [ ] update the `setup.py` file (replace `python(-/_)package(-/_)template` with your package name, replace the url with your package's github url, replace the author name, etc.),
 - [ ] rename the name of the folder containint the `__init__.py` file to the name of your package (**the name of this folder must match the `name` argument passed to `setup` in `setup.py`**), and
 - [ ] populate that same folder with the actual contents of your package.


# Installation/Upgrading

**Currently, installation requires that you have git installed on your machine!** (see also [#7](https://github.com/ThomasLastName/quality-of-life/issues/7))

For developers, you can start by cloning the repo as normal. Next, I recommend also navigating to the root directory of the repo, and then using the command `pip install -e .` (the `-e` flag stands for "editable", and the `.` indicates the current working directory). This way, "if you update the code from Github [or locally], your installation will automatically take those changes into account without requiring re-installation" (explanation borrowed from [these docs](https://sepia-lanl.readthedocs.io/en/latest/)).

If you use this template but change the name of the rpository, say to `my-repo`, then general users of your package can install and upgrade your code both with the command `pip install --upgrade git+https://github.com/ThomasLastName/my-repo.git` assuming it is hosted on GitHub in the same manner as this template. **However, if you intend to modify this package** (it's an empty template, after all), then you yourself should follow the develop installation instructions (previous paragraph).


