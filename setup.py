from setuptools import find_packages, setup

setup(
    name="spielwiese",
    packages=find_packages(include=["spielwiese"]),
    version="0.1",
    description="Collection of math scripts",
    author="Henrik Möllmann",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_requires=["pytest"],
    test_suite="tests",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/moellh/spielwiese",
)
