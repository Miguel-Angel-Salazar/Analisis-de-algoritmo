def formas_memo(n, memo={}):
    if n == 0 or n == 1:
        return 1
    
    if n in memo:
        return memo[n]
    
    memo[n] = formas_memo(n-1, memo) + formas_memo(n-2, memo)
    return memo[n]

print(formas_memo(740))