# Introduction
Useful for:
- sorting 
- implementing priority queues

## Two special properties
### Heaps must be complete binary trees

Some Complete Binary Tree Properties:
- All leaves are either at depth d or depth d-1
- The leaves at depth d are to the left of the leaves at depth d−1
- There is at most one node with just one child
- If the singular child exists, it is the left child of its parent
- If the singular child exists, it is the right most leaf at depth d.

### The nodes must be ordered according to the Heap order property
- Min Heap
- Max Heap

Max Heap Property:
key(A) >= key(B) where B is child of A

Min Heap Property:
key(A) <= key(B) where B is child of A

# Where are the Heaps used?
Get smallest or largest element: O(1)

Some famous algos implemented using Heaps:
- Prim's algorithm
- Dijkstra's algorithm
- Heap Sort algorithm

# Heap representation in Lists
0 at the root
left to right level wise in a tree

# Some common misconceptions
- Heap data structure is not same as heap memory
- Heap is not sorted at all (only largest or smallest is placed at top)

