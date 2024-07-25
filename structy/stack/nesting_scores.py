def nesting_score(string):
  pass # todo
  stack = [0]

  for char in string:
    if char == '[':
      stack.append(0)
    else:
      last = stack.pop()
      if last == 0:
        stack[-1] += (1)
      else:
        stack[-1] += 2 * last
        
  return stack.pop()

nesting_score("[[][][]]") # -> 6