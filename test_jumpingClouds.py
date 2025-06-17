
from jumping_clouds import jumping_on_clouds
import pytest

@pytest.mark.jumping
def test_jumping_clouds():
    assert jumping_on_clouds(7, [0, 0, 1, 0, 0, 1, 0]) == 4