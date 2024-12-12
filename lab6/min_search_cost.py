def min_search_cost(keys, freq):
    n = len(keys)
    dp = [[0] * n for _ in range(n)]
    freg_sum = [[0] * n for _ in range(n)]
    
    for i in range(n):
        freg_sum[i][i] = freq[i]
        for j in range(i+1, n):
            freg_sum[i][j] = freg_sum[i][j - 1] + freq[j]
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            for r in range(i, j+1):
                cost = (
                    (dp[i][r-1] if r > i else 0) +
                    (dp[r+1][j] if r < j else 0) +
                    freg_sum[i][j]
                )
                dp[i][j] = min(dp[i][j], cost)
    return dp[0][n-1]

keys = [5, 6]
freq = [17, 25]
print("min search cost: ", min_search_cost(keys, freq))
keys = [5, 10, 15]
freq = [10, 30, 20]
print("min search cost: ", min_search_cost(keys, freq))
