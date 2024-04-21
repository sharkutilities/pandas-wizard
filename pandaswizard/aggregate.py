# -*- encoding: utf-8 -*-

"""
Utility Function(s) Related to a Grouped/Aggregated Data Frame

The basic syntax for the groupby aggregation is `pd.groupby().agg({})`
and the utility functions provided here can be applied under the
aggregation section.
"""

import warnings
import numpy as np
import pandas as pd

def __set_method__(kwargs : dict) -> str:
    """
    Set "Method"/"Interpolation" Attribute for Aggregated Function(s)

    Check individual function for attribute defination and usages.
    The function returns values as used by :func:`percentile` and
    :func:`quantile` methods defined below.
    """

    assert not all(["method" in kwargs, "interpolation" in kwargs]), \
        "Either `method` or `interpolation` is required. Received both."

    method = kwargs.get("method", kwargs.get("interpolation", "linear"))
    return method


def __set_basemod__(basemod : str) -> str:
    assert basemod in ["pd", "pandas", "np", "numpy"], \
        f"basemod = {basemod} is not valid, and/or not implemented."

    basemod = "pd" if basemod in ["pd", "pandas"] else "np"
    return basemod


def __calculate_quantile__(
            x : pd.Series,
            n : float,
            method : str,
            func : str,
            dropna : bool,
            basemod : str
    ) -> float:
    """
    Calculates Percentile/Quantile for a Grouped Series

    The function can calculate both percentile and/or quantile, but
    name is set as `__calculate_quantile__()` as default. Uses either
    the `numpy` or the `pandas` module to calculate the result.
    """

    retval = None # ? return value, i.e., quantile/percentile
    basemod = __set_basemod__(basemod) # ? defaults to pd (pandas)

    if basemod == "pd":
        # ? use pandas to calculate the series quantile/percentile
        # this is the default feature, and mimics np.nanquantile
        retval = x.quantile(n, interpolation = method)
    else:
        # ? else use numpy to calculate series quantile/percentile
        # ! this is always true, asserted in `__set_basemod__()`
        x = x.values # ? convert to an np.ndarray
        n = n * 100 if func == "percentile" else n

        __func_dispatcher__ = {
            "percentile" : {
                True : np.nanpercentile,
                False : np.percentile
            },
            "quantile" : {
                True : np.nanquantile,
                False : np.quantile
            }
        }

        try:
            retval = __func_dispatcher__[func][dropna](x, n, method = method)
        except TypeError as err:
            __ref_issue = "https://github.com/numpy/numpy/issues/21283"
            warnings.warn(
                f"NumPy/np Version < 1.22, {__ref_issue} Error: {err}",
                FutureWarning
            )

            # ? for older version, try with attribute `interpolation`, else
            # ! this should not raise error, unless legacy numpy version, OR
            # method/interpolation value is given for a newer version, not available
            try:
                retval = __func_dispatcher__[func][dropna](x, n, interpolation = method)
            except Exception as err:
                __warn_message = f"Cannot call attribute `method/interpolation` = {err}"
                warnings.warn(f"{__warn_message}. Returning value w/o argument", SyntaxWarning)
                retval = __func_dispatcher__[func][dropna](x, n)

    return retval


def percentile(n : float, outname : str = None, **kwargs) -> float:
    """
    Compute the n-th Percentile for the Grouped Data Series

    In statistics, a `n`-th percentile, also known as centile score,
    is a score below which a given percentage `n` of scores in its
    frequency distribution falls or a score at or below which the
    given percentage falls. More information is available
    [here](https://en.wikipedia.org/wiki/Percentile). Percentiles are
    a type of [*quanitile*](https://en.wikipedia.org/wiki/Quantile)
    and can be interchangeably used.

    Internally, the function uses the `pd.Series.quantile(n = n / 100)`
    method to calculate the n-th percentile of the grouped series.

    :type  n: int or float
    :param n: Percentage value to compute. Values must be between
        `[0, 100]` both inclusive.

    :type  outname: str
    :param outname: Output name of the aggregated feature when the
        method is used in conjuncture with other functions. This
        does not have any significance when used as in the below
        example. The outname defaults to `f"Q{n:.2f}"` formatting.

    Keyword Arguments
    -----------------
        * **method** (*str*): This parameter specifies the method to
            use for estimating the percentile. There are many
            different methods of which some are unique to NumPy.
            Accepts any value as in `np.percentile(method = )`
            parameter, defaults to "linear" method. However, for
            the `pd.Series.quantile()` the argument `method` is
            termed as `interpolation` and the values can be:
            {'linear', 'lower', 'higher', 'midpoint', 'nearest'}.

        * **interpolation** (*str*): Same as :attr:`method` the
            method for quantile calculation as per pandas. Both the
            attribute :attr:`method` and :attr:`interpolation` cannot
            be passed at the same time, and raises `AssertionError`
            if done so.

        * **basemod** (*str*): Abbreviation for "base module", allows
            the user to choose from `pandas` or `numpy` to calculate
            percentile. When choosing `numpy` the default behaviour
            is `np.nanquantile()` as followed by `pd.Series.quantile`
            however, you can pass `dropna = False` which calculates
            using `np.percentile` and returns `np.nan` if input
            contain nan values. Defaults to `pandas`. Allowed terms:
            {'pd', 'pandas', 'np', 'numpy'}.

        * **dropna** (*bool*): Calculate the percentile by dropping
            the `nan` values. This method mimics the `np.nanpercentile`
            function, which is the default as in `pd.Series.quantile()`.
            More information: https://stackoverflow.com/a/70002786.

    Example and Usages
    ------------------

    Assuming an end-user have the basic understanding of `pandas` and
    `percentile`, we can use compute the percentile for a group like:

    ```python
    import pandas as pd

    data = pd.DataFrame(data = {"G" : ["A", "B", "B"], "V" : [1, 2, 3]})

    # CASE-I: standalone usage, can be used on multiple features
    percentile = data.groupby("A").agg("V" : pdw.percentile(50))

    # CASE-II: usage in conjunture of any other accepted function
    percentile = data.groupby("A").agg("V" : [sum, pdw.percentile(50)])
    ```

    Both the methods calculates the percentile for the grouped value.
    In **CASE-I** the argument "outname" does not have any implications
    as `pandas` by default returns using the result with the original
    name, however in case of **CASE-II** we can set the feature name
    using the argument `outname`.
    """

    method = __set_method__(kwargs)

    # ? the validation and check are done in __calculate_quantile__()
    dropna = kwargs.get("dropna", True)
    basemod = kwargs.get("basemod", "pandas")

    def percentile_(x : list) -> float:
        return __calculate_quantile__(x, n = n / 100, method = method, func = "percentile", dropna = dropna, basemod = basemod)

    percentile_.__name__ = outname or f"P{n:.2f}"
    return percentile_


