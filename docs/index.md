# Sphinx-helm

[![PyPI - Version](https://img.shields.io/pypi/v/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/kr8s-org/sphinx-helm/test.yaml)](https://github.com/kr8s-org/sphinx-helm/actions/workflows/test.yaml)
[![Read the Docs](https://img.shields.io/readthedocs/sphinx-helm)](https://sphinx-helm.readthedocs.io/en/latest/)
[![PyPI - License](https://img.shields.io/pypi/l/sphinx-helm)](https://pypi.org/project/sphinx-helm/)
[![EffVer Versioning](https://img.shields.io/badge/version_scheme-EffVer-0097a7)](https://jacobtomlinson.dev/effver)

```{toctree}
:maxdepth: 2
:hidden: true
example
customizing
history
```

`sphinx-helm` is a [Sphinx](https://www.sphinx-doc.org/) plugin for automatically generating documentation for your [Helm charts](https://helm.sh/).

## Features

- Render documentation from your `Chart.yaml` and `values.yaml` files.
- Sphinx extension for including in Python documentation.
- Works with `.rst` and `.md` documentation source files.

## Installation

```console
$ pip install sphinx-helm
```

## Example

Create an example `hello-world` Helm chart with `helm create`.

```console
$ helm create hello-world
Creating hello-world
```

Enable the plugin in your Sphinx `conf.py` file:

```python
extensions = ['sphinx_helm.ext']
```

Now you can use the `helm` directive wherever you wish in your documentation.

```{note}
Helm Chart paths are relative to the root of your documentation.
```

### reStructuredText

```rst
.. helm:: path/to/your/helm/chart
```

### MyST Markdown

````markdown

```{helm} path/to/your/helm/chart

```

````
