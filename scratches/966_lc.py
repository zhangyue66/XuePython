class Solution:
    def spellchecker(self, wordlist, queries):
        vowels = ['a', 'e', 'i', 'o', 'u','A', 'E', 'I', 'O', 'U']
        ans = []
        caseHash = {}
        vowelHash = {}
        sequenceHash = {}
        first_all_vowel = ""

        for word in wordlist:
            temp = word.lower()
            caseHash[temp] = word

            if temp not in sequenceHash:
                sequenceHash[temp] = word

        for word in wordlist:
            nonvowel = ""
            for i in range(len(word)):
                if word[i] not in vowels:
                    nonvowel += (word[i].lower()+str(i))
            if nonvowel == "" and first_all_vowel == "":
                first_all_vowel = word
            else:
                vowelHash[nonvowel] = word


        for query in queries:
            if query in wordlist:
                ans.append(query)
            else:
                if query.lower() in caseHash:
                    if query.lower() in sequenceHash:
                        ans.append(sequenceHash[query.lower()])
                    else:
                        ans.append(caseHash[query.lower()])
                else:
                    check = ""
                    for i in range(len(query)):
                        if query[i] not in vowels:
                            check += (query[i].lower()+str(i))

                    if check == "": # all vowels
                        ans.append(first_all_vowel)
                    else:
                        if check in vowelHash:
                            yz = vowelHash[check]

                            if yz in sequenceHash:
                                ans.append(sequenceHash[yz])
                            else:
                                ans.append(yz)

                        else:
                            ans.append("")

        return ans

# expected ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
# now2    ['kite', 'kite', 'KiTe', 'Hare', 'Hare', '', '', 'kite', '', 'kite']


# now      ['kite', 'kite', 'KiTe', 'Hare', 'Hare', 'Hare', 'Hare', 'kite', 'kite', 'kite']
# case: ["ae","aa"]
# ["UU"]

yz = Solution()
wordlist = ["KiTe","kite","hare","Hare"]
queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
print(yz.spellchecker(wordlist,queries))