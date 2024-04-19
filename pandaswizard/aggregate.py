# -*- encoding: utf-8 -*-

"""
Utility Function(s) Related to a Grouped/Aggregated Data Frame

The basic syntax for the groupby aggregation is `pd.groupby().agg({})`
and the utility functions provided here can be applied under the
aggregation section.
"""

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
            parameter, defaults to "linear" method.

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

    method = kwargs.get("method", "linear")

    def percentile_(x : list) -> float:
        return x.percentile(n, method = method)

    percentile_.__name__ = outname or f"Q{n:.2f}"
    return percentile_

def quantile(n : float, outname : str = None, **kwargs) -> float:
    """
    Compute the n-th Quantile for the Grouped Data Series

    In statisticsand probability, quantiles are cut points dividing
    the range of probability distribution into continuous intervals
    with equal probabilities, or dividing the observation in a
    sample in the same way. More information is available
    [here](https://en.wikipedia.org/wiki/Quantile).

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
            parameter, defaults to "linear" method.

    Example and Usages
    ------------------

    Assuming an end-user have the basic understanding of `pandas` and
    `quantile`, we can use compute the quantile for a group like:

    ```python
    import pandas as pd

    data = pd.DataFrame(data = {"G" : ["A", "B", "B"], "V" : [1, 2, 3]})

    # CASE-I: standalone usage, can be used on multiple features
    quantile = data.groupby("A").agg("V" : pdw.quantile(50))

    # CASE-II: usage in conjunture of any other accepted function
    quantile = data.groupby("A").agg("V" : [sum, pdw.quantile(50)])
    ```

    Both the methods calculates the quantile for the grouped value.
    In **CASE-I** the argument "outname" does not have any implications
    as `pandas` by default returns using the result with the original
    name, however in case of **CASE-II** we can set the feature name
    using the argument `outname`.
    """

    method = kwargs.get("method", "linear")

    def quantile_(x : list) -> float:
        return x.quantile(n, method = method)

    quantile_.__name__ = outname or f"Q{n:.2f}"
    return quantile_
