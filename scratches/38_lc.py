class Solution:
     def countAndSay(self,n):
    #     seq = "1"
    #     for i in range(n-1):
    #         seq = self.getNext(seq)
    #     return seq
    #
    #
    # def getNext(self,seq):
    #     answer = ""
    #     i = 0
    #     while i < len(seq):
    #         count = 1
    #         while i < len(seq)-1 and seq[i] == seq[i+1] :
    #             count += 1
    #             i += 1
    #         answer += str(count)+seq[i]
    #         i += 1
    #
    #     return answer

        if n <= 1:
            return '1'

        pre_seq = self.countAndSay(n - 1)
        count = 1
        answer = ''

        for i in range(len(pre_seq)):
            if i < len(pre_seq)-1 and pre_seq[i] == pre_seq[i+1] :
                count += 1
            elif i < len(pre_seq)-1 and pre_seq[i] != pre_seq[i+1]:
                answer += str(count)+pre_seq[i]
                count = 1
            elif i == len(pre_seq)-1:
                answer += str(count)+pre_seq[i]





        return answer








yz = Solution()

n = 4

print(yz.countAndSay(n))

for i in range(0):
    print(str(2)+"13")