#!/usr/bin/python3

from TreeNode import TreeNode

class Codec:
    def serialize(self, root):
        queue = [root]
        vals = []
        while len(queue) != 0:
            node = queue.pop(0)
            if node:
                queue.append(node.left)
                queue.append(node.right)
                vals.append(str(node.val))
            else:
                vals.append('n')
        return ':'.join(vals)
    
    def deserialize(self, data):
        if data == 'n':
            return None

        vals = data.split(':')
        root = TreeNode(int(vals[0]))
        queue = [root]
        for i in range(1, len(vals)):
            val = vals[i]
            node = TreeNode(int(val)) if val != 'n' else None
            if node:
                queue.append(node)
            if i & 1 == 1:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.pop(0)
        return root
