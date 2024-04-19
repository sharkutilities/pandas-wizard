<h1 align = "center">Pandas-Wizard</h1>

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
import pandaswizard as pdw

percentiles = df.groupby("group").agg({"A" : pdw.percentile(0.05)})
percentiles.head()
```

The above function calculates the 0.05, i.e., 5th percentile of the feature "A" based on the grouped column "group" from the data frame.

</div>
