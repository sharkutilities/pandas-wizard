# -*- encoding: utf-8 -*-

"""
Stationarity Checking for Time Series Data

@author:  Debmalya Pramanik
@version: v0.0.1
"""

from statsmodels.tsa.stattools import adfuller # adfuller test

def checkStationarity(frame : list, feature: str, verbose : bool = True, **kwargs) -> bool:
    """
    Performs ADF Test to Determine Data Stationarity

    Given an univariate series formatted as `frame.set_index("data")`
    the series can be tested for stationarity using the Augmented
    Dickey Fuller (ADF) test. The function also returns a `dataframe`
    of rolling window for plotting the data using `frame.plot()`.
    """

    results = adfuller(frame[feature].values) # should be send like `frame.col.values`
    stationary = True if (results[1] <= 0.05) & (results[4]["5%"] > results[0]) else False

    if verbose:
        print(f"Observations of ADF Test ({feature})")
        print("===========================" + "=" * len(feature))
        print(f"ADF Statistics  : {results[0]:,.3f}")
        print(f"p-value         : {results[1]:,.3f}")

        critical_values = {k : round(v, 3) for k, v in results[4].items()}
        print(f"Critical Values : {critical_values}")

    # rolling calculations for plotting
    rolling = frame.copy() # enable deep copy
    rolling = rolling[[feature]] # only keep single feature, works if multi-feature sent
    rolling.rename(columns = {feature : "original"}, inplace = True)

    rolling_ = rolling.rolling(window = kwargs.get("window", 12))
    rolling["mean"] = rolling_.mean()["original"].values
    rolling["std"] = rolling_.std()["original"].values

    print(f"Data is         :", "\u001b[32mStationary\u001b[0m" if stationary else "\x1b[31mNon-stationary\x1b[0m")
    return results, stationary, rolling
