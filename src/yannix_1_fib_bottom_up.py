def fib_bottom_up(n):
    if n == 1 or n == 2:
        return 1
    bottom_up = [None] * (n+1)
    bottom_up[1] = 1
    bottom_up[2] = 1
    for i in range(3, n+1):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[n]

# Test outputs
print(f"F(2) = {fib_bottom_up(2)}")
print(f"F(3) = {fib_bottom_up(3)}")
print(f"F(4) = {fib_bottom_up(4)}")
print(f"F(10) = {fib_bottom_up(10)}")

