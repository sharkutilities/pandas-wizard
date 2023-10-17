from statsmodels.tsa.stattools import adfuller # adfuller test

def checkStationarity(series : list, verbose : bool = True, **kwargs) -> bool:
    """Performs ADF Test to Determine Data Stationarity"""

    results = adfuller(series) # should be send like `frame.col.values`
    stationary = True if (results[1] <= 0.05) & (results[4]["5%"] > results[0]) else False

    if verbose:
        print("Observations of ADF Test")
        print("========================")
        print(f"ADF Statistics  : {results[0]:,.3f}")
        print(f"p-value         : {results[1]:,.3f}")

        critical_values = {k : round(v, 3) for k, v in results[4].items()}
        print(f"Critical Values : {critical_values}")

    print(f"Data is         :", "\u001b[32mStationary\u001b[0m" if stationary else "\x1b[31mNon-stationary\x1b[0m")
    return results, stationary
