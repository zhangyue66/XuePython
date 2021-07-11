nums = [1,3,7,17]
target = 8

# give any target number and find whether in list , it is sum of any two non-duplicated element
#if yes, return the position of the two elements in the list
#example 8 = 1+7
#return[0,2]
indexes = []
for index in range(len(nums)):
    indexes.append(index)

print(indexes)

dic_iter = zip(indexes,nums)

# dic = dic(dic)
# print(type(dic))


# for index,number in dic_iter :
#     #print("%d index %d value " %(index,number))
#     #target =8
#     dic_yz = dict(index,number)

dic = dict(dic_iter)

#print(dic)

#print(dic[2])

k = 0

target =8

while k <= len(nums)-1:
    j = k+1
    while j <= len(nums)-1:
        if dic[k]+dic[j] != target:
            j += 1
        else:
            print("find it! position is [%d , %d] " %(k,j))
            break
        #break
    k +=1
    print("test")















