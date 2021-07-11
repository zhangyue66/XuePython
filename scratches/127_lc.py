from _collections import defaultdict

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList):
        if endWord not in wordList:
            return 0
        else:
            graph = defaultdict(list)
            queue = []
            searched = [False]*(len(graph))
            queue.append()





yz = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
print(yz.ladderLength(beginWord,endWord,wordList))
