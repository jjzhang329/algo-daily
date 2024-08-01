# For example, given these roads:

# 0 --- 1
# | \
# |  \
# |   \
# 2    3

# There is a unique route for between every pair of cities.
# So the answer is True.


# For example, given these roads:

# 0 --- 1
# | \
# |  \
# |   \
# 2 -- 3

# There are two routes that can be used to travel from city 1 to city 2:
# - first route:  1, 0, 2
# - second route: 1, 0, 3, 2 
# The answer is False, because routes should be unique.

def rare_routing(n, roads):
  pass # todo
  graph = build_graph(n, roads)
  visited = set()
  valid = traverse(graph, 0, visited, None)
  return valid and len(visited) == n

def traverse(graph, node, visited, last_node):
  if node in visited:
    return False 

  visited.add(node)
  for neighbor in graph[node]:
    if neighbor != last_node and not traverse(graph, neighbor, visited, node):
      return False 

  return True


def build_graph(n, roads):
  graph = {}
  for city in range(n):
    graph[city] = []

  for (a, b) in roads:
    graph[a].append(b)
    graph[b].append(a)

  return graph

rare_routing(4, [
  (0, 1),
  (0, 2),
  (0, 3),
  (3, 2)
]) # -> False