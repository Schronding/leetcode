def coinChange(coins, amount):
    dp = [amount+ 1]*(amount+ 1)
    dp[0] = 0

    for a in range(1, amount + 1):
        for coin in coins:
            if a - coin >= 0:
                dp[a] = min(dp[a], 1 + dp[a - coin])
    if dp[amount] != amount + 1:
        return dp[amount]
    else:
        return -1

coins_0 = [1,2,5]
amount_0 = 11

coins_1 = [2]
amount_1 = 3

coins_2 = [1]
amount_2 = 0

coins_3 = [186,419,83,408]
amount_3 = 6249

print(coinChange(coins_0, amount_0))
print(coinChange(coins_1, amount_1))
print(coinChange(coins_2, amount_2))
print(coinChange(coins_3, amount_3))
