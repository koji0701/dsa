class TrieNode: 
    def __init__(self): 
        self.children = {} #letter : TrieNode
        self.endOfWord = False

class Trie:
    def __init__(self): 
        self.root = TrieNode()

    def fillWords(self, wordList: List[str]): 
        print(wordList)
        for word in wordList: 
            cur = self.root
            for l in word: 
                if l not in cur.children: 
                    cur.children[l] = TrieNode()
                cur = cur.children[l] 

            cur.endOfWord = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie() 
        trie.fillWords(words) 

        rv = []

        directions = (
            (1, 0),
            (0, 1), 
            (-1,0),
            (0,-1)
        )

        def dfs(r: int, c: int, cur: TrieNode, built: str): 
            
            if cur.endOfWord: 
                nonlocal rv 
                rv.append(built)
                cur.endOfWord = False
            
            curLetter = board[r][c]
            board[r][c] = "*"

            for dr, dc in directions: 
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= len(board) or nc < 0 or nc >= len(board[0]): 
                    continue 
                nextLetter = board[nr][nc]
                if nextLetter in cur.children:
                    dfs(nr, nc, cur.children[nextLetter], built+nextLetter)
            
            board[r][c] = curLetter

        
        for i in range(len(board)): 
            for j in range(len(board[0])): 
                startChar= board[i][j]
                if startChar in trie.root.children: 
                    dfs(i, j, trie.root.children[startChar], startChar)
        
        return rv


        
