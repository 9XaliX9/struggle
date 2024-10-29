print("\033[95m\n{------------------------------\n")

# Linked Lists

# A Linked List is, as the word implies, a list where the nodes are linked together.
#    Each node contains data and a pointer. The way they are linked together is that each
#    node points to where in the memory the next node is placed.

# Instead of storing a collection of data as an array, we can create a linked list.

x = 5
y = id(x)
print(type(y))

# A basic linked list in Python:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(3)
node2 = Node(5)
node3 = Node(13)
node4 = Node(2)

node1.next = node2
node2.next = node3
node3.next = node4

currentNode = node1
while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
print("null")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# There are three basic forms of linked lists:

# Singly linked lists
# Doubly linked lists
# Circular linked lists

# A singly linked list is the simplest kind of linked lists.
#   It takes up less space in memory because each node has only
#   one address to the next node.
# ------------------------------------------------------------------------
# Doubly linked lists

# A doubly linked list has nodes with addresses to both the
#   previous and the next node, and therefore takes up more memory.
#   But doubly linked lists are good if you want to be able
#   to move both up and down in the list.
# ------------------------------------------------------------------------
# Circular linked lists

# A circular linked list is like singly or doubly linked list with
#     the first node, the "head", and the last node, the "tail", connected.

# In singly or doubly linked lists, we can find the start and
# end of a list by just checking if the links are null. But for
# circular linked lists, more complex code is needed to
# explicitly check for start and end nodes in certain applications.

# Circular linked lists are good for lists you need to cycle through continuously.
# ------------------------------------------------------------------------
print("\n------------------------------}\n\033[0m")

# Basic things we can do with linked lists are:

# Traversal
# Remove a node
# Insert a node
# Sort

# 1) Traversal

# Traversing linked list means to go through the linked list
# by following the links from one node to the next.

# Traversal of linked lists is typically done to search for
# specific node, and read or modify the node's content, remove the
# node, or insert a node right before or after that node.

# To traverse a singly linked list, start with the first node
# in the list, the head node,-> follow that node's next link, and the next
# node's next link and so on, until the next address is null.

print("\033[95m\n{------------------------------\n")

class Node:
    def __init__(self,data,):
        self.data = data
        self.next = None

node1 = Node(2)
node2 = Node(4)
node3 = Node(6)
node4 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4

print("forward")

def Transverse(head):

    currentNode = head

    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("...")

Transverse(node1)

print("\n------------------------------}\n\033[0m")

print("\033[95m\n{------------------------------\n")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(20)
node2 = Node(40)
node3 = Node(60)
node4 = Node(80)
node5 = Node(100)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("...")

print("Traverse before deleting:\n")
traverse(node1)

print("\nTraverse after deleting:\n")

def deletingNode(head, nodeToDelete):

    if head == nodeToDelete:
        return head.next

    currentNode = head
    while currentNode.next and currentNode.next != nodeToDelete:
        currentNode = currentNode.next

    if currentNode.next is None:
        return head

    currentNode.next = currentNode.next.next
    return head


node1 = deletingNode(node1, node3)
traverse(node1)

print("\n------------------------------}\n\033[0m")
