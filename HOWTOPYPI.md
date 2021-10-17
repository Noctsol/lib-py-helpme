# Guide on how to Manually use PYPI
1. Make some repo and generate some class with some function in it to use
2. Manually create a *setup.py* file in the root directory with the following contents and fill it out:
```
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example-pkg-YOUR-USERNAME-HERE",
    version="0.0.1",
    author="Example Author",
    author_email="author@example.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
```
3. On your local computer, open CMD, and change to the root directory of your project using *cd [path]*
4. Run *python setup.py install* to install all the prequisite items to package python
5. Run *python -m pip install --upgrade build* to upgrade the tools used to compile tto a Python Artifact
6. Run *python -m build* to compile
7. Run *python3 -m pip install --upgrade twine* to upgrade/install the thing that actually uploads the packages
8. Run *py -m twine upload -u \_\_token\_\_ -p {pypiApiToken}* to upload to PYPI
    - Alternatively, you can run *py -m twine upload -u {pypiUser} -p {pypiPass}*