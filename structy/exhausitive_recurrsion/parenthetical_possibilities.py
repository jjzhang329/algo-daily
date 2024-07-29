def parenthetical_possibilities(s):
  if len(s) == 0:
    return ['']
  remaining, chars = get_options(s)
  suffixes = parenthetical_possibilities(remaining)
  possibilities = []
  for char in chars:
    possibilities += [ char + suffix for suffix in suffixes ]
  return possibilities
  
def get_options(s):
  if s[0] == '(':
    idx = s.index(')')
    chars = s[1:idx]
    remaining = s[idx + 1:]
    return ( remaining, chars )
  else:
    chars = s[0]
    remaining = s[1:]
    return ( remaining, chars )