"""
Date Created: 2021-10-17
Author: Noctsol
Summary:
    Config for releasing to pypi
"""


# Default Py Packagaes
import subprocess
import setuptools




# Gets the tag version numbers
git_tag_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, check=True)
    .stdout.decode("utf-8")
    .strip()
)

# Read the README file to get a long description for the package
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Mimic a setup cgf
setuptools.setup(
    name="helpu",
    version=git_tag_version,
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

