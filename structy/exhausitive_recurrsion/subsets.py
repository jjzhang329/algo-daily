def subsets(elements):
  pass # todo
  if len(elements) == 0:
    return [[]]

  first = elements[0]
  exclude_first = subsets(elements[1:])
  include_first = []
  for sub in exclude_first:
    include_first.append([first, *sub])

  return exclude_first + include_first