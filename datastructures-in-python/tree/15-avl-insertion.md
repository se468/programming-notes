# AVL Insertion
```
Node U – an unbalanced node
Node C – child node of node U
Node G – grandchild node of node U
```

# LL (Left-Left)
`Left-Left: Node C is the left-child of Node U, and Node G is left-child of Node C`
- Rotate node U towards right

# LR (Left-Right)
`Left-Right: Node C is the left-child of Node U, and Node G is right-child of Node C`

- Rotate node C towards left 
- Rotate node U towards right

# RR (Right-Right)
`Right-Right: Node C is the right-child of Node U, and Node G is right-child of Node C`
- Rotate node U towards left

# RL (Right-Left)
`Right-Left: Node C is right-child of Node U, and Node G is left-child of Node C`
- Rotate node C towards right
- Rotate node U towards left
