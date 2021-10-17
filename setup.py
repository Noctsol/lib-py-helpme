"""
Date Created: 2021-10-17
Author: Noctsol
Summary:
    Config for releasing to pypi
"""

import setuptools
import os

print(os.getcwd())

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helpu",
    version="0.0.2",
    author="Noctsol",
    author_email="author@example.com",
    description="Package with useful methods. Makes life easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noctsol/lib-py-helpu",
    project_urls={
        "Documentation": "https://github.com/Noctsol/lib-py-helpu/wiki",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=["helpu"],
    python_requires=">=3.0",
)

