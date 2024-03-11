# -*- encoding: utf-8 -*-

"""
A set of Utilities Function extended from `pandas` Module

The `pandas` is the goto module for any data analysis and machine
learning based application or codes. This provides some additional
utilities functions that is extended from the module along with other
python in-built/basic modules like `os`, `glob` etc. The file name is
kept `pandas_` and is thus can be imported as:

```python
import pandas_ as pd_
pd_.<function-name>(*args, **kwargs)
```

The function is made in such a way that all the arguments and keyword
arguments of each internal functions is accepted by the module.

@author: Debmalya Pramanik
"""

import os
import glob
import time

import pandas as pd

from tqdm import tqdm as TQ
from typing import Iterable

class DataReader(object):
    """
    A Object Oriented approach is Defined to Read File(s)

    Extends the `pd.read_csv()` and `pd.read_excel()` functionalities
    to read comma seperated or excel bulk files and to perform
    additional data cleaning and optimization.

    :type  filepath: str
    :param filepath: Root directory that contains all the files, that
                     can be either `csv` or `xlsx` files. This can be
                     controlled using `filetype` parameter.
                     TODO define algorithms for different file types.

    :type  filetype: str
    :param filetype: Type of file that is to be read from directory.
                     Currently, only `csv` and `xlsx` file types are
                     supported. Raises `ValueError` if different type
                     is obtained.
    """

    def __init__(self, filepath : str, filetype : str = "csv", **kwargs) -> None:
        self.filepath = filepath
        self.filetype = filetype

        # ! check `filetype` integrity
        if self.filetype not in ["csv", "xlsx"]:
            raise ValueError(f"File type `{self.filetype}` is not yet supported.")
        else:
            # we now know the type of file, thus we can now define meta functions
            # this enables calling `self.func_(*args, **kwargs)`
            self.func_ = {
                "csv"  : pd.read_csv,
                "xlsx" : pd.read_excel
            }.get(self.filetype)

        # * additional arguments to control the workflow/environment
        for argument, value in kwargs.items():
            # https://stackoverflow.com/a/27732520/6623589
            setattr(self, argument, value)


    def __get_files__(self) -> Iterable:
        """
        Return a list of files on the directory based on the input
        filename. In addition, for excel file, ignores open cached
        files which is denoted with "~$<filiname>.xlsx" in windows
        system. Considers the `glob` module, and prints additional
        information based on module `verbose` level.
        """

        files = glob.glob(os.path.join(self.filepath, f"*.{self.filetype}"))

        if self.filetype == "xlsx":
            # ! ignore open cached temporary windows files
            files = [file for file in files if not file.startswith("~$")]

        return files
    

    def read_files(self, **kwargs) -> pd.DataFrame:
        """
        Read `N`-Files from a Directory and Return a Single DF

        Using the `glob.glob()` and `pd.read_*()` functionality, read
        all the files from a directory and return a single dataframe
        concatenated on axis, and ignored indexes. Typically, this
        function accepts all the keyword arguments supported by the
        `pandas.read_*()` function.
        """

        files = self.__get_files__() # get a list of all files

        print(f"{time.ctime()} : Reading {len(files)} Files from Directory.")
        frame = pd.concat([self.func_(file, **kwargs) for file in TQ(files)], ignore_index = True)
        
        return frame


def percentile(n : float) -> float:
    """
    Calculate the Percentile/Quantile of an Array

    The numpy function `np.quantile(x)` is used for calculating the
    quantile of a series of values, however the same is not available
    when using `pd.groupby().agg({})`. To overcome this, the
    `percentile()` function can be used to calculate aggregation on a
    grouped feature. Simply call the function like:

    ```python
    df.groupby("ID").agg({"price" : [min, percentile(0.50), max]})
    ```
    """

    def percentile_(x : Iterable[float]) -> float:
        return x.quantile(n) # ! np.quantile() used, for `ndarray`
    
    percentile_.__name__ = f"Q{n*100:.0f}"
    return percentile_
