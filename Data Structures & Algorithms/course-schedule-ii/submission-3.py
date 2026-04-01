'''
topo sort - kahn's 

adj map + indegrees 

caveat: need to make sure its acyclic 

'''

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #topo sort 
        mp = {i: [] for i in range(numCourses)} #prereq : postreq
        indegree = {i: 0 for i in range(numCourses)} #how many preqreqs smth has

        for post, pre in prerequisites: 
            mp[pre].append(post)
            indegree[post] += 1
        print(mp)
        queue = deque()
        print(indegree)
        for post, indeg in indegree.items(): 
            if indeg == 0: 
                queue.append(post)
        print(queue)
        ordering = []
        while queue: 
            cur = queue.popleft() 
            print(cur)
            
            ordering.append(cur) 
            for postreq in mp[cur]: 
                indegree[postreq] -= 1
                if indegree[postreq] == 0:
                    queue.append(postreq)
                
    
        print(ordering) 

        if len(ordering) != numCourses: 
            return []


        return ordering









            
