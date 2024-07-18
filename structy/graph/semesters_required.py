# semesters required
# Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. 
# Courses have ids ranging from 0 through n - 1. 
# A single prerequisite of (A, B) means that course A must be taken before course B. 
# Return the minimum number of semesters required to complete all n courses. 
# There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.
# Note that given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. 
# You must take A in some semester before B.
# You can assume that it is possible to eventually complete all courses.

def semesters_required(num_courses, prereqs):
  pass # todo
  graph = build_graph(prereqs, num_courses)
  distance = {}
  for node in graph:
    if len(graph[node]) == 0:
      distance[node] = 1
      
  for node in graph:
      traverse(graph, node, distance)

  return max(distance.values())

def traverse(graph, node, distance):
  if node in distance:
    return distance[node]

  longest = 0
  for neighbor in graph[node]:
    paths = traverse(graph, neighbor, distance)
    if paths > longest:
      longest = paths 

  distance[node] = longest + 1 
  return distance[node]
  
def build_graph(preq, num_courses):
  graph = {}
  for num in range(num_courses):
    graph[num] = []

  for a, b in preq:
    graph[a].append(b)

  return graph
