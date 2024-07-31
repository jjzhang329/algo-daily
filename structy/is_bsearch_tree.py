# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

#in order traversal should return the values as ascending orders
def is_binary_search_tree(root):
  pass # todo
  values = []
  in_order_traverse(root, values)
  return is_sorted(values)

def in_order_traverse(root, values):
  if root == None:
    return

  left = in_order_traverse(root.left, values)
  values.append(root.val)
  right = in_order_traverse(root.right, values)

def is_sorted(values):
  for i in range(1, len(values)):
    if values[i] < values[i-1]:
      return False 

  return True