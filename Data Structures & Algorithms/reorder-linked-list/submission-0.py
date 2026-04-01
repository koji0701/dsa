# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
Pattern: 
second half of linked list gets reversed 


then merge 2 lists: from start of first half + reversed second half

'''



class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find second half of linked list, fast slow 
        slow = head 
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #slow at middle 
        #reverse linked list from slow (mid) to end
        prev = None
        cur = slow

        while cur: 
            nextNode = cur.next 
            cur.next = prev 
            prev = cur 
            cur = nextNode 
        
        #second half is reversed. prev is the head
        #now, merge two linked lists. the second half, and the first half. 

        #merge prev and head 
        first = head 
        second = prev 

        while second.next: 
            nextSecond = second.next
            nextFirst = first.next 

            first.next = second 
            first = nextFirst 

            second.next = first 
            second = nextSecond

        








        