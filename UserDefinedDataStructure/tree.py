class Node:
    def __init__(self, letter):
        self.childleft = None
        self.childright = None
        self.nodedata = letter

root = Node('A')
root.childleft = Node('B')
root.childright = Node('C')
root.childleft.childleft = Node('D')
root.childleft.childright= Node('E')


#in order traversal
def InOrd(root):
    if root:
        InOrd(root.childleft)
        print(root.nodedata)
        InOrd(root.childright)

InOrd(root)


# pre order traversals

def preOrd(root):
    if root:
        print("-----",root.nodedata)
        preOrd(root.childleft)
        preOrd(root.childright)

preOrd(root)

def PostOrd(root):
    print("   ",root)
    if root:
        PostOrd(root.childleft)
        PostOrd(root.childright)
        print("post----",root.nodedata)
PostOrd(root)