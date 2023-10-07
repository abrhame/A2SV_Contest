class TrieNode:
    def __init__(self):
        self.children = [0] * 26
        self.is_word = False
        self.count = 0
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not curr.children[idx]:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]  
        curr.is_word = True
        curr.count += 1    


    def search(self, word: str) -> bool:
        stack = [(self.root,0)]
        while stack:
            cfurr,idx = stack.pop()
            if idx == len(word):
                if curr.is_word:
                    return True
            elif word[idx] in curr.children: 
                stack.append((curr.children[word[idx]], idx+1))
        return False

    def findidx(self,word,start,curascii):
        for i in range(start, len(word)):
            if ord(word[i]) - ord('a') == curascii:
                return i
        return -1

    def dfshelper(self,node,word,start):
        for i in range(26):
            if node.children[i]:
                child = node.children[i]
                index = self.findidx(word,start,i)
                if index != -1:
                    if child.is_word:
                        self.count += child.count
                    self.dfshelper(child,word,index + 1)



    def dfs(self,word):
        self.count = 0
        self.dfshelper(self.root,word,0)
        return self.count

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = WordDictionary()
        count = 0
        for word in words:
            trie.addWord(word)

        return trie.dfs(s)