# -*- encoding: utf-8 -*-

"""
A Set of Function(s) to Collate/Aggregate based on Logic

A simple example of aggregation is the statistical measures like
:attr:`mean`, :attr:`median`, etc. Additional in-frequently but
popular aggregation functions are defined here for end-users.
"""

import numpy as np
from typing import Union, Callable

def weightedMA(initial : float, rate : Union[float, Callable], length : int, decay : bool = True) -> np.ndarray:
    """
    Collate a Series based on Weighted Moving Average (WMA) Method

    WMA is a variant of SMA/EMA, and is popularly used in financial
    analysis, which gives more weightage to the recent data and
    produces a smoother line (sometimes) giving a more accurate picture
    of the underlying data trend.

    :type  initial: float
    :param initial: The initial weighteage of the value, typically
        a value of :attr:`0.5` is a good starting point.

    :type  rate: float, callable
    :param rate: The rate at which subsequent values are increasing
        or decreasing. Typically, a value of :attr:`2` (i.e., at each
        subsequent level the impact is halved - "half life decay") is
        a good starting point. The rate can either be a numeric value,
        i.e., each subsequent values is calculated as
        :attr:`n_1 = n_0 / rate` or can be a callable, i.e., each
        value is calculated like :attr:`n_1 = rate(n_0)` thus allow
        more control and dynamic approach.

    :type  length: int
    :param length: Length of the window, this enables a quick
        summarization of the final outcome using `x * weightedMA()`,
        where :attr:`x` is also a n-dimensional :attr:`numpy` array.

    :type  decay: bool
    :param decay: When true (default) the returned array will be
        reveresed, i.e., it will give more priority to the recent
        data points (where the :attr:`x` is sorted in ascending order),
        else typically returns a "growth" array where more weightage
        is given to the data which is older.
    """

    factors = [initial] # append the initial values, and then calculate
    for _ in range(length - 1):
        factors.append(
            rate(factors[-1]) if hasattr(rate, "__call__")
            else factors[-1] / rate
        )

    factors = np.array(factors)
    return factors[::-1] if decay else factors
