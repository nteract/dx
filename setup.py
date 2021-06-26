#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python

from os.path import exists
from setuptools import setup

install_requires = []

extras_require = {"tests": ["pytest"]}

extras_require["all"] = list(set([val for k, v in extras_require.items() for val in v]))

setup(
    name="dx",
    version=None,
    cmdclass=None,
    description="data explorer",
    author="nteract contributors",
    author_email="carolcode@willingconsulting.com",
    license="BSD",
    keywords="data, exploration",
    long_description=(open("README.md").read() if exists("README.md") else ""),
    url="https://github.com/nteract/dx",
    packages=["dx"],
    package_data={"dx": []},
    install_requires=install_requires,
    extras_require=extras_require,
)
