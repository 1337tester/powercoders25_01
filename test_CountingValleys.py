#from counting_valleys import counting_valleys
#import pytest

#@pytest.mark.counting
#def test_counting_valleys():
#    assert counting_valleys(8,"UDDDUDUU") == 1 

from counting_valleys import counting_valleys
import pytest

@pytest.mark.parametrize("a, b, expected", [
    (7, "UUUUDDD", 0),
    (8, "UDDDUDUU", 1),
    (12, "UUUUDDUDUUUD", 0),
    (10, "UDDDUUUDUU", 1),
    (10, "DDUUDDUDUU", 2),
    (8, "DDUUDDUD", 2),
    (6, "DUDDUD", 2),
    (5, "DUUUD", 1),
    (4, "DDUU", 1),
    (3, "DUU", 1)
])
def test_counting_valleys(a, b, expected):
    assert counting_valleys(a, b) == expected 