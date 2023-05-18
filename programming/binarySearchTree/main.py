import sys



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)

    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root

def preorder(root, result=[]):
    if root is None:
        return 

    result.append(root.value)
    preorder(root.left, result)
    preorder(root.right, result)
    return result

def inorder(root, result=[]):
    if root is None:
        return

    inorder(root.left, result)
    result.append(root.value)
    inorder(root.right, result)
    return result

def postorder(root, result=[]):
    if root is None:
        return

    postorder(root.left, result)
    postorder(root.right, result)
    result.append(root.value)
    return result

for line in sys.stdin:
    nums = [int(i) for i in line.split(',')]

    root = None
    for num in nums:
        root = insert(root, num)

    print(preorder(root))
    print(inorder(root))
    print(postorder(root))
