import pytest

# Multiplication Table Function
def create_multi_table(size):
    if size <= 0 or size > 12:
        raise IndexError("Size must be between 1 and 12")
    
    multi_table = [['X'] + list(range(1, size+1))]  # the first row
    for i in range(1, size+1):
        row = [i]  # the first column
        for j in range(1, size+1):
            row.append(i * j)  # calculate and append to the row
        multi_table.append(row)  # append the row to the table

    return multi_table

# Basic 1
# Tests basic tests 1A
def test_multi_table_1A_basic():
    multi_table = create_multi_table(5)
    assert multi_table[1][1] == 1

# Tests basic tests 1B
def test_multi_table_1B_basic():
    multi_table = create_multi_table(5)
    assert multi_table[1][5] == 5

# Tests basic tests 1C
def test_multi_table_1C_basic():
    multi_table = create_multi_table(5)
    assert multi_table[5][5] == 25

# Tests basic tests 1 Parametrized
@pytest.mark.parametrize("range, x, y, exp_result", [
    (5, 1, 1, 1),
    (5, 1, 5, 5),
    (5, 5, 5, 25)]
    )
def test_multi_table_1_basic_parametrized(range, x, y, exp_result):
    multi_table = create_multi_table(range)
    assert multi_table[x][y] == exp_result

# Basic 2
# Tests basic tests 2A
def test_multi_table_2A_basic():
    multi_table = create_multi_table(10)
    assert multi_table[1][1] == 1

# Tests basic tests 2B
def test_multi_table_2B_basic():
    multi_table = create_multi_table(10)
    assert multi_table[1][10] == 10

# Tests basic tests 2C
def test_multi_table_2C_basic():
    multi_table = create_multi_table(10)
    assert multi_table[10][10] == 100

@pytest.mark.parametrize("range, x, y, exp_result", [
    (10, 1, 1, 1),
    (10, 1, 10, 10),
    (10, 10, 10, 100)]
    )
def test_multi_table_2_basic_parametrized(range, x, y, exp_result):
    multi_table = create_multi_table(range)
    assert multi_table[x][y] == exp_result

# Xfail, we give parameters where it should fail and it will mark as Xfail when it fails.
# Run for each basic 2 test, plus a parametrized version
@pytest.mark.xfail
def test_multi_table_2_basic_xfail_1():
    multi_table = create_multi_table(10)
    assert multi_table[1][1] != 1

@pytest.mark.xfail
def test_multi_table_2_basic_xfail_2():
    multi_table = create_multi_table(10)
    assert multi_table[1][10] != 10

@pytest.mark.xfail
def test_multi_table_2_basic_xfail_3():
    multi_table = create_multi_table(10)
    assert multi_table[10][10] != 100

# Parametrized Xfails
@pytest.mark.parametrize("range, x, y, exp_result", [
    (10, 1, 1, 1),
    (10, 1, 10, 10),
    (10, 10, 10, 100)]
    )
@pytest.mark.xfail
def test_multi_table_2_basic_xfail_parametrized(range, x, y, exp_result):
    multi_table = create_multi_table(range)
    assert multi_table[x][y] != exp_result

# Should raise an index error, outside the range. 
def test_multi_table_index_error():
    try:
        create_multi_table(13)
    except IndexError:
        assert True
    else:
        assert False, "Expected IndexError but no exception was raised"

@pytest.mark.parametrize("input_size, expected_output", [
    (2, [['X', 1, 2], [1, 1, 2], [2, 2, 4]]),
    (3, [['X', 1, 2, 3], [1, 1, 2, 3], [2, 2, 4, 6], [3, 3, 6, 9]]),
    (4, [['X', 1, 2, 3, 4], [1, 1, 2, 3, 4], [2, 2, 4, 6, 8], [3, 3, 6, 9, 12], [4, 4, 8, 12, 16]]),
    (6, [['X', 1, 2, 3, 4, 5, 6], [1, 1, 2, 3, 4, 5, 6], [2, 2, 4, 6, 8, 10, 12], [3, 3, 6, 9, 12, 15, 18], [4, 4, 8, 12, 16, 20, 24], [5, 5, 10, 15, 20, 25, 30], [6, 6, 12, 18, 24, 30, 36]])
])

def test_multi_table_parametrized(input_size, expected_output):
    multi_table = create_multi_table(input_size)
    assert multi_table == expected_output