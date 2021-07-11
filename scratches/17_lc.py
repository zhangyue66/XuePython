from itertools import product

class Solution:

    def letterCombinations(self, digits: str) :
        if len(digits) == 0 :
            return []
        else:

            res = []
            digit_map = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

            def backtrack(combination,next_digits):
                if len(next_digits) == 0:
                    res.append(combination)
                else:

                    for letter in digit_map[next_digits[0]]:
                        backtrack(combination+letter,next_digits[1:])

            backtrack("",digits)

            return res



yz = Solution()

digits = "23"

print(yz.letterCombinations(digits))