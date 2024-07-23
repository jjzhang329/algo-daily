def min_change(amount, coins):
  if _min_change(amount, coins, {}) == float('inf'):
    return -1 

  return _min_change(amount, coins, {})

def _min_change(amount, coins, memo):
  pass # todo
  if amount in memo:
    return memo[amount]
    
  if amount < 0:
    return float('inf')
    
  if amount == 0:
    return 0

  min_coins = float('inf')
  for coin in coins:
    num_coins = 1+ _min_change(amount-coin, coins, memo)
    if num_coins < min_coins:
      min_coins= num_coins
      
  memo[amount] = min_coins
  return min_coins

min_change(8, [1, 5, 4, 12]) # -> 2, because 4+4 is the minimum coins possible