# -*- encoding: utf-8 -*-

"""
A Set of Utility Functions for a Time Series Data for ``pandas``

A time series analysis is a way of analyzing a sequence of data which
was collected over a period of time and the data is collected at a
specific intervals. The :mod:`pandas` provides various functions to
manipulate a time object which is a wrapper over the ``datetime``
module and is a type of ``pd.Timestamp`` object.

The module provides some utility functions for a time series data
and tests like "stationarity" which is a must in EDA!

.. caution::
    The time series module consists of functions which was earlier
    developed in `GH/sqlparser <https://gist.github.com/ZenithClown/f99d7e1e3f4b4304dd7d43603cef344d>`_.

.. note::
    More details on why the module was merged is
    available `GH/#24 <https://github.com/sharkutilities/pandas-wizard/issues/24>`_.

.. note::
    Code migration details are mentioned
    `GH/#27 <https://github.com/sharkutilities/pandas-wizard/issues/27>`_.
"""

from pandaswizard.timeseries.stationarity import *
from pandaswizard.timeseries.ts_featuring import *
