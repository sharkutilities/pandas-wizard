<div align = "center">
<h1>Stationarity in Time Series Data</h1>
<p><b>Theory:</b>Understand Stationary and Non-Stationary in Time Series Data</p>
</div>

<br>

<div align = "justify">

Stationarity is one of the fundamental concepts in time series analysis. The **time series data model works on the principle that the [_data is stationary_](https://www.analyticsvidhya.com/blog/2021/04/how-to-check-stationarity-of-data-in-python/) and [_data has no unit roots_](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/)**, this means:
  * the data must have a constant mean (across all periods),
  * the data should have a constant variance, and
  * auto-covariance should not be dependent on time.

Let's understand the concept using the following example, for more information check [this link](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/).

![Non-Stationary Time Series](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/09/ns5-e1536673990684.png)

| ADF Test | KPSS Test | Series Type | Additional Steps |
| :---: | :---: | :---: | --- |
| ✅ | ✅ | _stationary_ | |
| ❌ | ❌ | _non-stationary_ | |
| ✅ | ❌ | _difference-stationary_ | Use differencing to make series stationary. |
| ❌ | ✅ | _trend-stationary_ | Remove trend to make the series _strict stationary. |

</div>
