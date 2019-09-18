# AVL tree
- For each node, height of left and right subtree can differ by at most one (balanced)
- At any point difference becomes more than one, tree gets re-balanced

# Time complexity
Insertion, deletion, search: 
O(h) - h is height of BST

Worst Case is O(n) - for skewed BSTs - where n is # of nodes in the tree

* AVL trees are essentially that: BSTs in the best-case.
