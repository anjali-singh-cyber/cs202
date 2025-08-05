a = int(input("Enter a number a :"))
def factorial_recursive(a):
    if a < 0:
        return "Factorial is not defined for negative numbers."
    elif a == 0:
        return 1  # Base case: factorial of 0 is 1
    else:
        return a * factorial_recursive(a - 1)  # Recursive step
print(f"The factorial of {a} is {factorial_recursive(a)}")

