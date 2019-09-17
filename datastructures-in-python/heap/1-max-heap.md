# Building Max Heap
Start with empty heap, `insert()` all elements 

# Insertion in Max Heap
- Create child node at the end of heap
- Place new key at that node
- restore heap property by swapping parent and child if parent is smaller than child. (called `percolating up`).
- continue to percolate up until heap property is restored.

# Remove maximum in Max Heap
- Delete root node
- Move the key of last child node at last level to the root
- Now compare the key with its children and if the key is smaller than the key at any of the child nodes, swap values. (Max Heapifying)
- Continue to max heapify until heap property is restored.


#Implementation

```
class maxHeap:
  def __init__(self):
    self.heap = []
    
  def insert(self,val):
    self.heap.append(val)
    self.__percolateUp(len(self.heap) - 1)
  
  def getMax(self):
    if self.heap:
        return self.heap[0]
    return None
  
  def removeMax(self):
    if len(self.heap) > 1:
        max = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]
        self.__maxHeapify(0)
        return max
    elif len(self.heap) == 1:
        max = self.heap[0]
        del self.heap[0]
        return max
    else:
        return None
  
  def __percolateUp(self, index):
    parent = (index - 1) // 2
    if index <= 0:
        return
    elif self.heap[parent] < self.heap[index]:
        tmp = self.heap[parent]
        self.heap[parent] = self.heap[index]
        self.heap[index] = tmp
        self.__percolateUp(self,parent)
    
  def __maxHeapify(self,index):
    left = (index * 2) + 1
    right = (index * 2) + 2
    largest = index
    if len(self.heap) > left and self.heap[largest] < self.heap[left]:
        largest = left
    if len(self.heap) > right and self.heap[largest] < self.heap[right]:
        largest = right
    if largest != index:
        tmp = self.heap[largest]
        self.heap[largest] = self.heap[index]
        self.heap[index] = tmp
        self.__maxHeapify(largest)
  
heap = maxHeap()

```