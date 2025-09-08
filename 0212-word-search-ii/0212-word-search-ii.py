# initalize class for trinode for the nodes of trie
class TrieNode:
    def __init__(self):
        #the children nodes of the trienode to a hashmap
        self.children = {}
        #word as false, this will later help us check in Trie class whether words exist or not
        self.word = False 
    #another fn that takes (Self + word) as para 
    def addWord(self, word):
        #pointer 
        cur = self
        #iterate thru every char in word for c 
        for c in word:
            if c not in cur.children:
                #add charc to trie using TrieNode() class 
                cur.children[c] = TrieNode()
            cur = cur.children[c]
                #update the cur.word as the word exist 
        cur.word = True

        



class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        # w in words ?
        for w in words:
            # using root (add words)

            root.addWord(w)
        rows = len(board)
        cols = len(board[0])

        res, visit = set(), set()

        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visit or board[r][c] not in node.children):
               return 

            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]

            if node.word:
                #add word to res 
                res.add(word)

            dfs(r + 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c - 1, node, word)

            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root, "")

        return list(res)


        