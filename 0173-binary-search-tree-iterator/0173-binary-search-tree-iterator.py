# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        
        self.order = []
        self.ptr = 0
        
        def in_order(node):
            if node:
                in_order(node.left)
                self.order.append(node.val)
                in_order(node.right)
        
        in_order(root)
        
    def next(self) -> int:
        self.ptr += 1
        return self.order[self.ptr - 1]

    def hasNext(self) -> bool:
        return self.ptr < len(self.order)


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()