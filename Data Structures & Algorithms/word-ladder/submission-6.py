'''
DAWG - directed acyclic word graph 

- bfs through the dawg
- its a valid switch if theres only one fork throughout the traversal 
- record the fork, if you reach the end + its valid, 
    there should only be 1 fork
- check both words w/ both forks switched out for letters. 
- queue any of the new words that match a word in WordList 
    - queue should be tupled with # of transformations 

- construction O(n) 
- traversal idk how to calculate big O


heur note: 
- only len=beginWord words in wordList should be in dawg



try this one first
simpler than dawg? same complexity? 
- construct an undirected graph where two words are connected 
    iff they are 1 letter apart
- O(v^2) construction noramlly but can be optimized
    - optimize this, let * = every place in the word
    - hash with * in the word, and match them up
- O(v+e) traversal (bfs dikjstras etc)


TOPOLOGICAL SORT 

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
        

        #step 3 do a mp traversal for min path from beginWord -> end

        #ucs 

        heap = [] #(cnt, word, seen set)
        heapq.heapify(heap) 

        heapq.heappush(heap, (1, beginWord, set()))
        minCnt = 9999
        while heap: 
            cnt, word, seen = heapq.heappop(heap)
            if word == endWord: 
                minCnt = min(minCnt, cnt)
                continue
            if cnt > minCnt:
                continue
            seen.add(word)
            for nei in mp[word]: 
                if nei in seen: 
                    continue
                heapq.heappush(heap, (cnt+1, nei, seen))
        
        if minCnt < 9999: 
            return minCnt
        return 0




