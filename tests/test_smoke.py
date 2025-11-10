from calculator import calculate_expression

def test_calculate_addition():
    assert calculate_expression('1 + 2 + 3') == '6'

def test_calculate_subtraction():
    assert calculate_expression('2 - 3') == '-1'

def test_calculate_multiplication():
    assert calculate_expression('2 * 5') == '10'

def test_calculate_divide():
    assert calculate_expression('10 / 5') == '2'

def test_calculate_addition2():
    assert calculate_expression('1 + 3') == '4'

def test_calculate_subtraction2():
    assert calculate_expression('10 - 5') == '5'

def test_calculate_multiplication2():
    assert calculate_expression('100 * 2') == '200'

def test_calculate_divide2():
    assert calculate_expression('200 / 100') == '2'

def test_smoke():
    assert True

def test_smoke1():
    assert True
