from setuptools import find_packages, setup

setup(
    name="mgfrofr",
    version="0.1.0",
    description="Official implementation of MgfrOFR for old film restoration",
    packages=find_packages(include=["mgfrofr", "mgfrofr.*", "basicofr", "basicofr.*", "basicsr", "basicsr.*"]),
    python_requires=">=3.8",
)
