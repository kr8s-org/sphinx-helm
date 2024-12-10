# Sphinx-helm

```{toctree}
:maxdepth: 2
:hidden: true
example
customizing
history
```

`sphinx-helm` is a [Sphinx](https://www.sphinx-doc.org/) plugin for automatically generating documentation for your [Helm charts](https://helm.sh/).

It will use the chart's `Chart.yaml` and `values.yaml` files in order to
generate the content in a markup language of your choice.

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
extensions = ['sphinx-helm.ext']
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
