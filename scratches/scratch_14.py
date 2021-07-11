s1 = 'hello, world!'
s2 = "hello, world!"
# 以三个双引号或单引号开头的字符串可以折行
s3 = """
hello,
world!
"""
print(s1, s2, s3, end='')


s1 = '\'hello, world!\''
s2 = '\n\\hello, world!\\\n'
print(s1, s2, end='')

s1 = '\141\142\143\x61\x62\x63'
s2 = '\u9a86\u660a'
print(s1, s2)

s1 = r'\'hello, world!\''
s2 = r'\n\\hello, world!\\\n'
print(s1, s2, end='\n')

a, b = 5, 10
print('the calculation is like :{0}*{1} = {2}'.format(a, b, a * b))




t = ('骆昊', 38, True, '四川成都')
print(t)

for member in t:
    try:
        print(member)
        member.isnumeric()

    except:
        print("error")

t = ('王大锤', 20, True, '云南昆明')
print(t)

person = list(t)
print(person)



#Yield function usage


