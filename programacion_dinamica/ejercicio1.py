def fibo_memo(n,memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    
    memo[n] = fibo_memo(n-1,memo) + fibo_memo(n-2,memo)
    return memo[n]