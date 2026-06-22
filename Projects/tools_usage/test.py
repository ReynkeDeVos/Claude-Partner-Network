import math

from main import calculate_pi


def test_calculate_pi_default():
    """Test calculate_pi with default parameter (5 digits)"""
    result = calculate_pi()
    expected = 3.14159
    print(f"Test 1 - Default (5 digits): {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ Test 1 passed!")


def test_calculate_pi_5_digits():
    """Test calculate_pi with 5 digits explicitly"""
    result = calculate_pi(5)
    expected = 3.14159
    print(f"Test 2 - 5 digits: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ Test 2 passed!")


def test_calculate_pi_2_digits():
    """Test calculate_pi with 2 digits"""
    result = calculate_pi(2)
    expected = 3.14
    print(f"Test 3 - 2 digits: {result}")
    assert result == expected, f"Expected {expected}, but got {result}"
    print("✓ Test 3 passed!")


def test_calculate_pi_accuracy():
    """Test that calculated pi is close to math.pi"""
    result = calculate_pi(5)
    math_pi_rounded = round(math.pi, 5)
    print(f"Test 4 - Accuracy check: {result} vs math.pi: {math_pi_rounded}")
    assert result == math_pi_rounded, f"Expected {math_pi_rounded}, but got {result}"
    print("✓ Test 4 passed!")


def test_calculate_pi_range():
    """Test that pi is in the expected range"""
    result = calculate_pi(5)
    print(f"Test 5 - Range check: {result}")
    assert 3.14159 <= result <= 3.14160, f"Pi value {result} is out of expected range"
    print("✓ Test 5 passed!")


if __name__ == "__main__":
    print("Running tests for calculate_pi function...")
    print("=" * 50)

    try:
        test_calculate_pi_default()
        test_calculate_pi_5_digits()
        test_calculate_pi_2_digits()
        test_calculate_pi_accuracy()
        test_calculate_pi_range()

        print("=" * 50)
        print("All tests passed! ✓")
        print(f"\nCalculated Pi to 5th digit: {calculate_pi(5)}")
        print(f"Actual math.pi:             {round(math.pi, 5)}")

    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
