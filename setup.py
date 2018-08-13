#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import versioneer

install_requires = []

extras_require = {"tests": ["pytest"]}

extras_require['all'] = list(
    set([val for k, v in extras_require.items() for val in v]))

setup(
    name='dx',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='data explorer',
    author='nteract contributors',
    author_email='jupyter@googlegroups.com',
    license='BSD',
    keywords="data, exploration",
    long_description=(open('README.md').read() if exists('README.md') else ''),
    url='https://github.com/nteract/dx',
    packages=['dx'],
    package_data={'dx': []},
    install_requires=install_requires,
    extras_require=extras_require)