def quantile(n : float, outname : str = None, **kwargs) -> float:
    """
    Compute the n-th Quantile for the Grouped Data Series

    In statisticsand probability, quantiles are cut points dividing
    the range of probability distribution into continuous intervals
    with equal probabilities, or dividing the observation in a
    sample in the same way. More information is available
    [here](https://en.wikipedia.org/wiki/Quantile).

    Internally, the function uses the `pd.Series.quantile()` method
    to calculate the n-th quantile of the grouped series.

    :type  n: int or float
    :param n: Probability value for the quantiles to compute. The
        values must be between `[0, 1]` both inclusive.

    :type  outname: str
    :param outname: Output name of the aggregated feature when the
        method is used in conjuncture with other functions. This
        does not have any significance when used as in the below
        example. The outname defaults to `f"Q{n:.2f}"` formatting.

    Keyword Arguments
    -----------------
        * **method** (*str*): This parameter specifies the method to
            use for estimating the quantile. There are many
            different methods of which some are unique to NumPy.
            Accepts any value as in `np.quantile(method = )`
            parameter, defaults to "linear" method. However, for
            the `pd.Series.quantile()` the argument `method` is
            termed as `interpolation` and the values can be:
            {'linear', 'lower', 'higher', 'midpoint', 'nearest'}.

        * **interpolation** (*str*): Same as :attr:`method` the
            method for quantile calculation as per pandas. Both the
            attribute :attr:`method` and :attr:`interpolation` cannot
            be passed at the same time, and raises `AssertionError`
            if done so.

        * **basemod** (*str*): Abbreviation for "base module", allows
            the user to choose from `pandas` or `numpy` to calculate
            percentile. When choosing `numpy` the default behaviour
            is `np.nanquantile()` as followed by `pd.Series.quantile`
            however, you can pass `dropna = False` which calculates
            using `np.percentile` and returns `np.nan` if input
            contain nan values. Defaults to `pandas`. Allowed terms:
            {'pd', 'pandas', 'np', 'numpy'}.

        * **dropna** (*bool*): Calculate the percentile by dropping
            the `nan` values. This method mimics the `np.nanpercentile`
            function, which is the default as in `pd.Series.quantile()`.
            More information: https://stackoverflow.com/a/70002786.

    Example and Usages
    ------------------

    Assuming an end-user have the basic understanding of `pandas` and
    `quantile`, we can use compute the quantile for a group like:

    ```python
    import pandas as pd

    data = pd.DataFrame(data = {"G" : ["A", "B", "B"], "V" : [1, 2, 3]})

    # CASE-I: standalone usage, can be used on multiple features
    quantile = data.groupby("A").agg("V" : pdw.quantile(0.5))

    # CASE-II: usage in conjunture of any other accepted function
    quantile = data.groupby("A").agg("V" : [sum, pdw.quantile(0.5)])
    ```

    Both the methods calculates the quantile for the grouped value.
    In **CASE-I** the argument "outname" does not have any implications
    as `pandas` by default returns using the result with the original
    name, however in case of **CASE-II** we can set the feature name
    using the argument `outname`.
    """

    method = __set_method__(kwargs)

    # ? the validation and check are done in __calculate_quantile__()
    dropna = kwargs.get("dropna", True)
    basemod = kwargs.get("basemod", "pandas")

    def quantile_(x : list) -> float:
        return __calculate_quantile__(x, n = n, method = method, func = "quantile", dropna = dropna, basemod = basemod)

    quantile_.__name__ = outname or f"Q{n * 100:.2f}"
    return quantile_
