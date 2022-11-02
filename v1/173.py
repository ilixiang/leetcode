class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        node = root
        while node != None:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node != None:
            self.stack.append(node)
            node = node.left
        return val
        
    def hasNext(self) -> bool:
        return len(self.stack) != 0
