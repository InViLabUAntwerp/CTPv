# setup.py
from setuptools import setup, find_packages

wx_dep = "wxPython>=4.2.3 ; sys_platform!='linux'"


setup(
    name="CTPv",
    version="0.2.3-2",
    description="A toolbox of camera, Plücker and transformation utilities",
    author="Rhys Evans & Seppe Sels",
    license="MIT",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=[
        "numpy",
        "matplotlib",
        "scikit-learn",
        "scipy",
        "open3d",
        "plyfile",
        "vispy",
        wx_dep
    ],
    python_requires=">=3.10",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
