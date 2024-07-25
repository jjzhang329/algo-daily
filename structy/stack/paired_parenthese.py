def paired_parentheses(string):
  pass # todo
  stack = []
  for char in string:
    if char == '(':
      stack.append('(')
    elif char == ')':
      if not stack:
        return False
      stack.pop()

  return not stack