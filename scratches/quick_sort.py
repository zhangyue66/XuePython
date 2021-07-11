
def quicksort(array):
    less =[]
    equal=[]
    greater = []

    if len(array) >= 0 and len(array) <2:
        return array
    else:

        #print (array)
        pivot = array[0]
        #print (pivot)

        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else :
                greater.append(x)
        return quicksort(less)+equal+quicksort(greater)


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print (quicksort(test))