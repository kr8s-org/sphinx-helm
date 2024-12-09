# sphinx-helm

sphinx-helm is a Sphinx plugin for automatically generating documentation for your [Helm charts](https://helm.sh/).

<!-- TODO: Add badges for CI, PyPI, etc -->

Features:

- Render documentation from your `Chart.yaml` and `values.yaml` files.
- Sphinx extension for including in Python documentation.
- Works with `rst` and `md` documentation source files.

## Installation

```
$ pip install sphinx-helm
```

## Usage

Add the extension to your Sphinx config.

```python
# conf.py

extensions = ['sphinx-helm.ext']
```

Use the directive to generate documentation for your helm chart.

```rst
.. helm:: path/to/your/helm/chart
```
