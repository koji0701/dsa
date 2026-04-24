# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
start at root and use the fact thats its a bst 
- swap so let p = smaller node, q = larger node 
- if cur node > p but is < q (aka, there is a divergence)
    -> that is the lowest common ancestor 

- else the cur node is > both nodes: 
    - traverse down to the right child 

- else the cur node is < both sides: 
    - traverse down to the left child 

'''


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val: 
            p, q = q, p
        print("p", p.val)
        print("q", q.val)
        
        cur = root 

        while cur is not None: 
            print(cur.val)
            if cur.val >= p.val and cur.val <= q.val: 
                print("returning", cur.val)
                return cur 
            elif cur.val > q.val: 
                cur = cur.left 
            elif cur.val < p.val: 
                cur = cur.right 
            else: 
                print("did something wrong")
                return None
        
        return cur 
















