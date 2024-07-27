# -*- encoding: utf-8 -*-

"""
Utility Functions and/or Wrappers for pandas Library

The :mod:`pandaswizard` module includes functions, wrappers and other
utility functions for `pandas` module. The package is kept simple and
minimalistic such that external dependencies are reduced. The working
of the module is divided into the following sections:

    * :mod:`pandaswizard.aggregate`: a set of aggregate functions
      that can be used along with ``pd.groupby().agg({...})`` method
      without comprimising functionality.
    * :mod:`pandaswizard.wrappers`: a set of decorators/wrappers
      that can be used along side a function.
"""

# ? package follows https://peps.python.org/pep-0440/
# ? https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html
__version__ = "1.1.0a0"

# init-time options registrations
from pandaswizard.aggregate import (
    quantile,
    percentile
)

from pandaswizard import window
from pandaswizard import wrappers
from pandaswizard import functions
