class Solution:
    def isBalanced(self, root):
        self.Bal = True
        
        def dfs(node):
            if not node: return 0
            lft, rgh = dfs(node.left), dfs(node.right)
            if abs(lft - rgh) > 1: self.Bal = False
            return max(lft, rgh) + 1
            
        dfs(root)
        return self.Bal