def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide (a,b):
    if b == 0:
        return "Error: Division by zero"
    return a/b

def calculate():
<<<<<<< HEAD
    `print("=== Team Calculator 1.0 ===")`
=======
    print("=== Team Calculator: Version A ===")
    print("Welcome to the Pair Calculator!")
>>>>>>> dd54e4bc966718be5eae925fc7beb9845442280a
    print("Addition: 5 + 3 =", add(5, 3))
    print("Subtraction: 5 - 3 =", subtract(5, 3))
    print("Multiplication 5 * 3 =", multiply(5, 3))

if __name__ == "__main__":
    calculate()