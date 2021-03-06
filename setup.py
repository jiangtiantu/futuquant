#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2017 Futu, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import sys
from os.path import dirname, join

from setuptools import (
    find_packages,
    setup,
)

with open(join(dirname(__file__), 'futuquant/VERSION.txt'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='futuquant',
    version=version,
    description='Futu Quantitative Trading API',
    classifiers=[],
    keywords='Futu HK/US Stock Quant Trading API',
    author='Futu, Inc.',
    author_email='ftdev@futunn.com',
    url='https://github.com/FutunnOpen/futuquant',
    license='Apache License 2.0',
    packages=find_packages(exclude=[]),
    package_data={'': ['*.*']},
    include_package_data=True,
    install_requires=[
    	"future",
			"vnpy >= 1.7.3",
			"pandas",
			"numpy",
			"matplotlib",
			"psutil",
			"simplejson",
			"protobuf",
			"PyCryptodome",
    ],
)
