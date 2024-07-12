#
# ~~~ See distribution
from pkg_resources import get_distribution, DistributionNotFound
dist = get_distribution('python_package_templage')

#
# ~~~ Fetch local package version
__version__ = dist.version

#
# ~~~ Compare local version to latest version
def see_latest_version():
    import requests, re
    url = 'https://raw.githubusercontent.com/ThomasLastName/python-package-template/main/setup.py'
    response = requests.get(url)
    if response.status_code == 200:
        setup_py_content = response.text
        version_match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", setup_py_content)
        if version_match:
            latest_version = version_match.group(1)
            return latest_version        
        else:
            raise ValueError("Version string not found in setup.py.")
    else:
        raise ValueError(f"Failed to fetch setup.py: {response.status_code} - {response.text}")

def check_for_update_available(__version__):
    try:
        latest_version = see_latest_version()
        if __version__ < latest_version:
            import warnings
            warnings.warn(
                f"You are using bnns version {__version__}, but version {latest_version} is available. "
                f"Consider upgrading using ",
                UserWarning
            )
    except Exception as e:
        import warnings
        warnings.warn(f"Could not check the latest version of bnns: {e}")

check_for_update_available(__version__)



