

import setuptools
import re
pattern  = "^\\d{1,3}.\\d{1,3}.\\d{1,3}$"

test = "1.3.4567"

pattern = re.compile(pattern)
is_match = bool(pattern.match(test))

assert is_match is True


print(setuptools.find_packages(where="."))

