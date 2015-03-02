#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pip.download import PipSession
from pip.req import parse_requirements
import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import {{ cookiecutter.app_name }}
version = {{ cookiecutter.app_name }}.__version__

session = PipSession()

requirements = [
    str(req.req) for req in parse_requirements('requirements.txt', session=session)
]

setup(
    name='{{ cookiecutter.project_name }}',
    version=version,
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/pipermerriam/{{ cookiecutter.repo_name }}',
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    license="MIT",
    scripts=['{{ cookiecutter.app_name }}/manage.py'],
)
