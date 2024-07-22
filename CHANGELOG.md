<h1 align = "center">CHANGELOG</h1>

<div align = "justify">

All notable changes to this project will be documented in this file. The format is based on
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [PEP0440](https://peps.python.org/pep-0440/)
styling guide. For full details, see the [commit logs](https://github.com/sharkutilities/pandas-wizard/commits).

## `PEP0440` Styling Guide

<details>
<summary>Click to open <code>PEP0440</code> Styilng Guide</summary>

Packaging for `PyPI` follows the standard PEP0440 styling guide and is implemented by the **`packaging.version.Version`** class. The other
popular versioning scheme is [`semver`](https://semver.org/), but each build has different parts/mapping.
The following table gives a mapping between these two versioning schemes:

<div align = "center">

| `PyPI` Version | `semver` Version |
| :---: | :---: |
| `epoch` | n/a |
| `major` | `major` |
| `minor` | `minor` |
| `micro` | `patch` |
| `pre` | `prerelease` |
| `dev` | `build` |
| `post` | n/a |

</div>

One can use the **`packaging`** version to convert between PyPI to semver and vice-versa. For more information, check
this [link](https://python-semver.readthedocs.io/en/latest/advanced/convert-pypi-to-semver.html).

</details>

## Release Note(s)

The release notes are documented, the list of changes to each different release are documented. The `major.minor` patch are indicated
under `h3` tags, while the `micro` and "version identifiers" are listed under `h4` and subsequent headlines. The legend for
changelogs are as follows:

  * 🎉 - **Major Feature** : something big that was not available before.
  * ✨ - **Feature Enhancement** : a miscellaneous minor improvement of an existing feature.
  * 🛠️ - **Patch/Fix** : something that previously didn’t work as documented – or according to reasonable expectations – should now work.
  * ⚙️ - **Code Efficiency** : an existing feature now may not require as much computation or memory.
  * 💣 - **Code Refactoring** : a breakable change often associated with `major` version bump.

### Version 1.0.0

We're pleased to annouce the first major release and preview-built for **`pandaswizard`**! This version mainly focuses on enduser
feedback and basic setup for the module.

### Version 1.1.0 | WIP

Moveing from `alpha` release to `stable` release. The following features are updated for the release as below:

  * 🎉 Added a wrapper function [`timeit`](./pandaswizard/wrappers.py) to print executed time for a function
    that returns a pandas dataframe object.

### Version 1.1.0a0 | Release Date: 21.04.2024

Moving from `development` release to `alpha` testing release, the version brings the additional new features and/or enhancements for
the module:

  * 🎉 Added **`pdw.wrappers`** module housing useful decorators,
  * 🛠️ ([#7](https://github.com/sharkutilities/pandas-wizard/issues/7)) For legacy/`np < 1.22` try to return the aggregated
    value using "interpolation" attribute.
  * 🎉📃 Basic code documentation is now available, hosted using
    [readthedocs/pandas-wizard](https://pandas-wizard.readthedocs.io/en/latest/index.html)

### Version 1.1.0.dev0 | Release Date: 20.04.2024

Major enhancement of the preview built, also created an favicon and logo for the project. The logo is modified from the original
pandas logo.

  * ⚙️ Added two new functions `__set_method__()` and `__calculate_quantile__()` to reduce code duplicacy,
  * ✨ ([#3](https://github.com/sharkutilities/pandas-wizard/issues/3)) Added the ability to choose from either `pandas` or `numpy`
    to calculate grouped result:
    - ✨ allows the user to choose any of the *method* to calculate based on `numpy` documentations,
    - 💣 numpy version requirement is `numpy >= 1.22` due to argument change `interpolation` to `method`
      more [details](https://github.com/numpy/numpy/issues/21283).

#### Version 1.0.1.dev0 | Release Date: 19.04.2024

The first `dev` or `preview-build` for `v1.0.0` focusing on function development and objective documentation. The version
focuses on providing basic features like:

  * 🎉 `pandaswizard.quantile`: A simple function to calculate quantile of a grouped data series,
  * 🎉 `pandaswizard.percentile`: A simple function to calculate percentile of a grouped data series.

</div>
