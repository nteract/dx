from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

from .datasets import load_sample
import pandas as pd

def dx(dataframe, sampled=None):
    # All the metadata keys that we'll apply for just the data explorer media type, application/vnd.dataresource+json
    scoped_metadata = {}

    if sampled:
        scoped_metadata["sampled"] = sampled

    metadata = {
        "application/vnd.dataresource+json": scoped_metadata
    }

    with pd.option_context('display.html.table_schema', True):
        display(dataframe, metadata=metadata)

def enable():
    pd.options.display.html.table_schema = True

def disable():
    pd.options.display.html.table_schema = False
