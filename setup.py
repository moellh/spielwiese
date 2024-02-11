from setuptools import find_packages, setup

setup(
    name = "nolib",
    packages = find_packages(include=["nolib"]),
    version = "0.1",
    description = "Numeric Operations Library",
    author = "Henrik Möllmann",
    install_requires = [],
    setup_requires = ["pytest-runner"],
    tests_requires = ["pytest"],
    test_suite = "tests",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/moellh/nolib",
)
