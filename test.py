

import setuptools
import re
import os


folder_path = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(folder_path, "requirements.txt")
with open(file_path) as f:
    text = f.read()

packages_list = text.split("\n")
print(packages_list)