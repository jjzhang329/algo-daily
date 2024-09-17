# longest path
# Write a function, longest_path, that takes in an adjacency list for a directed acyclic graph. 
# The function should return the length of the longest path within the graph. 
# A path may start and end at any two nodes. 
# The length of a path is considered the number of edges in the path, not the number of nodes.

#using dfs to record the distance
#return the largest value of the distance

def longest_path(graph):
  pass # todo
  distance = {}
  
  for node in graph:
   if len(graph[node]) == 0:
     distance[node] = 0

  for node in graph:
    dfs(graph, node, distance)

  return max(distance.values())
  
def dfs(graph, node, distance):
  if node in distance:
    return distance[node]

  longest = 0

  for neighbor in graph[node]:
    size = dfs(graph, neighbor, distance)
    if size > longest:
      longest = size
      
  distance[node] = longest + 1
  
  return distance[node]



graph = {
  'a': ['c', 'b'],
  'b': ['c'],
  'c': []
}

longest_path(graph) # -> 2