
print("\033[95m\n{------------------------------\n")
                                      
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')
nodeH = TreeNode('H')

root.right =nodeB
root.left = nodeA

nodeA.right = nodeD
nodeA.left = nodeC

nodeB.right = nodeF
nodeB.left = nodeE

nodeC.right = nodeH
nodeC.left = nodeG

print("root.right.left:", root.right.left.data)
                                            
print("\n------------------------------}\n\033[0m")

# ***TREE***

# The Tree data structure is similar to Linked Lists in that each node
#     contains data and can be linked to other nodes.

# The Tree data structure can be useful in many cases:

# Hierarchical Data: File systems, organizational models, etc.
# Databases: Used for quick data retrieval.
# Routing Tables: Used for routing data in network algorithms.
# Sorting/Searching: Used for sorting data and searching for data.
# Priority Queues: Priority queue data structures are commonly
#      implemented using trees, such as binary heaps.
#-----------------------------------------------------------------------------

# A Binary Search Tree is a Binary Tree where every node's left child has a 
# lower value, and every node's right child has a higher value.

# A clear advantage with Binary Search Trees is that operations like search,
#  delete, and insert are fast and done without having to shift values in memory.


# AVL Trees:

# The only difference between a regular Binary Search Tree and an AVL Tree 
# is that AVL Trees do rotation operations in addition, to keep the tree balance.









print("\n------------------------------}\n\033[0m")