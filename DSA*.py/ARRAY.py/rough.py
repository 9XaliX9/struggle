print("\033[96m\n{------------------------------")


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None



def InOrder(node):
    if node is None:
        return
    InOrder(node.left)
    print(node.data, end=" ")
    InOrder(node.right)

root = TreeNode('R')


nodeA = TreeNode('A')
nodeB = TreeNode('B')

nodeC = TreeNode('C')
nodeD = TreeNode('D')

nodeE = TreeNode('E')
nodeF = TreeNode('F')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF



print(root.left.right.data)
InOrder(root)



print("\n------------------------------}\n\033[0m")
