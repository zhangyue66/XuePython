class Solution:
    def avoidFlood(self, rains):
        ans = []
        hash = {}
        stack = [] #record previous lake which rains
        last_rain = []

        for rain in rains:
            if rain > 0:#raining this day
                ans.append(-1)
                stack.append(rain)
                if rain not in hash or hash[rain] == 0:
                    hash[rain] = 1
                else:
                    return []
            elif rain == 0: # sunny day . decide to dry a lake
                #enhancement here. first dry lake that will be on rain in future
                if len(stack) != 0:
                    cur = stack.pop() # dry this lake using greedy
                    hash[cur] = 0 # means dry
                    ans.append(cur)
                else:#stack is empty. you can dry any lake
                    ans.append("yz")
        yz = 0
        for i in range(1,10**9):
            if i not in hash:
                yz = i # yz replace "yz" in ans
                break
        new_ans =[yz if x=="yz" else x for x in ans]
        return new_ans

yz = Solution()
rains = [1,2,3,4]
#rains = [1,2,0,0,2,1]
#rains = [1,2,0,1,2]
#rains = [69,0,0,0,69]
#rains = [1,2,0,2,3,0,1]
print(yz.avoidFlood(rains))
