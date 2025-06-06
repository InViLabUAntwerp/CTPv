# setup.py
from setuptools import setup, find_packages

setup(
    name="core_toolbox_python",
    version="0.1.0",
    description="A toolbox of camera, Plücker and transformation utilities",
    author="Rhys Evans & Seppe Sels",
    license="MIT",
    packages=find_packages(where="."),
    install_requires=[
        "numpy",
        "matplotlib",
        "scikit-learn",
        "scipy",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
