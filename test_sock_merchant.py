from sock_merchant import sock_merchant

def test_sock_merchant_basic():
    """Test the basic functionality of sock_merchant function"""
    assert sock_merchant([1, 2, 1, 2, 1, 3, 2]) == 2
    assert sock_merchant([10, 20, 20, 10, 10, 30]) == 2