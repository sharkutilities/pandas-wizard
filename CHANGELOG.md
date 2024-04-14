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
under `h3` tags, while the `micro` and "version identifiers" are listed under `h4` and subsequent headlines.

</div>
