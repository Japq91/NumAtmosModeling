from setuptools import setup, find_packages

setup(
    name="atMOdel",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "xarray>=0.20.0",
        "matplotlib>=3.5.0",
        "pandas>=1.3.0",
        "pillow>=9.0.0"
    ],
)