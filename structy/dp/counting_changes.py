# For example,
# counting_change(4, [1,2,3]) -> 4
# There are four different ways to make an amount of 4:
# 1. 1 + 1 + 1 + 1
# 2. 1 + 1 + 2
# 3. 1 + 3
# 4. 2 + 2

def counting_change(amount, coins):
  return _counting_change(amount, coins, 0, {})

def _counting_change(amount, coins, idx, memo):
  pass # todo
  key  = (amount, idx)
  if key in memo:
    return memo[key]
    
  if amount == 0:
    return 1
    
  if idx == len(coins):
    return 0

  coin = coins[idx]
  count = 0
  for qty in range(0, (amount//coin) + 1):
    remaining = amount - qty*coin 
    count += _counting_change(remaining, coins, idx+1, memo)
    
  memo[key] = count
  return memo[key]