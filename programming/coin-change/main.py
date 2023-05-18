import sys



def greedy_coin_change(coins, amount):
    coins.sort(reverse=True)
    result = 0
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result += 1
    return result

def dp_coin_change(coins, amount):
    dp = [0] * (amount + 1)
    for i in range(1, amount + 1):
        dp[i] = float('inf')
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
                
    return dp[amount]

for line in sys.stdin:
    coins, amount = line.strip().split()
    coins = [int(i) for i in coins.split(',')]
    amount = int(amount)

    result = dp_coin_change(coins, amount)
    print(result)

        
