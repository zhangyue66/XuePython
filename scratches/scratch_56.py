string = "abcddddefghizdd" #i

target_string = "ddd"   #j

i=0

while i<(len(string)):
    if string[i] != target_string[0]:
        i += 1
        continue
    else:
        anchor = i
        is_found = True
        for j in range(len(target_string)):
            if string[anchor] != target_string[j]:
                is_found = False
                break
            else:
                anchor += 1
        if is_found:
            print(i)
            break

    i += 1




















