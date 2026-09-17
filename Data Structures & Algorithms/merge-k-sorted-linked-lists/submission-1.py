# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #just keep a heap of top elem in each list
        lis = ListNode() 
        ghostNode = lis
        heap = [] # min-heap of (val, id, node)
        heapq.heapify(heap) 
        id = 0
        for head in lists: 
            if head: 
                #print(head.val)
                heapq.heappush(heap, (head.val, id, head))
                id += 1
    
        while heap: 
            _, _, cur = heapq.heappop(heap)
            nextNode = cur.next 
            if nextNode: 
                heapq.heappush(heap, ( nextNode.val, id, nextNode))
                id += 1
            lis.next = cur 
            lis = lis.next
    
        return ghostNode.next
        



        

