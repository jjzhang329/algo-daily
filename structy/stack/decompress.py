def decompress_braces(string):
  numbers = '123456789'
  stack = []
  for char in string:
    if char in numbers:
      stack.append(int(char))
    else:
      if char == '}':
        segment = ''
        while isinstance(stack[-1], str):
          popped = stack.pop()
          segment = popped + segment
        num = stack.pop()
        stack.append(segment * num)
      elif char != '{':
        stack.append(char)
  return ''.join(stack)