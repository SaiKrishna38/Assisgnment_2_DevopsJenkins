import calculator

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(4, 3) == 7
    print("All addition cases are passed")

def test_subtract():
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(12, 3) == 9
    print("All subtraction cases are passed")

def test_product():
    assert calculator.product(4, 1) == 4
    assert calculator.product(4, 9) == 36
    print("All product cases are passed")

if __name__ == "__main__":
    try:
        test_add()
        test_subtract()
        test_product()
        print("All test cases are successful")
    except AssertionError as e:
        print(f"\nTest failed: {e}")
    except Exception as e:
        print(f"\nError occurred: {e}")