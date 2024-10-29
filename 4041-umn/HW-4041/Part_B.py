
#PartB.py
# name: M Ali ahsan



import math
import sys

class BinaryHeap:
    """A binary heap that depends on a compare function"""

    def __init__(self, compareFunction):
        """Constructor takes in a compare function (determines min / max heap)"""
        self.compareFunction = compareFunction
        self.heap = []

    def left(self, index):
        """Left node in a binary heap"""
        return 2*(index)+1

    def right(self, index):
        """Right node in a binary heap"""
        return 2*(index)+2

    def parent(self, index):
        """Parent node"""
        if index > 0:
            return (index+1)//2 - 1
        else:
            return -1

    def build_heap(self, list):
        """Builds a heap from a list"""
        self.heap = list
        for i in range(int(len(self.heap)/2-1), -1, -1):
            self.heapify(i)

    def size(self):
        """Returns the size of the heap."""
        return len(self.heap)

    def pop(self):
        """Pops the optimal element (min or max) and heapifies the full heap."""
        if (len(self.heap) > 0):
            top = self.heap[0];
            self.heap[0] = self.heap[len(self.heap)-1];
            self.heap.pop()
            self.heapify(0)
            return top
        else:
            return None
        
    def heapify(self, index):
        """Heapifies any subnode in the binary heap"""
        L = self.left(index)
        R = self.right(index)
        optimal = index
        if (L < len(self.heap) and self.compareFunction(self.heap[L], self.heap[index])):
            optimal = L
        if (R < len(self.heap) and self.compareFunction(self.heap[R], self.heap[optimal])):
            optimal = R
        if (optimal != index):
            tmp = self.heap[index]
            self.heap[index] = self.heap[optimal];
            self.heap[optimal] = tmp
            self.heapify(optimal)

    def display(self):
        """Display the heap for debug mode."""
        if (len(self.heap) == 0):
            return
        currentLevel = 0
        for i in range(0, len(self.heap)):
            level = int(math.log(i+1)/math.log(2))
            maxLevels = (math.log(len(self.heap))/math.log(2))
            spacing = ""
            for j in range(0, int(math.pow(2, maxLevels-level))):
                spacing = spacing + " "
            if (currentLevel < level):
                print("")
                currentLevel = level
            sys.stdout.write(spacing)
            sys.stdout.write(str(self.heap[i]))
        print("")



def max_compare(a, b):
    """Comparison function for a max heap."""
    return a > b

def min_compare(a, b):
    """Comparison function for a max heap."""
    return a < b

    ######################unchanged################

class PriorityQueue:
    """A priority queue implemented using the BinaryHeap."""

    def __init__(self, compareFunction):
        """Initialize the priority queue with a comparison function."""
        self.heap = BinaryHeap(compareFunction)

    def insert(self, item):
        """Insert an item into the priority queue."""
        self.heap.heap.append(item)
        self.heap.build_heap(self.heap.heap) 

    def maximum(self):
        """Return the maximum item without removing it."""
        return self.heap.heap[0] if self.heap.size() > 0 else None

    def extract_max(self):
        return self.heap.pop()


print("\033[96m\n{------------START------------------")                                        

if __name__ == "__main__":
    def max_compare(a, b):
        return a > b

    pq = PriorityQueue(max_compare)

    # (a) Add items to the priority queue
    items = [5, 2, 8, 10, 3, 1]
    for item in items:
        pq.insert(item)
        print(f"Inserted {item}, current max: {pq.maximum()}")
        


    # (b) Pop off a few items
    print("\nExtracting max items:")
    for _ in range(3):
        print(f"Extracted: {pq.extract_max()}, new max: {pq.maximum()}")


    # (c) Add low priority items
    print("\nAdding low priority items:")
    for item in [1, 0, 4 , 9]:
        pq.insert(item)
        print(f"Inserted {item}, current max: {pq.maximum()}")


    # (d) Add high priority items
    print("\nAdding high priority items:")
    for item in [15, 20, 40, 55]:
        pq.insert(item)
        print(f"Inserted {item}, current max: {pq.maximum()}")


    # (e) Final extraction of items
    print("\nFinal extraction of items:")
    while pq.heap.size() > 0:
        print(f"Extracted: {pq.extract_max()}, new max: {pq.maximum()}")

                                        
print("\n------------END------------------}\n\033[0m")