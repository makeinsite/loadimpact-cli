"""
Copyright 2015 Load Impact

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

from setuptools import setup

import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'loadimpactcli'))

from version import __version__

setup(
    name='loadimpact-cli',
    version=__version__,
    author='Load Impact',
    author_email='support@loadimpact.com',
    packages=['loadimpactcli'],
    py_modules=['loadimpactcli'],
    include_package_data=True,
    install_requires=[
        'click',
        'loadimpact',
        'tzlocal',
        'six',
    ],
    entry_points={
        'console_scripts': [
            'loadimpact=loadimpactcli.loadimpact_cli:run_cli',
        ],
    },
    test_suite='tests'
)