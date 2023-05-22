
# insertion with recursion
class Node:
    def __init__(self,key):
        self.left = None
        self.right = None
        self.val = key

def insert_value(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val > key:
            root.left = insert_value(root.right, key)
        elif root.val < key:
            root.right = insert_value(root.left, key)
    return root


def in_order(root):
    if root:
        in_order(root.left)
        print(root.val, end=" ")
        inorder(root.right)

root = Node(50)
root = insert_value(root, 69)
root = insert_value(root, 23)
in_order(root)