# csv를 Dictionary로 만들기 예제

csv_values = """
이름, 연락처, 나이
철수, 010-1234-5678, chulsu@gmail.com
영희, 010-432-2345, 0hie@gmail.com
"""

csv_values = csv_values.strip('\n')
csv_list = csv_values.split('\n')

keys = []

for el in csv_list[0].split(','):
    keys.append(el.strip(' '))

# print(keys)

results = []
for val in csv_list[1:]:
    result_dict = {}
    i = 0
    for el in val.split(','):
        result_dict[keys[i]] = el.strip(' ')
        i += 1
    results.append(result_dict)

# print(results)


# set 연산
set1 = set()
set2 = set()
set3 = set()
for i in range(1, 100+1):
    if i % 15 == 0:
        set3.add(i)
    if i % 5 == 0:
        set2.add(i)
    if i % 3 == 0:
        set1.add(i)
# print(set1.union(set2))
# print(set3.difference(set1))


# List Comprehension 
# 1) 1~100까지 숫자 중 3의 배수인 숫자만 가진 리스트 만들기
multi_3 = [ i for i in range(1, 100+1) if i % 3 == 0]
print(multi_3)
# print([ i for i in range(1, 100+1) if i % 3 == 0])

# 2) [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
double_for = [ [i for i in range(1, 3+1)] for j in range(3)]
print(double_for)
# print([ [i for i in range(1, 3+1)] for j in range(3)])