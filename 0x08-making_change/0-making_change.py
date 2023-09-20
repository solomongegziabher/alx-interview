#!/usr/bin/python3
""" Change comes from within
"""


def makeChange(coins, total):
    """ Return the fewest number of coins needed to meet total
    """
    mx = total + 1
    dp = [0] + [mx for _ in range(total)]
    for i in range(1, len(dp)):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], dp[i - c] + 1)
    return dp[-1] if dp[-1] != total + 1 else - 1
