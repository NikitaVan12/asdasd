# from main import sum2
# import pytest
#
#
# def test():
#     assert sum2([1, 2, 3, 4, 5, 6]) == 21

from main import xxx
import pytest


def test():
    dct1 = {
        'a': 1,
        'b': 2,
    }
    dct2 = {
        'c': 3,
        'd': 4,
    }
    assert xxx(dct1, dct2) == {'a': 1,'b': 2,'c': 3,'d': 4,}