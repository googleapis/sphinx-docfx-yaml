# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import codecs
from setuptools import setup, find_packages
extra_setup = dict(
install_requires=[
    'PyYAML',
    'wheel>=0.24.0',
    'sphinx',
    'unidecode',
],
setup_requires=['pytest-runner'],
tests_require=['pytest', 'mock'],
)

setup(
    name='sphinx-docfx-yaml',
    version='1.2.76',
    author='Eric Holscher',
    author_email='eric@ericholscher.com',
    url='https://github.com/googleapis/sphinx-docfx-yaml',
    description='Sphinx Python Domain to DocFX YAML Generator',
    package_dir={'': '.'},
    packages=find_packages('.', exclude=['tests']),
    # trying to add files...
    include_package_data=True,
    **extra_setup
)
