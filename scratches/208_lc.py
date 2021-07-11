class TrieNode:
    def __init__(self):
        self.children = 26 * [None]

        self.isWord = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        p = self.root

        for c in word:
            index = ord(c)-ord("a")
            if p.children[index] is None:
                p.children[index] = TrieNode()
            p = p.children[index]
        p.isWord = True




    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.find(word)
        return node is not None and node.isWord == True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        return self.find(prefix) is not None

    def find(self,prefix):

        p = self.root
        for c in prefix:
            index = ord(c)-ord("a")
            if not p.children[index]:
                return None
            p = p.children[index]

        return p


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)     """