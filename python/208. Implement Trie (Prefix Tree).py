from collections import deque

class TrieNode:
    def __init__(self) -> None:
        self.children=[None]*26
        self.isWord=False
    
class Trie:

    def __init__(self):
        self.trie=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.trie
        for letter in word:
            i=ord(letter)-ord('a')
            if cur.children[i]==None:
                cur.children[i]=TrieNode()
            cur=cur.children[i]
        cur.isWord=True
        
    def search(self, word: str) -> bool:
        cur=self.trie
        for letter in word:
            i=ord(letter)-ord('a')
            if cur.children[i]==None:
                return False
            cur=cur.children[i]
        return cur.isWord

    def startsWith(self, prefix: str) -> bool:
        cur=self.trie
        for letter in prefix:
            i=ord(letter)-ord('a')
            if cur.children[i]==None:
                return False
            cur=cur.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)