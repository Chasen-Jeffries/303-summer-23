import pytest

# Import the function we want to test
from problem2_func import calc_number_of_seconds

def test_calc_number_of_seconds_1():
    # Test Case 1: 1 second should return 1
    assert calc_number_of_seconds(1, "second") == 1

def test_calc_number_of_seconds_2():
    # Test Case 2: 2 minutes should return 120 seconds
    assert calc_number_of_seconds(2, "minute") == 120

def test_calc_number_of_seconds_3():
    # Test Case 3:  
    assert calc_number_of_seconds(1, 'hour') == 3600

def test_calc_number_of_seconds_4():
    # Test Case 4:  
    assert calc_number_of_seconds(1, 'day') == 86400

def test_calc_number_of_seconds_5():
    # Test Case 5:  
    assert calc_number_of_seconds(1, 'week') == 604800

def test_calc_number_of_seconds_6():
    # Test Case 6:  
    assert calc_number_of_seconds(3, 'month') == 7776000

def test_calc_number_of_seconds_7():
    # Test Case 7:  
    assert calc_number_of_seconds(2, 'year') == 63072000

def test_calc_number_of_seconds_8():
    # Test Case 8: Negative time_period should raise an exception
    with pytest.raises(Exception):
        calc_number_of_seconds(-5, "hour")

def test_calc_number_of_seconds_9():
   # Test Case 9: Invalid unit type for second function value
    with pytest.raises(Exception):
        calc_number_of_seconds(5, 5)

def test_calc_number_of_seconds_10():
    # Test Case 10: Invalid string unit should raise an exception
    with pytest.raises(Exception):
        calc_number_of_seconds(10, "years")

@pytest.mark.parametrize("a, b, result", [
    (1, 'second', 1),
    (2, 'minute', 120),
    (1, 'hour', 3600),
    (1, 'day', 86400),
    (1, 'week', 604800),
    (3, 'month', 7776000),
    (2, 'year', 63072000)]
    )
def test_calc_number_of_seconds_parametrized(num, unit, exp_result):
    num_seconds = calc_number_of_seconds(num, unit)
    assert num_seconds == exp_result

@pytest.mark.parametrize("a, b, result", [
    (-5, 'second', -5),
    (5, 5, 5),
    (10, 'years', 120)]
    )
def test_calc_number_of_seconds_exceptions_parametrized(num, unit, exp_result):
    with pytest.raises(Exception):
    	assert calc_number_of_seconds(num, unit) == exp_result