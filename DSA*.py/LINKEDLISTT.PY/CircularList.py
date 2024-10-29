
print("\033[95m\n{------------------------------\n")

# circular doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(10)
node2 = Node(100)
node3 = Node(1000)
node4 = Node(10000)

node1.next = node2
node1.prev = node4

node2.next = node3
node2.prev = node1

node3.next = node4
node3.prev = node2

node4.next = node1
node4.prev = node3


startNode = node1
currentNode = node1

print("forward: ")

print(currentNode.data, end=" -> ")
currentNode = currentNode.next

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next

print("...")
# #----------------------------------------------
print("\nBackward: ")
currentNode = node4
startNode = node4

print(currentNode.data, end=" -> ")
currentNode = currentNode.prev

while currentNode != startNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.prev

print("...")

print("\n------------------------------}\n\033[0m")
