
#from jumping_clouds import jumping_on_clouds
#import pytest

#@pytest.mark.jumping
#def test_jumping_clouds():
#    assert jumping_on_clouds(7, [0, 0, 1, 0, 0, 1, 0]) == 4

from jumping_clouds import jumping_on_clouds
import pytest

@pytest.mark.parametrize("n, c, expected", [
    (7, [0, 0, 1, 0, 0, 1, 0], 4),
    (6, [0, 0, 0, 0, 1, 0], 3),
    (6, [0, 0, 0, 1, 0, 0], 3),
    (2, [0, 0], 1),
    (8, [0, 0, 0, 0, 0, 1, 0, 0], 4),
    (1, [0], 0),
    (3, [0, 1, 0], 1)
])
def test_jumping_on_clouds(n, c, expected):
    assert jumping_on_clouds(n, c) == expected
