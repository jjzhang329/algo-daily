def can_concat(s, words):
  return _can_concat(s, words, {})
  
def _can_concat(s, words,memo):
  pass # todo
  if s in memo:
    return memo[s]
    
  if len(s) == 0:
    return True

  for word in words:
    if s.startswith(word):
      suffix = s[len(word):]
      if _can_concat(suffix, words, memo):
        memo[s] = True
        return True
  memo[s] = False
  return memo[s]