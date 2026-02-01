# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        stack=[[root, root.val]]
        while stack:
            node, value=stack.pop()
            if node.val>=value:
                ans+=1
                value=node.val
            if node.left:
                stack.append([node.left,value])
            
            if node.right:
                stack.append([node.right, value])
        return ans