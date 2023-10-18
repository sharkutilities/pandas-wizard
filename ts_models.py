# -*- encoding: utf-8 -*-

"""
A Set of Simplistic Time Series Models

A set of simplistic time series models developed on top of `pandas`
and `numpy` functionalities to provide quick analysis and develop a
base line for a univariate time series data.

@author:  Debmalya Pramanik
@version: v0.0.1
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
        series_ = self.series # make a copy of the original iterable
        forecast = [] # append the forecasted values to the list to return
        
        for _ in range(self.n_forecast):
            _iter_ma = series_.mean() # current iteration moving average
            
            # pop fifo, and add latest iter
            series_ = np.insert(series_, len(series_), _iter_ma)
            series_ = np.delete(series_, 0)
            
            forecast.append(_iter_ma)
            
        return np.array(forecast)
    
    
    def exponential(self, factor : float = 0.5) -> np.ndarray:
        series_ = self.series # make a copy of the original iterable
        forecast = [] # append the forecasted values to the list to return
        
        factors = [factor / (2 ** i) for i in range(self.n_forecast)]
        
        for _ in range(self.n_forecast):
            _iter_ma = (series_ * factors).sum() # current iteration moving average
            
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