# What is a Red-Black Tree?
- Every node is either Red or Black in color
- The root is always colored Black
- Two Red nodes cannot be adjacent, i.e., No red parent can have a red child and vice versa
- Each path from the root to None contains the same number of Black colored nodes
- The color of None nodes is considered Black

Although AVL Trees are technically more ‘balanced’ than Red-Black Trees, AVL Trees take more rotations during insertion and deletion operations than Red-Black Trees. 

* If you have search-intensive applications where insertion and deletion are not that frequent, use AVL Trees, otherwise, use Red-Black Trees.

