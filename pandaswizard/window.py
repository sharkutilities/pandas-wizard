# -*- encoding: utf-8 -*-

"""
A Utility Wrapper for the Rolling Functions for the :attr:`pandas` Module

The :attr:`pandas.core.window.rolling()` is a useful window function
that can be used to capture historic data movement patterns (like
moving averages). However, there are some limitations like application
of user defined function to the rolling module. For example, we may
want to average out based on "weighted moving average" function.
"""

import numpy as np
import pandas as pd

from typing import Union, Callable

def _rolling(series : pd.Series, window : Union[int, Callable], **kwargs):
    """
    Wrapper Function that Syncs the Method with :attr:`.rolling()` Method

    The wrapper function accepts all the keyword arguments and returns
    only the arguments with their default value (or user-defined) to
    the :attr:`rolling()` method.

    Limitations: the wrapper function will work only with a data
    of type :attr:`pd.Series` and thus, does not supporr the :attr:`on`
    parameter which selects column from the data frame. The defined
    wrapper will typically work like:

    .. code-block:: python
        data = pd.DataFrame(data = {...})
        data["calculations"] = data["column"].apply(pdw.rolling(...))
    """

    min_periods = kwargs.get("min_periods", None)
    center = kwargs.get("center", False)
    win_type = kwargs.get("win_type", None)
    closed = kwargs.get("closed", None)
    step = kwargs.get("step", None)

    return series.rolling(
        window,
        min_periods = min_periods,
        center = center,
        win_type = win_type,
        closed = closed,
        step = step
    )


def rolling(
        series : Union[pd.Series, np.ndarray],
        window : Union[int, Callable],
        method : Callable = np.mean,
        **kwargs
    ) -> np.ndarray:
    """
    A Wrapper for the :attr:`pd.DataFrame(...).rolling()` Module

    The :attr:`pandas` module useful window function :attr:`rolling`
    which are most of the time sufficient for aggregating over a
    data series but limited to in-built functions, or a custom function
    can be applied by using `.apply(...)` over the rolling values.
    To address this issue, the function wraps the method and rolling
    calculations in one place and returns an array to be directly
    added to the dataframe. Example is as below:

    .. code-block:: python
        data = pd.DataFrame(np.random.random((100, 1)), columns = ["A"])

        data["MA-50"] = data["A"].rolling(50).mean() # using rolling method

    Instead of moving average, we can also give more weightage to the
    recent time-period (weighted average) like:

    .. code-block:: python
        udf = lambda x : (x * np.array([0.125, 0.250, 0.500])).sum()
        data["wma"] = data["A"].rolling(3).apply(udf)

    To reduce iterative process of defining the factors (of :attr:`udf`)
    and creating one step calculations this function can be helpful.
    The revised syntax is like:

    .. code-block:: python
        data["wma"] = pdw.rolling(data["A"], 50, method = np.mean, ...)

    The following paramteres and keyword arguments are accepted by the
    function to provide dynamic approach as below:

    :type  series: object
    :param series: The dataframe series object which can be typically
        accessed directly like :attr:`dataframe["column"]` or an
        n-dimensional array like :attr:`dataframe["column"].values`.

    :type  window: int | callable
    :param window: The length of the window which is either an integer
        or a callable value which is supported by the
        `pd.DataFrame.rolling` function.

    :type  method: callable
    :param method: The aggregation method of the rolling series,
        which can be a simple function like :attr:`np.mean` or
        can be any of the custom fancy functions.
    """

    rolling_ = _rolling(series, window, **kwargs) # rolling object
    return [
        method(array) if array.shape[0] == window
        else np.nan for array in rolling_
    ]
