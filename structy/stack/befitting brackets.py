def befitting_brackets(string):
  mapping = {'(':')', '[':']', '{':'}'}
  stack = []

  for char in string:
    if char in mapping:
      stack.append(char)
    else:
      if not stack or mapping[stack.pop()] != char:
        return False
        
  return not stack

befitting_brackets('(){}[](())') # -> True