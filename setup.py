# Copyright 2023 Katteli Inc.
# TestFlows.com Open-Source Software Testing Framework http://testflows.com)
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
from setuptools import setup

setup(
    name="testflows.combinatorics",
    version="__VERSION__",
    description="TestFlows - Combinatorics",
    author="Vitaliy Zakaznikov",
    author_email="vzakaznikov@testflows.com",
    readme="README.rst",
    url="https://github.com/testflows/testflows-combinatorics",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
    license="Apache-2.0",
    packages=[
        "testflows.combinatorics",
    ],
    zip_safe=False,
    install_requires=[],
    extras_require={"dev": ["testflows.core>=1.9"]},
)
