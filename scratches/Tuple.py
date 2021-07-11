'''
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()

'''

t =("张越",38,True,'Seattle')

print(t)

print(t[0])
print(t[3])

a = len(t)
print(a)
print(len(t))

for number in t:
    print(number,end='asdasd\n')

try:
    t[0] = 'city'
    print(t)
except TypeError as err:
    print(err)

person = list(t)

print(person)

person[0] = 'Bruce Lee'
print(person)