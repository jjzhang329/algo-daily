def safe_cracking(hints):
  pass # todo
  graph = build_graph(hints)
  return topological_order(graph)

def topological_order(graph):
  num_parents = {}

  for node in graph:
    num_parents[node] = 0

  for node in graph:
    for child in graph[node]:
      num_parents[child] += 1

  ready = [ node for node in graph if num_parents[node] == 0 ]
  order = []

  while ready:
    node = ready.pop()
    order.append(str(node))

    for child in graph[node]:
      num_parents[child] -= 1
      if num_parents[child] == 0:
        ready.append(child)
  
  return ('').join(order)
  
def build_graph(hints):
  graph = {}

  for (a, b) in hints:
    if a not in graph:
      graph[a] = []

    if b not in graph:
      graph[b] = []

    graph[a].append(b)

  return graph