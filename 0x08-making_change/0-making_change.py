#!/usr/bin/python3

""" Given a pile of coins of different values, determine the
    fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """ Prototype: def makeChange(coins, total)
        Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any number of coins you have,
        return -1 coins is a list of the values of the coins in
        your possession.The value of a coin will always be an integer
        greater than 0. You can assume you have an infinite number of
        each denomination of coin in the list. Your solution’s runtime
        will be evaluated in this task.
    """
    if total <= 0:
        return 0

    if (coins is None or len(coins) == 0):
        return -1

    change = 0
    available_coins = sorted(coins, reverse=True)
    change_left = total

    for coin in available_coins:
        while (change_left % coin >= 0 and change_left >= coin):
            change += int(change_left / coin)
            change_left = change_left % coin

    change = change if change_left == 0 else -1

    return change
