class Solution:
    def findLUSlength(self, a: str, b: str):
        if a == b:
            return -1
        elif len(a) == len(b):
            return len(a)
        else:
            return max(len(a),len(b))