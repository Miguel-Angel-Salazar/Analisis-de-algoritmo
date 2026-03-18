def subconjunto(nums):
    resultado = []
    def backtracking(temp, start):
        resultado.append(temp[:])
        for i in range(start, len(nums)):
            temp.append(nums[i])
            backtracking(temp, i + 1)
            temp.pop()
    backtracking([], 0)
    return resultado

print(subconjunto([1, 2, 3]))