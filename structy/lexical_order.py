def detect_dictionary(dictionary, alphabet):
  pass # todo
  for i in range(1, len(dictionary)):
    if not valid_order(dictionary[i-1], dictionary[i], alphabet):
      return False 

  return True 

def valid_order(word1, word2, alphabet):
  for i in range(len(word1)):
    value1 = alphabet.index(word1[i]) if i < len(word1) else float('-inf')
    value2 = alphabet.index(word2[i]) if i < len(word2) else float('-inf')

    if value1 < value2:
      return True 
    elif value1 > value2:
      return False 

  return True