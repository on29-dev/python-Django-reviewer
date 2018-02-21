def plus_1(x):
    return x + 1

def plus_exclamation(x):
    return x + '!'

def input_num():
    num = int(input("1~9 중 하나의 정수를 입력하세요."))
    if num not in range(1, 9+1):
        print("잘못된 입력입니다.")
    else:
        return num

def multi_2(num):
    return num * 2

def plus_5(num):
    return num + 5

def multi_50(num):
    return num * 50

def plus_1769(num):
    return num + 1769

def sub_birth(num):
    return num - 1950

def i_dont_know():
    return sub_birth(plus_1769(multi_50(plus_5(multi_2(input_num())))))

print(i_dont_know())


###

def range_list(start, end=None, step=None):
    if not end:
    # end가 없다면 false라면
        return list(range(start))
    elif not step:
        return list(range(start, end))
    return list(range(start, end, step))

