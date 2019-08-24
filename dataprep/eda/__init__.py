
"""Docstring
    Data preparation module
"""
import tempfile

from bokeh.io import output_file, output_notebook

from ..utils import _rand_str, is_notebook
from .plot import plot
from .correlation import plot_correlation
from .missing import plot_missing

# Dask Default partitions
DEFAULT_PARTITIONS = 1

if is_notebook():
    output_notebook(hide_banner=True)
else:
    output_file(filename=tempfile.gettempdir() + '/' + _rand_str() + '.html')
