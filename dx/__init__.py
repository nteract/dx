"""A Pythonic Data Explorer"""

__version__ = '0.3.0.dev0'


import pandas as pd

from .datasets import load_sample


def dx(dataframe, sampled=None):
    """Create dx from a dataframe"""
    # All the metadata keys that we'll apply for just the data explorer media
    # type, `application/vnd.dataresource+json`
    scoped_metadata = {}

    if sampled:
        scoped_metadata["sampled"] = sampled

    metadata = {"application/vnd.dataresource+json": scoped_metadata}

    with pd.option_context('display.html.table_schema', True):
        display(dataframe, metadata=metadata)


def enable():
    """Enable html table display"""
    pd.options.display.html.table_schema = True


def disable():
    """Disable html table display"""
    pd.options.display.html.table_schema = False
