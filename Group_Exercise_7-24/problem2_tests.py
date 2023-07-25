import pytest

# Import the function we want to test
from problem2_func import calc_number_of_seconds

def test_calc_number_of_seconds():
    # Test Case 1: 1 second should return 1
    assert calc_number_of_seconds(1, "second") == 1

    # Test Case 2: 2 minutes should return 120 seconds
    assert calc_number_of_seconds(2, "minute") == 120

    # Test Case 3:  
    assert calc_number_of_seconds(1, 'hour') == 3600

    # Test Case 4:  
    assert calc_number_of_seconds(1, 'day') == 86400

    # Test Case 5:  
    assert calc_number_of_seconds(1, 'week') == 604800

    # Test Case 6:  
    assert calc_number_of_seconds(3, 'month') == 7776000

    # Test Case 7:  
    assert calc_number_of_seconds(2, 'year') == 63072000

    # Test Case 8: Negative time_period should raise an exception
    with pytest.raises(ValueError):
        calc_number_of_seconds(-5, "hour")

   # Test Case 8: Invalid unit type for second function value
    with pytest.raises(ValueError):
        calc_number_of_seconds(5, 5)

    # Test Case 9: Invalid string unit should raise an exception
    with pytest.raises(ValueError):
        calc_number_of_seconds(10, "years")


