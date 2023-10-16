class MovingAverage:
    """
    A Base Method for Moving Average based Forecasting Model
    
    A moving average is the most simple timeseries model, which is
    implemented using python. Note, the `.rolling` and `.cumsum`
    methods of `pandas` and `numpy` respectively is used internally
    where required to achieve the forecast.
    """
    
    def __init__(self, n_lookback : int, n_forecast : int, series : list) -> None:
        self.n_lookback = n_lookback
        self.n_forecast = n_forecast
        
        # the series is expected to have the same values as `looback`
        # else, an warning is raised and only the last `n` loockback values are kept
        self.series = self._check_series(series) # ? removes the values with warning
        
        
    def simple_ma(self) -> np.ndarray:
        series_ = self.series # make a copy of the original iterable
        forecast = [] # append the forecasted values to the list to return
        
        for _ in range(self.n_forecast):
            _iter_ma = series_.mean() # current iteration moving average
            
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