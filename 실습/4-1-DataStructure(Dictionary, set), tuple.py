tuple_1_to_100 = tuple(range(1, 100+1))
print(tuple_1_to_100)

list_1_to_100 = list(tuple_1_to_100)
print(list_1_to_100)

###

#  Tuple
my_info = [('이름', 'NaN'), ('email', 'abc@bbc.co.uk'), ('phone', '000-000-0000'), ('nationality', 'S.Korea')]

for el in my_info:
	print(el[0], end=" : ")
	print(el[1])

###

# Dictionary
# 간단: 딕셔너리 만들기
NaN = {
	'name': 'Cinji',	
	'age': '80',
	'phone': '080-0000-0000',
}
NaN['email'] = 'javascript@python.org'
print(NaN.get('name'))
print(NaN.get('age'))
print(NaN.get('phone'))
print(NaN.get('email'))
print(NaN['name'])
print(NaN['age'])
print(NaN['phone'])
print(NaN['email'])

for el in NaN:
	print(el)

###

# 조금 힘들껄요: 튜플을 딕셔너리로 바꾸기
my_info = [
	('nickname', 'cocolman'),
	('country', 'korea'),
	('name', 'sol')
]

dic = {}
for i in range(0, len(my_info)):
	dic[my_info[i][0]] = my_info[i][1]
print(dic)

dic = {}
for el in my_info:
	dic[el[0]] = el[1]
print(dic)

print(dict(my_info))