class TrieNode:
    def __init__(self):
        self.children = 26*[None]
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
        cur = self.root
        for letter in word:
            index = ord(letter)-ord("a")
            if cur.children[index] is None:
                cur.children[index] = TrieNode()

            cur = cur.children[index]
        cur.isWord = True
        #print(self.root.children)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root

        for letter in word:
            index = ord(letter)-ord("a")
            if cur.children[index] != letter:
                return False

            cur = cur.children[index]

        return cur is not None and cur.isWord == True


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root

        for letter in prefix:
            index = ord(letter)-ord("a")
            if cur.children[index] != letter:
                return False

            cur = cur.children[index]

        if cur is not None:
            return True
        else:
            return False




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)