# -*- coding: utf-8 -*-

import os
import re

from setuptools import find_packages, setup

version = ""
with open("sentiment_analysis/__init__.py", encoding="UTF8") as f:
    version = re.search(
        r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE
    ).group(1)

path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")

requirements = []
with open(f"{path}/requirements.txt", encoding="UTF8") as f:
    requirements = f.read().splitlines()

if not version:
    raise RuntimeError("version is not defined")

readme = ""
with open(f"{path}/README.md", encoding="UTF8") as f:
    readme = f.read()

setup(
    name="sentiment-analysis-ko",
    author="kijk2869",
    url="https://github.com/kijk2869/sentiment-analysis-ko",
    project_urls={
        "Source": "https://github.com/kijk2869/sentiment-analysis-ko",
        "Tracker": "https://github.com/kijk2869/sentiment-analysis-ko/issues",
    },
    version=version,
    packages=find_packages(),
    license="MIT",
    description="Korean sentiment analyzation",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=requirements,
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
)