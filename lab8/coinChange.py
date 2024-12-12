def change(coins, amount):
    memo = {}

    def dp(rem):
        if rem == 0: return 0

        if rem < 0: return float('inf')

        if rem in memo: return memo[rem]

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, dp(rem - coin) + 1)

        memo[rem] = min_coins
        return memo[rem]
    
    result = dp(amount)

    return result if result != float('inf') else -1

coins = [1, 2, 5, 10]
amount = 11
print("гаралт: ", change(coins, amount))