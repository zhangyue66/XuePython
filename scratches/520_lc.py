class Solution:
    def detectCapitalUse(self, word: str):
        if word.islower() == True:
            return True
        elif word.isupper():
            return True
        elif word[0].isupper() and word[1:].islower():
            return True

        else:
            return False
