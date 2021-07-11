#Exercise 1 - rolling text "Seattle Like Yue Zhang"
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    try:
        while True:
                # 清理屏幕上的输出
                os.system('cls')  # os.system('clear')
                print(content)
                # 休眠200毫秒
                time.sleep(0.2)
                content = content[1:] + content[0]
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()


# content = "京欢迎你为你开天辟地…………' +'北"
#-> content = 欢迎你为你开天辟地…………北 + 京



# Exercis2 设计一个函数产生指定长度的验证码，验证码由大小写字母和数字构成

#password(length)


import random
import string


def passwrod(length=input("Enter length of your password!")):
    if length.isdigit() == False:
        print("not number!")
    else:
        ge_pass = ''
        for number in range(int(length)):
            #ge_pass += random.choice("ABCDEFabcdef123456")
            ge_pass += random.choice(string.ascii_lowercase+string.ascii_uppercase+string.digits)
        print(str(ge_pass))

if __name__ == "__main__":
    passwrod()


#Exercise3 设计一个函数返回给定文件名的后缀名。
#For example, user will input a file name as "snis007.avi" ,after function, you will be presented the ".avi is what your are looking for"

# return_suffix()


def return_suffix(file_name = input("Please enter a file name with dot : ")):
    while "." in file_name:
        print("we find it!")
        position = file_name.find('.')
        file_name = file_name[position:]
        print(file_name)
        break

    return file_name


if __name__ == '__main__':
    return_suffix()

'''
def get_suffix(filename, has_dot=False):
    """
    获取文件名的后缀名

    :param filename: 文件名
    :param has_dot: 返回的后缀名是否需要带点
    :return: 文件的后缀名
    """
    pos = filename.rfind('.')
    if 0 < pos < len(filename) - 1:
        index = pos if has_dot else pos + 1
        return filename[index:]
    else:
        return ''





print(get_suffix("ssni007.avi",has_dot=True))

'''

# Exercise 4








