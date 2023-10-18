<div align = "center">
<h1>Time Series Utilities</h1>
<p>object oriented process to create <b>time series <i>sequence</i> features</b> for AI/ML model development</p>
<a href = "#"><code>Colab <b>Notebook</b></code></a>
</div>

<br>

<div align = "justify">

**WARNING:** Merging all the time series gists into a single module.
  
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