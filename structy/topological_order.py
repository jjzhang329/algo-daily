def topological_order(graph):
  pass # todo
  num_parents = {}
  for node in graph:
    num_parents[node] =  0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  ready = [ node for node in num_parents if num_parents[node] == 0 ]
  result = []
  while ready:
    node = ready.pop()
    result.append(node)
    for child in graph[node]:
      num_parents[child] -= 1 
      if num_parents[child] == 0:
        ready.append(child)

  return result