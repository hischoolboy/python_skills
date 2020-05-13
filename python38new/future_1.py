# 赋值表达式
def new1_1():
    a = [1, 2, 3]
    if (b := len(a)) < 4:
        print('length is less than 2')
        print(f'b= {b}')
    print('-' * 10)
    print(b)


# 仅限位置形参
def f(a, b, /, c, d, *, e, f):
    print('iuu'*10)


def new1_2():
    # f(1, 2, )
    f(1, 2, 4, 5, e=10, f=1)
    # f(1, 2, 3, e=10)


def new1_3():
    a = '阿三'
    b = '阿四'
    print(f'{a=!s}, {b=}')


def new2_1():
    from pprint import pp, pprint
    test_dict = dict(e='a', f='b',a=1, b=2, c=3,)
    print('pp print is {}'.format(pp(test_dict)))
    print('pprint result is {}'.format(pprint(test_dict)))


if __name__ == '__main__':
    # new1_1()
    # new1_2()
    new1_3()
    new2_1()



