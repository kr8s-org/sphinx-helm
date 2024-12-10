# sphinx-helm

[![PyPI - Version](https://img.shields.io/pypi/v/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/kr8s-org/sphinx-helm/test.yaml)](https://github.com/kr8s-org/sphinx-helm/actions/workflows/test.yaml)
[![Read the Docs](https://img.shields.io/readthedocs/sphinx-helm)](https://sphinx-helm.readthedocs.io/en/latest/)
[![PyPI - License](https://img.shields.io/pypi/l/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![EffVer Versioning](https://img.shields.io/badge/version_scheme-EffVer-0097a7)](https://jacobtomlinson.dev/effver)

sphinx-helm is a Sphinx plugin for automatically generating documentation for your [Helm charts](https://helm.sh/).


Features:

- Render documentation from your `Chart.yaml` and `values.yaml` files.
- Sphinx extension for including in Python documentation.
- Works with `.rst` and `.md` documentation source files.

## Installation

```
$ pip install sphinx-helm
```

## Usage

Add the extension to your Sphinx config.

```python
# conf.py

extensions = ['sphinx_helm.ext']
```

Use the directive to generate documentation for your helm chart.

### reStructuredText

```rst
.. helm:: path/to/your/helm/chart
```

### MyST Markdown

````markdown

```{helm} path/to/your/helm/chart

```

````
