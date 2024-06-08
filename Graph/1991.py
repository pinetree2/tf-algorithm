# 트리순회
class Node:
  def __init__(self,data,left_node,right_node):
    self.data = data
    self.left_node=left_node 
    self.right_node=right_node 

# 전위 순회 (Preorder Traversal)
def preorder(node):
  print(node.data, end='')
  if node.left_node != None:
    preorder(tree[node.left_node])
  if node.right_node != None:
    preorder(tree[node.right_node])

# 중위 순회 (Inorder Traversal)
def inorder(node):
  if node.left_node != None:
    inorder(tree[node.left_node])
  print(node.data, end= '')
  if node.right_node != None:
    inorder(tree[node.right_node])


# 후위 순회 (Postorder Traversal)
def postorder(node):
  if node.left_node != None:
    postorder(tree[node.left_node])
  if node.right_node != None:
    postorder(tree[node.right_node])
  print(node.data, end='')

n = int(input())
tree = {}

for _ in range(n):
  data, left_node, right_node = input().split()
  if left_node == ".":
    left_node = None
  if right_node == ".":
    right_node = None
  tree[data] = Node(data, left_node, right_node)

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])