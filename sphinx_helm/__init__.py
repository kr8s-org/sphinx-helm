"""sphinx-helm."""

import os.path

from ._version import get_versions

__version__ = get_versions()["version"]
del get_versions

from .ext import setup, HelmDirective

__ALL__ = ["setup", "HelmDirective", "TEMPLATES_PATH"]

TEMPLATES_PATH = os.path.join(os.path.dirname(__file__), "templates")
