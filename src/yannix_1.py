def Fibonacci(n):
    # check if input < 0
    if n < 0:
        print("Invalid input")
 
    # F(0) = 0
    elif n == 0:
        return 0

    # F(1) = 1, F(2) = 1
    elif n == 1 or n == 2:
        return 1
    else:
        # Do recursive function
        return Fibonacci(n-1) + Fibonacci(n-2)
 
# Test outputs
print(f"F(2) = {Fibonacci(2)}")
print(f"F(3) = {Fibonacci(3)}")
print(f"F(4) = {Fibonacci(4)}")
print(f"F(10) = {Fibonacci(10)}")
