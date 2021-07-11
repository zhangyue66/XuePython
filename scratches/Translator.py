# Build a translator Giraffe language vowels -> g
# A E I O U Y -> Vowels

def translate(phrase):
    translation = ""
    vowel_list = ["a","e","i","o","u"]
    cap_vowel_list = ["A","E","I","O","U"]
    for letter in phrase:
        if letter in vowel_list:
            translation = translation + "g"
        elif letter in cap_vowel_list:
            translation = translation + "G"
        else:
            translation = translation + letter
    print(translation)
    return translation
translate("cat")
translate("appleiloveyou")
translate("AEgghj")