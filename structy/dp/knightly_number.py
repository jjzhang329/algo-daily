def knightly_number(n, m, kr, kc, pr, pc):
  return _knightly_number(n, m, kr, kc, pr, pc, {})

def _knightly_number(n, m, kr, kc, pr, pc, memo):
  pass # todo
  key = (kr, kc, m)
  if key in memo:
    return memo[key]
    
  deltas = [(2, 1), (1, 2), (1, -2), (-2, 1), (2, -1), (-1, 2), (-1, -2), (-2, -1)]

  row_inbound = 0 <= kr < n 
  col_inbound = 0 <= kc < n 

  if not row_inbound or not col_inbound or m < 0:
    return 0 

  if m == 0 and kr == pr and kc == pc:
    return 1
    
  path = 0
  
  for delta in deltas:
    r, c = delta
    path += _knightly_number(n, m-1, kr+r, kc+c, pr, pc, memo)
  memo[key] = path
  return memo[key]

knightly_number(8, 2, 4, 4, 5, 5) # -> 2