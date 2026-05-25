class ListNode: 
    def __init__(self, key, val, next=None, prev=None): 
        self.next = next
        self.prev = prev
        self.val = val
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.startNode = ListNode(-1, -1)
        self.endNode = ListNode(-1, -1) 

        self.startNode.next = self.endNode 
        self.endNode.prev = self.startNode

        self.cache = {} #key : ListNode

        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.cache: 
            val = self.cache[key].val
            self._remove(key)
            self.put(key, val) 
            return val
        
        return -1 


    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self._remove(key)
        else: 
            if self.capacity <= 0:
                self._remove(self.startNode.next.key)

        #add to the end 
        self.cache[key] = ListNode(key, value) 

        curLastNode = self.endNode.prev 

        curLastNode.next = self.cache[key] 
        self.cache[key].prev = curLastNode 
        self.cache[key].next = self.endNode 
        self.endNode.prev = self.cache[key]
        self.capacity -=1 

    def _remove(self, key: int) -> None: 
        if key not in self.cache: 
            return 
        #removes from the list and the cache
        cur = self.cache[key]

        prevNode = cur.prev 
        nextNode = cur.next 
        prevNode.next = nextNode 
        nextNode.prev = prevNode 
        self.capacity += 1

        del self.cache[key]
        







