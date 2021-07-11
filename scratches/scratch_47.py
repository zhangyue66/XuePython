def is_bigger(src, dest, seperator):
    src_list = src.split(seperator)
    dest_list = dest.split(seperator)
    length = max(len(src_list), len(dest_list))

    for i in range(0, length):
        try:
            if int(src_list[i]) > int(dest_list[i]):
                return True
            elif int(src_list[i]) == int(dest_list[i]):
                continue
            else:
                return False
        except Exception as e:
            if len(src_list) > len(dest_list):
                return True
            else:
                return False
    return False
