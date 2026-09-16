class CacheNode: 
    def __init__(self, key: int, val: int): 
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.keyVals = {}

        self.ghostHead = CacheNode(-1, 0) 
        self.ghostTail = CacheNode(-2, 0)
        self.ghostHead.next = self.ghostTail
        self.ghostTail.prev = self.ghostHead


    def get(self, key: int) -> int:
        if key in self.keyVals: 
            oldKeyNode = self.keyVals[key]
            val = oldKeyNode.val
            self._remove(oldKeyNode) 
            self.put(key, val)

            return val

        
        return -1



    def put(self, key: int, value: int) -> None:
        if key in self.keyVals: 
            self._remove(self.keyVals[key])

        if self.capacity == 0: 
            lruNode = self.ghostHead.next 
            self._remove(lruNode) 
        
        newNode = CacheNode(key, value) 

        self.ghostTail.prev.next = newNode
        newNode.prev = self.ghostTail.prev 
        newNode.next = self.ghostTail 
        self.ghostTail.prev = newNode

        self.keyVals[key] = newNode 
        self.capacity -=1 
    
    def _remove(self, node): 
        if node.key in self.keyVals: 
            node.prev.next = node.next
            node.next.prev = node.prev 

            self.capacity +=1 
            del self.keyVals[node.key]
    








