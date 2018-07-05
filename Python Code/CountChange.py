def countChange(amount, coins):
    return countChangeHelper(amount, coins, 0)
def countChangeHelper(amount, coins, index):
    if amount == 0: return 1
    if amount < 0: return 0
    if index >= len(coins): return 0
    
    return countChangeHelper(amount - coins[index], coins, index) + countChangeHelper(amount, coins, index + 1)

print countChange(15, [1,5,10,20,25,50])
