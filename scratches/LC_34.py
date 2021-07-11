class Leet34Code(object):

    def binary_search(self,num,target):
        start, end = 0, len(num) - 1
        while start <= end:
            mid = (start + end) // 2
            if target > num[mid]:
                start = mid + 1
            elif target < num[mid]:
                end = mid - 1
            else:
                return mid
        return [-1,-1]

    #def print(self,target):


def main():
    sorting = Leet34Code()
    print(sorting.binary_search([5,7,7,8,8,10],8))
    print("sorting is done!")



if __name__ == "__main__":
    main()