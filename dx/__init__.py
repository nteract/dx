
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

import pandas as pd

def dx(dataframe):
    with pd.option_context('display.html.table_schema', True):
        display(dataframe)

from .datasets import load_sample
