# -*- encoding: utf-8 -*-

"""
Utility Code(s) for Data Frame/Series Object Manipulation
"""

import numpy as np
import pandas as pd

from tqdm.notebook import tqdm as TQ
from typing import Any, Dict, Iterable, List, Tuple

def jsonify(
        frame : pd.DataFrame,
        dikey : List[str],
        dival : List[str],
        **kwargs
    ) -> Dict[Tuple[str, str], Iterable[Any] | Any]:
    """
    Convert a Data Frame into a JSON/Dictionary Object for Search

    A typical :class:`pd.DataFrame` requires multiple ``and`` clause
    in loop to search for a key and then get the relevant values using
    column slice. The function converts the data frame into an
    ``dict`` by setting the search key as the dictionary key in a
    ``tuple`` format and return relevant values.

    :type  frame: pd.DataFrame
    :param frame: A data frame object that needs to be converted to
        an iterable dictionary for faster searches.

    :type  dikey: List[str]
    :param dikey: A list of primary key (in specific order) that will
        be used for the dictionary indexation.

    :type  dival: List[str]
    :param dival: Value columns that will be the values in the output
        dictionary; strictly should be in the order of requirement.

    Keyword Arguments
    -----------------

    For finer data output control and refinement, use the following
    keyword arguments:

        * **dtype** (str | None): Final invered data type of the
            values, defaults to ``None``, i.e., the original data type
            is maintained.
        * **uselist** (bool): Return the values as a list or keep the
            :class:`np.ndarray` format; defaults to False, i.e., the
            array format is preserved.
        * **roundvalue** (bool): Round floating point values to the
            given decimal places; defaults to False.
        * **decimals** (int): Number of decimals if ``roundvalue`` is
            active to convert the value; defaults to 2.
        * **onduplicate** (str): If there is a duplicate primary key
            then what should be the behaviour of the function. By
            default, a dictionary directly updates the value without
            any warning. Available values are - (i) ``ignore`` -
            ignore duplicate keys and directly update to the last
            available value, (ii) ``raise`` (default) - raise an error
            if a duplicate key is found and stop the function.
        * **returnscalar** (bool): If ``len(dival) == 1`` and only
            the scalar value is required then returns a single value
            instead of an ``np.ndarray | list``, defaults to False.
        * **jobidentity** (str | None): Message for the :mod:`tqdm`
            progress bar, for understanding, defaults to None.
    """

    dtype : str | None = kwargs.get("dtype", None)
    uselist : bool = kwargs.get("uselist", False)
    roundvalue : bool = kwargs.get("roundvalue", False)
    decimals : int = kwargs.get("decimals", None)
    onduplicate : str = kwargs.get("onduplicate", "raise")
    returnscalar : bool = kwargs.get("returnscalar", False)
    jobidentity : str | None = kwargs.get("jobidentity", None)

    assert onduplicate in ["ignore", "raise"], "Invalid Value."

    outdict, n = dict(), frame.shape[0]
    jobidentity = f"JSONIFY({jobidentity})"

    for _, row in TQ(frame.iterrows(), total = n, desc = jobidentity):
        values = np.array(row[dival].values)
        values = np.array(row[dival].values, dtype = dtype) \
            if dtype else values
        values = np.round(values, decimals = decimals) \
            if roundvalue else values
        values = list(values) if uselist else values

        if returnscalar and len(values) == 1:
            values = values[0] # only the first index, one value
        else:
            raise ValueError("Return array has more than one value.")

        key = tuple(row[dikey]) # pk; in strict order
        if (key in outdict.keys()) and onduplicate == "raise":
            raise ValueError(f"Duplicate Key: {key}")
        else:
            outdict[key] = values

    return outdict
