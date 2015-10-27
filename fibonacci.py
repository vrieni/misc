

#simple but horrible fibonacci algorithm
def fib(n):
    if n <= 2: f = 1
    else: f = fib(n-1) + fib(n-2)
    return f


#memoized fibonacci algorithm
memo = {}
def fib_memoized(n):
    if n in memo: return memo[n]
    if n <= 2: f = 1
    else: f = fib_memoized(n-1) + fib_memoized(n-2)
    memo[n] = f
    return f
