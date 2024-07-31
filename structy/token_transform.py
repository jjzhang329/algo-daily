def token_transform(s, tokens):
  pass # todo
  i, j = 0, 1
  output = []
  while i < len(s):
    if s[i] != '$':
      output.append(s[i])
      
      i += 1
      j += 1
    elif s[j] != '$':
      j += 1
    else:
      token = s[i:j+1]
      value = tokens[token]
      evaluated = token_transform(value, tokens)
      tokens[token] = evaluated
      output.append(evaluated)
      i = j + 1
      j = i + 1

  return ('').join(output)

tokens = {
  '$LOCATION$': '$ANIMAL$ park',
  '$ANIMAL$': 'dog',
}
token_transform('Walk the $ANIMAL$ in the $LOCATION$!', tokens)
# -> 'Walk the dog in the dog park!'