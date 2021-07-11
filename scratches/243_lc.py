#Shortest word distance
# given word 1 and word2 return the shortest distance between two words in list




#input word1 = coding  word2 = practice

#output should be 3

#input makes and coding. output should be 1


class Solution:
    def shortestDistance(self,words,word1,word2):
        dic = dict(enumerate(words))
        list_one = []
        list_two = []

        for index,word in dic.items():
            if word == word1:
                list_one.append(index)
        for index,word in dic.items():
            if word == word2:
                list_two.append(index)

        distance = float("inf")
        for i in list_one:
            for j in list_two:
                distance = min(abs(i-j),distance)

        return distance

words = ["practice","makes","perfect","coding","makes"]
word1 = "makes"
word2 = "coding"



yz = Solution()
print(yz.shortestDistance(words,word1,word2))