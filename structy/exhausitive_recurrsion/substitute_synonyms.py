def substitute_synonyms(sentence, synonyms):
  words = sentence.split(' ')
  subarrays = generate(words, synonyms)
  return [ ' '.join(subarray) for subarray in subarrays ]

def generate(words, synonyms):
  if len(words) == 0:
    return [[]]
  
  first_word = words[0]
  remaining_words = words[1:]
  
  subarrays = generate(remaining_words, synonyms)
  
  if first_word in synonyms:
    result = []
    for synonym in synonyms[first_word]:
      result += [ [synonym, *subarray] for subarray in subarrays ]
    return result
  else:
    return [ [first_word, *subarray] for subarray in subarrays ]
  

sentence = "follow the yellow brick road"
synonyms = {
  "follow": ["chase", "pursue"],
  "yellow": ["gold", "amber", "lemon"],
}

substitute_synonyms(sentence, synonyms)
# [
#   'chase the gold brick road',
#   'chase the amber brick road',
#   'chase the lemon brick road',
#   'pursue the gold brick road',
#   'pursue the amber brick road',
#   'pursue the lemon brick road'
# ]