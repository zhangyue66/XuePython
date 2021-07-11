"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""
'''
import re

def main():
    username = input("Please create your username now: " )
    u_is_valid = False
    if re.match("^\w{6,20}$",username):
        password = input("Create your password now : ")
        if re.match("^[1-9]",password) and len(password)>4 and len(password)<12:
            print("Pass is good!")
        else:
            print("not good password!")


    else:
        print("Not valide user name")



if __name__ == "__main__":
    main()
'''

import re

def main():
    sentence = '''
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    '''
    pattern = re.compile(r"(?<=\D)1[34578]\d{9}(?=\D)")
    number_list = re.findall(pattern,sentence)

    print("the telephone number is " + str(number_list))

if __name__ == '__main__':
    main()