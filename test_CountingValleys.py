from counting_valleys import counting_valleys
import pytest

@pytest.mark.counting
def test_counting_valleys():
    assert counting_valleys(8,"UDDDUDUU") == 1 