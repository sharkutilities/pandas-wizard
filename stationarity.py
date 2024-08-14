# -*- encoding: utf-8 -*-

"""
Stationarity Checking for Time Series Data

A functional approach to check stationarity using different models
and the function attrbutes are as defined below.
"""

from statsmodels.tsa.stattools import kpss # kpss test
from statsmodels.tsa.stattools import adfuller # adfuller test

def checkStationarity(frame : object, feature: str, method : str = "both", verbose : bool = True, **kwargs) -> bool:
    """
    Performs ADF Test to Determine Data Stationarity

    Given an univariate series formatted as `frame.set_index("data")`
    the series can be tested for stationarity using the Augmented
    Dickey Fuller (ADF) and Kwiatkowski-Phillips-Schmidt-Shin (KPSS)
    test. The function also returns a `dataframe` of rolling window
    for plotting the data using `frame.plot()`.

    :type  frame: pd.DataFrame
    :param frame: The dataframe that (ideally) contains a single
                  univariate feature (`feature`), else for a
                  dataframe containing multiple series only the
                  `feature` series is worked upon.

    :type  feature: str
    :param feature: Name of the feature, i.e. the column name
                    in the dataframe. The `rolling` dataframe returns
                    a slice of `frame[[feature]]` along with rolling
                    mean and standard deviation.

    :type  method: str
    :param method: Select any of the method ['ADF', 'KPSS', 'both'],
                   using the `method` parameter, name is case
                   insensitive. Defaults to `both`.
    """

    results = dict() # key is `ADF` and/or `KPSS`
    stationary = dict()

    if method.upper() in ["ADF", "BOTH"]:
        results["ADF"] = adfuller(frame[feature].values) # should be send like `frame.col.values`
        stationary["ADF"] = True if (results["ADF"][1] <= 0.05) & (results["ADF"][4]["5%"] > results["ADF"][0]) else False

        if verbose:
            print(f"Observations of ADF Test ({feature})")
            print("===========================" + "=" * len(feature))
            print(f"ADF Statistics  : {results['ADF'][0]:,.3f}")
            print(f"p-value         : {results['ADF'][1]:,.3f}")

            critical_values = {k : round(v, 3) for k, v in results["ADF"][4].items()}
            print(f"Critical Values : {critical_values}")

        # always print if data is stationary/not
        print(f"[ADF] Data is   :", "\u001b[32mStationary\u001b[0m" if stationary else "\x1b[31mNon-stationary\x1b[0m")

    if method.upper() in ["KPSS", "BOTH"]:
        results["KPSS"] = kpss(frame[feature].values) # should be send like `frame.col.values`
        stationary["KPSS"] = False if (results["KPSS"][1] <= 0.05) & (results["KPSS"][3]["5%"] > results["KPSS"][0]) else True

        if verbose:
            print(f"Observations of KPSS Test ({feature})")
            print("============================" + "=" * len(feature))
            print(f"KPSS Statistics : {results['KPSS'][0]:,.3f}")
            print(f"p-value         : {results['KPSS'][1]:,.3f}")

            critical_values = {k : round(v, 3) for k, v in results["KPSS"][3].items()}
            print(f"Critical Values : {critical_values}")

        # always print if data is stationary/not
        print(f"[KPSS] Data is  :", "\x1b[31mNon-stationary\x1b[0m" if stationary else "\u001b[32mStationary\u001b[0m")

    # rolling calculations for plotting
    rolling = frame.copy() # enable deep copy
    rolling = rolling[[feature]] # only keep single feature, works if multi-feature sent
    rolling.rename(columns = {feature : "original"}, inplace = True)

    rolling_ = rolling.rolling(window = kwargs.get("window", 12))
    rolling["mean"] = rolling_.mean()["original"].values
    rolling["std"] = rolling_.std()["original"].values

    return results, stationary, rolling
