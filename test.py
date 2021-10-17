

import setuptools
import re
pattern  = "^helpu-\\d{1,3}.\\d{1,3}.\\d{1,3}$"

test = "helpu-1.3.457"

pattern = re.compile(pattern)
is_match = bool(pattern.match(test))

assert is_match is True


print(setuptools.find_packages(where="."))

