'''
approach: 

1. create a bidirectional adj map of words, where neighbors are where letters 
off by 1 letter 

    a. runtime trick: hash words like "cat" -> "*at" and "c*t" etc

2. UCS search through the adj map
    try: just use a bfs? and keep track of minCnt
    yeah this would work i go through all nodes regardless


'''

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        #heuristics 
        if len(beginWord) != len(endWord): 
            return 0 

        wordList = set(wordList)
        if endWord not in wordList: 
            return 0 
        
        starredMp = defaultdict(set) # {"*at" : set(bat, cat, ...) }
        mp = defaultdict(set) #{"cat" : set(bat, rat, ...)}
        wordToStarsCache = defaultdict(list)
        #build mp using the starredMp
        #just continuously do set unions from stared 
        #versions of words to build the mp set 

        wordList.add(beginWord)
        #step 1 build starredMp (hash beginWord too)
        for word in wordList: 
            if len(word) != len(endWord): 
                continue
            for i in range(len(word)): 
                nw = word[0:i] + "*" + word[i+1:]
                wordToStarsCache[word].append(nw)
                starredMp[nw].add(word)
        

        #step 2 build mp from starredMp 
        for word in wordList: 
            if len(word) != len(endWord): 
                continue
            for star in wordToStarsCache[word]:
                mp[word] = mp[word] | starredMp[star]
        

        #3. bfs map traversal. global count variable that keeps track of rank
        #all edges=1. thus natural sort for first one to get to endWord
        #global seen too 

        seen = set([beginWord])
        count = 1 

        queue = deque() 
        queue.append(beginWord) 

        while queue: 
            for _ in range(len(queue)): #bfs, so that you process by level 
                
                word = queue.popleft()
                seen.add(word) 

                for nei in mp[word]: 
                    if nei == endWord: 
                        return count + 1 #-1 rank optimization
                    if nei not in seen: 
                        queue.append(nei) 
                
            count += 1
        
        return 0




