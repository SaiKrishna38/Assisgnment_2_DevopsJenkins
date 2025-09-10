def add(a, b):
    assert a > 0 and b > 0, "Both numbers must be positive integers"
    return a + b

def subtract(a, b):
    assert a > 0 and b > 0, "Both numbers must be positive integers"
    return a - b

def product(a, b):
    assert a > 0 and b > 0, "Both numbers must be positive integers"
    return a * b

if __name__ == "__main__":
    try:
        a = int(input("Enter first positive integer: "))
        b = int(input("Enter second positive integer: "))
        
        print(f"Addition: {add(a, b)}")
        print(f"Subtraction: {subtract(a, b)}")
        print(f"Product: {product(a, b)}")
        
    except ValueError:
        print("Error: Please enter valid integers")
    except AssertionError as e:
        print(f"Error: {e}")