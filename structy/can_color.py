# For example, given this graph:

# x-y-z

# It is possible to color the nodes by using red for x and z, 
# then use blue for y. So the answer is True.

# For example, given this graph:

#     q
#    / \
#   s - r

# It is not possible to color the nodes without making two 
# adjacent nodes the same color. So the answer is False.

def can_color(graph):
  pass # todo
  color = {}
  for node in graph:
    if not node in color:
      if not traverse(graph, node, False, color):
        return False
      
  return True

def traverse(graph, node, coloring, color):
  if node in color:
    return color[node] == coloring 

  color[node] = coloring
  for neighbor in graph[node]:
    if not traverse(graph, neighbor, not coloring, color):
      return False 
  
  return True

can_color({
  "q": ["r", "s"],
  "r": ["q", "s"],
  "s": ["r", "q"]
}) # -> False