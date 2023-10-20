<div align = "center">
<h1>Time Series Utilities</h1>
<p>object oriented process to create <b>time series <i>sequence</i> features</b> for AI/ML model development</p>
<a href = "#"><code>Colab <b>Notebook</b></code></a>
</div>

<br>

<div align = "justify">

**WARNING:** Merging all the time series gists into a single module.

## Stationarity & Unit Roots

Stationarity is one of the fundamental concepts in time series analysis. The **time series data model works on the principle that the [_data is stationary_](https://www.analyticsvidhya.com/blog/2021/04/how-to-check-stationarity-of-data-in-python/) and [_data has no unit roots_](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/)**, this means:
  * the data must have a constant mean (across all periods),
  * the data should have a constant variance, and
  * auto-covariance should not be dependent on time.

Let's understand the concept using the following example, for more information check [this link](https://www.analyticsvidhya.com/blog/2018/09/non-stationary-time-series-python/).

![Non-Stationary Time Series](https://cdn.analyticsvidhya.com/wp-content/uploads/2018/09/ns5-e1536673990684.png)

<div align = "center">

| ADF Test | KPSS Test | Series Type | Additional Steps |
| :---: | :---: | :---: | --- |
| ✅ | ✅ | _stationary_ | |
| ❌ | ❌ | _non-stationary_ | |
| ✅ | ❌ | _difference-stationary_ | Use differencing to make series stationary. |
| ❌ | ✅ | _trend-stationary_ | Remove trend to make the series _strict stationary. |

</div>

## Time Series Featuring

Time series analysis is a special segment of AI/ML application development where a feature is dependent on time. The code here is desgined to create a *sequence* of `x` and `y` data needed in a time series problem. The function is defined with two input parameters (I) **Lootback Period (T) `n_lookback`**, and (II) **Forecast Period (H) `n_forecast`** which can be visually presented below.

<div align = "center">

![prediction-sequence](https://i.stack.imgur.com/YXwMJ.png)

</div>

## Getting Started

The code is publically available at [**GitHub gists**](https://gist.github.com/ZenithClown) which is a simple platform for sharing *code snippets* with the community. To use the code, simply clone the code like:

```shell
git clone https://gist.github.com/ZenithClown/.git ts_utils
export PYTHONPATH="${PYTHONPATH}:ts_utils"
```

Done, you can now easily import the function with *python* notebooks/code-files like:

```python
from ts_featuring import CreateSequence
```

</div>