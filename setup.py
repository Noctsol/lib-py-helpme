"""
Date Created: 2021-10-17
Author: Noctsol
Summary:
    File for releasing to pypi
"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="helpme",
    version="0.0.1",
    author="Noctsol",
    author_email="author@example.com",
    description="Package with useful methods. Makes life easier",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Noctsol/lib-py-helpme",
    project_urls={
        "Documentation": "https://github.com/Noctsol/lib-py-helpme/wiki",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="helpme"),
    python_requires=">=3.9",
)