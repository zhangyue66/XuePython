set1 = {1,2,3,3,3,2}

print(set1)
print("Length is %d !" %(len(set1)))



set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))


set2 = set(range(1,10))
set3 = set((1,2,3,3,2,1))

print(set2,set3)


set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

set1.add(4)
set1.add(5)
set2.update([11,12])


set2.update((13,14))



set2.discard(5)

if 4 in set2:
    set2.remove(4)

#what is difference between discard and remove
#remove will throw error if element is not existing. Discard will not!!

print(set1,set2)

#randomly removing 
#print(set3.pop())

print(set3)

print(set1 & set2)
print(set1 | set2)
print(set1.intersection(set2))
print(set1.union(set2))
print(set1 - set2)
print(set1.difference(set2))
print(set1 ^ set2)
print(set1.symmetric_difference(set2))
if set1.symmetric_difference(set2) == set2.symmetric_difference(set1):
    print("Yue is handsome")