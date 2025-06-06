# setup.py
from setuptools import setup, find_packages

setup(
    name="core_toolbox_python",
    version="0.1.0",
    description="A toolbox of camera, Plücker and transformation utilities",
    author="Your Name",
    author_email="you@example.com",
    license="MIT",
    packages=find_packages(where="."),          # automatically find core_toolbox_python.*
    install_requires=[
        "numpy",
        "matplotlib",        # mpl_toolkits comes along with matplotlib
        "scikit-learn",      # when you `import scipy` via sklearn, it will pull in scipy too
        "scipy",
    ],
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # If you have any data files, package_data=... etc.
)
