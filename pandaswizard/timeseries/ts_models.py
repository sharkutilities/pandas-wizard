# -*- encoding: utf-8 -*-

"""
A Set of Simplistic Time Series Models

A set of simplistic time series models developed on top of `pandas`
and `numpy` functionalities to provide quick analysis and develop a
base line for a univariate time series data.

.. caution::
    This will be a part of pandaswizard/functions module instead
    `GH/#29 <https://github.com/sharkutilities/pandas-wizard/issues/29>`_.
"""

import warnings
import numpy as np

class MovingAverage:
    """
    A Set of Moving Average (MA) based Models for Time Series Methods
    
    A moving average is the most simple timeseries model, which is
    implemented using python. However, when used well the MA model is
    able to provide much analysis and is one of the favorites for a
    quick understanding in the stock market.
    
    Note, the `.rolling` and `.cumsum` methods of `pandas` and
    `numpy` respectively is used internally where required to
    achieve the forecast.

    The model is an extension for moving average, and can be used to
    forecast into the future on a rolling basis. Example:

    ```python
    N_LOOKBACK = 4
    N_FORECAST = 5

    # given the series, the rolling forecast for `N_FORECAST` period:
    simple_ma = MovingAverage(
        n_lookback = N_LOOKBACK,
        n_forecast = N_FORECAST,
        series = np.array([12, 7, 27, 34])
    ).simple()

    >> np.array([20.00, 22.00, 25.75, 25.25, 23.00])
    ```

    :type  n_lookback: int
    :param n_lookback: Number of periods to lookback into the past.
                       Typically, 'n-lags' is a good indicator of
                       price, as the price of `(N+1)` is always a
                       factor of `N, N-1, N-2, ..., N-n` where `n`
                       can be determined statistically.

    :type  n_forecast: int
    :param n_forecast: Number of periods to forecast into the future.

    :type  series: iterable
    :param series: Time series data, where each item of the iterable
                   is a value at interval `n, ..., N-2, N-1, N` where
                   `N` is the value at current date.
    """
    
    def __init__(self, n_lookback : int, n_forecast : int, series : np.ndarray) -> None:
        self.n_lookback = n_lookback
        self.n_forecast = n_forecast
        
        # the series is expected to have the same values as `looback`
        # else, an warning is raised and only the last `n` loockback values are kept
        self.series = self._check_series(series) # ? removes the values with warning


    def simple(self) -> np.ndarray:
        """
        Simple Moving Average Forecast

        The most simple algorithm is the simple moving average
        which gives equal weightage to all the time, and does not
        consider level, trend, or seasonality.

        Simple moving average forecasting is not advisable, and is
        only applicable for data with low variations, i.e. the data
        is stationary.
        """

        series_ = self.series.copy() # make a copy of the iterable
        forecast = [] # append the forecasted values to the list

        for _ in range(self.n_forecast):
            _iter_ma = series_.mean()

            # pop fifo, and add latest iter
            series_ = np.insert(series_, len(series_), _iter_ma)
            series_ = np.delete(series_, 0)

            forecast.append(_iter_ma)

        return np.array(forecast)


    def exponential(self, alpha : float = 0.5) -> np.ndarray:
        """
        Exponential Moving Average Forecasting

        An exponential moving average is an extension of the
        moving average algorithm that places an greater weightage to
        the recent data points. The EMA is also referred to as the
        exponentially weighted moving average.

        Side note: In financial market, like all moving average
        metrices, the EMA is a technical indicator which is used to
        produce buy and sell signals based on crossovers and
        divergence on crossovers.
        (https://www.investopedia.com/terms/e/ema.asp)

        In addition, traders often use different EMA lengths of
        10-, 50-, and 200-days moving average as an indicator.

        However, in time series forecasting (like price forecasting)
        the order (`q`) can be determined from the ACF & PACF tests.
        But, in case of exponential smoothening/forecasting the order
        is referred as `alpha` which is the coefficient of level
        smoothening.

        EMA(T+1) = sum(
            alpha * EMA(T)
            + (alpha / 2) * EMA(T-1)
            + (alpha / 4) * EMA(T-2)
            + ...
            + (alpha / 2^n) * EMA(T-n)
        )

        where `n` is the lookback period, and `T` is the current day.

        :type  alpha: float
        :param alpha: The coefficient for level smoothening.
                      alpha ∈ (0, 1), typically the best value is 0.5
        """

        series_ = self.series.copy() # make a copy of the iterable
        forecast = [] # append the forecasted values to the list
        
        factors = alpha / (2 ** np.arange(1, stop = self.n_lookback + 1))

        for _ in range(self.n_forecast):
            _iter_ma = (series_ * factors).sum()

            # pop fifo, and add latest iter
            series_ = np.insert(series_, len(series_), _iter_ma)
            series_ = np.delete(series_, 0)

            forecast.append(_iter_ma)

        return np.array(forecast)


    def _check_series(self, series : list) -> list:
        """
        Data Sanity Check on the `series` and Return Cleaned Series

        Checks if the series length is expected as the `lookback`
        period, else returns a truncated data series with a simple
        warning.
        """

        if len(series) > self.n_lookback:
            warnings.warn(f"Series Length = {len(series)}, while Lookback = {self.n_lookback} Periods.")
            return series[-self.n_lookback :]
        elif len(series) < self.n_lookback:
            raise ValueError(f"Cannot compile, as {len(series)} < {self.n_lookback}. Check values.")
        else:
            return series



if __name__ == "__main__":
    N_LOOKBACK = 4
    N_FORECAST = 5

    series = np.array([12, 7, 27, 34])
    print(f"Given Series: {series}", end = "\n\n")

    model = MovingAverage(
        n_lookback = N_LOOKBACK,
        n_forecast = N_FORECAST,
        series = series
    )

    # calculate the simple moving average
    simple_ma = model.simple()
    print("Simple Moving Average:", end = "\n  ")
    print(simple_ma)

    # calculate the exponential moving average
    exponential_ma = model.exponential()
    print("Exponential Moving Average:", end = "\n  ")
    print(exponential_ma)
