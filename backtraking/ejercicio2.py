def subconjunto(nums,k):
    resultado = []
    
    def backtracking(inicio, actual):
        if len(actual)==k:
            resultado.append(actual[:])
            return
        for i in range(inicio, len(nums)):
            actual.append(nums[i])
            backtracking(i + 1,actual)
            actual.pop()
    backtracking([], 0)
    return resultado

print(subconjunto([1, 2, 3]))