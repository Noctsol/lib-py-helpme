"""
Date Created: 2021-10-17
Author: Noctsol
Summary:
    Config for releasing to pypi via GitHub Workflows
"""



# Default Py Packagaes
import re
import os
import subprocess
import setuptools



# Gets the tag version numbers - for GitHub Workflows - Does not work locally
# Check is set to false because this will return nonzero status even though it works
git_tag_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE, check=False)
    .stdout.decode("utf-8")
    .strip()
)
print(f"--> Build #:{git_tag_version}")

# Checks that the tag version matches the format of 0[0][0].0[0][0].0[0][0]
pattern = re.compile("^\\d{1,3}.\\d{1,3}.\\d{1,3}$")
is_match = bool(pattern.match(git_tag_version))
assert is_match is True

# Reads the requirement.txt file in the root dir
folder_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(folder_path, "requirements.txt")
with open(file_path) as f:
    text = f.read()

# packages_list = text.split("\n")

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
    install_requires=[
        "uuid",
        "os",
        "datetime",
        "csv"
        ]
)
