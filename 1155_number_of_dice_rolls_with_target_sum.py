def numRollsToTarget(n,k,target):
    dp = [0] * (target+1)
    dp[0] = 1
    MOD = (10**9)+7
    for _ in range(n):
        next_dp = [0] * (target+1)
        for value in range(1,k+1):
            for total in range(val,target+1)
                next_dp[total] = (next_dp[total] + dp[total-value]) % MOD
        dp = next_dp
    return dp[target]

print(numRollsToTarget(1,6,3))
print(numRollsToTarget(2,6,7))
print(numRollsToTarget(30,30,500))
