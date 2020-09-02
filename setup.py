from setuptools import setup, find_packages

import os
import re

here = os.path.dirname(__file__)


def _get_version(*path):
    try:
        with open(os.path.join(here, *path)) as fp:
            m = re.compile(r".*__version__ = '(.*?)'", re.S).match(fp.read())
            return m.group(1)
    except Exception:
        return '0.0.0'

version = _get_version('src', 'pycure', '__init__.py')


def _read(name):
    try:
        with open(os.path.join(here, name)) as fp:
            return fp.read()
    except Exception:
        return ""

long_description = _read('README.rst')

install_requires = [
]

tests_require = [
    'testfixtures',
]

entry_points = {
    'console_scripts': [
    ],
}

setup(
    name="pycure",
    version=version,
    description="All about Japanese battle heroine \"Pretty Cure\"",
    long_description=long_description,
    classifiers=[
        "Development Status :: stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8.3",
        "Programming Language :: Python :: 3.9.0rc1",
        "Topic :: Utilities",
    ],
    author='Jiro',
    author_email='shun812linus@gmail.com',
    url='https://github.com/Ricotan-naboon/pycure',
    license='MIT License',
    package_dir={'': 'src'},
    packages=find_packages('src'),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'testing': tests_require,
    },
    test_suite='tests',
    entry_points=entry_points)
