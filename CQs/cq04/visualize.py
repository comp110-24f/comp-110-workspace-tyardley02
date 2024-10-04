"""Combining the concatenation and coordinates functions"""

__author__ = "730467229"

from concatenation import concat
from coordinates import get_coords

x: str = "123"
y: str = "abc"

print(concat(x, y))

get_coords(x, y)
