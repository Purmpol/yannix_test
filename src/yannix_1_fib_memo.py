def fib_2(n, memo):
    if memo[n] is not None:
        return memo[n]
    if n == 1 or n == 2:
        result = 1
    else:
        result = fib_2(n-1, memo) + fib_2(n-2, memo)
    memo[n]  = result
    return result

def fib_memo(n):
    memo = [None] * (n + 1)
    return fib_2(n, memo)
 
# Test outputs
print(f"F(2) = {fib_memo(2)}")
print(f"F(3) = {fib_memo(3)}")
print(f"F(4) = {fib_memo(4)}")
print(f"F(10) = {fib_memo(10)}")
