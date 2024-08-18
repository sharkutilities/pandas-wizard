<h1 align = "center">
  <img alt = "favicon" src = "https://raw.githubusercontent.com/sharkutilities/pandas-wizard/master/favicon.png" height = 250px><br>
  pandas-wizard
</h1>

<div align = "center">

[![Documentation Status](https://readthedocs.org/projects/pandas-wizard/badge/?version=latest&style=plastic)](https://pandas-wizard.readthedocs.io/en/latest/?badge=latest)
[![GitHub Issues](https://img.shields.io/github/issues/sharkutilities/pandas-wizard?style=plastic)](https://github.com/sharkutilities/pandas-wizard/issues)
[![GitHub Forks](https://img.shields.io/github/forks/sharkutilities/pandas-wizard?style=plastic)](https://github.com/sharkutilities/pandas-wizard/network)
[![GitHub Stars](https://img.shields.io/github/stars/sharkutilities/pandas-wizard?style=plastic)](https://github.com/sharkutilities/pandas-wizard/stargazers)
[![LICENSE File](https://img.shields.io/github/license/sharkutilities/pandas-wizard?style=plastic)](https://github.com/sharkutilities/pandas-wizard/blob/master/LICENSE)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/pandas-wizard?style=plastic)](https://pypistats.org/packages/pandas-wizard)
[![PyPI Latest Release](https://img.shields.io/pypi/v/pandas-wizard.svg?style=plastic)](https://pypi.org/project/pandas-wizard/)

[![GuardRails badge](https://api.guardrails.io/v2/badges/252923?token=3d0607cb31a1f48e15354fb326b65a0266e6f5ad60cd4f21f544ec8cb19dc6fb)](https://dashboard.guardrails.io/gh/sharkutilities/repos/252923)



</div>

<div align = "justify">

[**Pandas-Wizard (`pandaswizard`)**](https://github.com/sharkutilities/pandas-wizard) is a simple Python module for providing
utility functions and wrappers for the `pandas` module. The module is kept simple and use of external dependencies is minimized
unless needed to enhance performance.

This is a relatively new repository, and if you find any performance or improvement scope please check the
[contributing guidelines](https://github.com/sharkutilities/.github/blob/master/.github/CONTRIBUTING.md) for the organization.
All help and criticism are appreciated. If you find any additional use cases please create a pull request or submit for a
new feature.

## Getting Started

The source code is currently hosted at GitHub: [**sharkutilities/pandas-wizard**](https://github.com/sharkutilities/pandas-wizard).
The binary installers for the latest release are available at the [Python Package Index (PyPI)](https://pypi.org/project/pandas-wizard/).

```bash
pip install -U pandas-wizard
```

The list of changes between each release is available [here](./CHANGELOG.md).

The purpose of the below guide is to illustrate the main features of **pandas-wizard** and assume the working knowledge of
the [`pandas`](https://pypi.org/project/pandas/) module and use cases. The below example calculates the percentile of
`pandas.DataFrameGroupBy` object using [`np.percentile`](https://numpy.org/doc/stable/reference/generated/numpy.percentile.html).

```python
import pandaswizard as pdw # attempt to create an ubiquitous naming

# let's calculate the 50th-percentile, i.e. the median for each group
percentiles = df.groupby("group").agg({"A" : pdw.percentile(50)})
percentiles.head()

# or, preferred usage is to use in conjunture with other aggregation function like
statistics = df.groupby("group").agg({"A" : [sum, pdw.percentile(50), pdw.quantile(0.95)]})
statistics.head()
```

The above function calculates the 50th percentile, i.e., the median of the feature "A" based on the grouped column "group" from the data frame.

---

**Footnote:** The [favicon](./favicon.png) is designed from the original [`pandas`](https://pandas.pydata.org/static/img/pandas.svg) logo and no
copyright infringement is intended. Since the main objective is to provide a utility function for `pandas` the logo is re-used and developed
using [canva](https://www.canva.com/).

</div>
