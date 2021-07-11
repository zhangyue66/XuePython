class Solution:
    def getHint(self, secret: str, guess: str):
        if len(secret) == 0 or len(guess) == 0:
            return "0A0B"
        else:
            cnt_A = 0
            cnt_B = 0
            A_yz = []
            B_yz = []


            #validate = True * len(guess)
            for i in range(len(guess)):
                if secret[i] == guess[i]:
                    cnt_A += 1
                else:
                    A_yz.append(secret[i])
                    B_yz.append(guess[i])

            validate = [True] * len(A_yz)
            #print(A_yz)
            #print(B_yz)
            #print(validate)
            k = 0
            while k < len(A_yz):
                for j in range(len(B_yz)):
                    #print(validate)
                    if B_yz[j] in A_yz:
                        ind = A_yz.index(B_yz[j])
                        if validate[ind] != False:

                            cnt_B += 1
                            validate[ind] = False

            return str(cnt_A)+"A"+str(cnt_B)+"B"

secret = "1123"
guess = "0111"


yz = Solution()

print(yz.getHint(secret,guess))