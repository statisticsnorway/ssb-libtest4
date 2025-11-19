from ssb_libtest4.functions import example_function
from ssb_libtest4.functions import is_prime


def test_example_function() -> None:
    assert example_function(1, 2) == "1 is less than 2"
    assert example_function(1, 0) == "1 is greater than or equal to 0"


def test_negative_numbers() -> None:
    assert is_prime(-10) is False
    assert is_prime(-1) is False
    assert is_prime(0) is False
    assert is_prime(1) is False


def test_small_primes() -> None:
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(5) is True
    assert is_prime(7) is True
    assert is_prime(11) is True


def test_small_composites() -> None:
    assert is_prime(4) is False
    assert is_prime(6) is False
    assert is_prime(8) is False
    assert is_prime(9) is False
    assert is_prime(12) is False


def test_larger_primes() -> None:
    assert is_prime(97) is True
    assert is_prime(101) is True
    assert is_prime(131) is True


def test_larger_composites() -> None:
    assert is_prime(100) is False
    assert is_prime(121) is False
    assert is_prime(143) is False
