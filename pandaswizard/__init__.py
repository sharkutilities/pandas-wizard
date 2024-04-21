# -*- encoding: utf-8 -*-

"""
Utility Functions, Wrappers for pandas Library - Coming Soon!

The :mod:`pdwizard` module includes functions, wrappers and other
utility functions for `pandas` module. The package is kept simple and
minimalistic such that external dependencies are reduced.
"""

# ? package follows https://peps.python.org/pep-0440/
# ? https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
__version__ = "1.1.0a0"

# init-time options registrations
from pandaswizard.aggregate import (
    quantile,
    percentile
)

from pandaswizard import wrappers
