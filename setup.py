import os
import re
import sys
import codecs

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


CURRENT_DIRECTORY = os.path.realpath(os.path.dirname(__file__))

TESTS_REQUIRES = (
    "pytest >= 3",
)

EXTRAS_REQUIRE = {
    "dev": TESTS_REQUIRES
}


class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass into py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = ["n", "1"]

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest

        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


def read(*paths):
    """This function aim to read from special
    files with special formatting using python
    codecs library.
    """

    path = os.path.join(CURRENT_DIRECTORY, *paths)

    with codecs.open(path) as stream:
        return stream.read()


def find_version(*file_paths):
    """Retrieve the version from a given file
    """
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = [\"']([^\"'']*)[\"']",
        version_file,
        re.M
    )

    if version_match:
        return version_match.group(1)

    raise RuntimeError("Unable to find version")


setup(
    name="lincl",
    version=find_version("lincl", "__init__.py"),
    description="Linux commands line",
    long_description=read("README.rst"),
    cmdclass={"test": PyTest},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="subprocess popen check_output check_call dynamicmethods",
    author="Christfried BALIZOU",
    author_email="christfriedbalizou@gmail.com",
    license="MIT",
    packages=find_packages(),
    entry_points={},
    tests_require=TESTS_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    include_package_data=True,
    python_requires=">=3.7"
)
