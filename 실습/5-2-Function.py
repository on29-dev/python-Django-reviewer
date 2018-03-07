def test(a, b, c):
	print('a는 : ', a)
	print('b는 : ', b)
	print('c는 : ', c)

test(b=1, c=2, a=3)

# packing & unpacking
def sum_all(*args):
	return sum(args)

print(sum_all(1, 2, 3, 4, 5)) 

def print_f_name(father, mother, sister, brother):
	print('아버지 이름은 ', father)
	print('어머니 이름은 ', mother)
	print('언니 이름은 ', sister)
	print('남동생 이름은 ', brother)

# print_f_name(father="임꺽정", mother="임사랑", sister="하니", brother="둘리", cat="나비")
# TypeError: print_f_name() got an unexpected keyword argument 'cat'

def print_f_name2(**kwargs):
	for key in kwargs:
		print(key, '의 이름은 ', kwargs[key])

print_f_name2(father="임꺽정", mother="임사랑", sister="하니", brother="둘리", cat="나비")

###
likes = []
def what_like():
	like = input("무엇을 좋아하나요?")
	likes.append(like)
	print(likes)

what_like()


###

def add_n(a, n):
	if n == 0:
		return a
	return 1 + add_n(a, n-1)

print(add_n(10, 7))


###
try:
	num = input('숫자를 입력하세요.')
	num = int(num)
# except ValueError:
# 에러의 종류에 따라 에러처리를 다르게 할 수 있음
except:
	print("숫자를 숫자키로 입력하세요. 한글 말고 영어말고")

# TypeError, NameError, ZeroDivisionError 등등...