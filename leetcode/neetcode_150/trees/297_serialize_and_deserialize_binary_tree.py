class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    null = 'null'
    index = 0

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []

        def helper(node):
            if node is None:
                res.append(self.null)
                return
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)

        helper(root)
        return ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')

        def helper():
            if data[self.index] == self.null:
                self.index += 1
                return None
            node = TreeNode(data[self.index])
            self.index += 1
            node.left = helper()
            node.right = helper()
            return node

        return helper()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
