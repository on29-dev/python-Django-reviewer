Family = [{
    'age': '2',
    'birth': '2/20',
    'contact': '019-999-9999'
}, {
    'age': '5',
    'birth': '2/21',
    'contact': 'None'
}, {
    'age': '5',
    'birth': '2/22',
    'contact': '010-222-2222'
}, {
    'age': '2',
    'birth': '2/23',
    'contact': '080-1234-3453'
}]

_result = ''
for j in Family[0].items():
    _result = _result + j[0] + ', '
for i in range(0, len(Family)):
    for _tuple in Family[i].items():
        _result = _result + _tuple[1] + ', '
result = _result.strip(', ')
print(result)
# age, birth, contact, 2, 2/20, 019-999-9999, 5, 2/21, None, 5, 2/22, 010-222-2222, 2, 2/23, 080-1234-3453


###

pep20 = """
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

num_alpha = {}
_pep20_filtered = ""
_set = set()
for k in pep20:
    if k.isalpha():
        _pep20_filtered += k
for i in list(_pep20_filtered):
    if not i in _set:
        num_alpha[i] = 1
    else:
        num_alpha[i] += 1
    for j in num_alpha:
        _set.add(j)
print(num_alpha)
# {'B': 1, 'e': 86, 'a': 50, 'u': 20, 't': 74, 'i': 49, 'f': 10, 'l': 33, 's': 42, 'b': 19, 'r': 31, 'h': 29, 'n': 38, 'g': 11, 'y': 15, 'E': 2, 'x': 6, 'p': 20, 'c': 16, 'm': 15, 'S': 3, 'o': 41, 'C': 1, 'd': 16, 'F': 1, 'R': 1,'k': 2, 'A': 3, 'v': 5, 'U': 1, 'I': 3, 'T': 1, 'w': 4, 'D': 1, 'N': 2}
# for문이 2번 나오고 _pep20_filtered로 따로 만드는 등 다소 복잡한데 더 좋은 방법이 있는지 궁금합니다.
# 검토결과: count()를 써보세요
# 오?!

# count()를 써봤다.
num_alpha_count = {}
_pep20_filtered = ""
_set = set()
for k in pep20:
    if k.isalpha():
        _pep20_filtered += k
for j in _pep20_filtered:
    _set.add(j)
for i in _set:
    num_alpha_count[i] = _pep20_filtered.count(i)
print(num_alpha_count)
# {'T': 1, 'I': 3, 'c': 16, 'l': 33, 'b': 19, 'm': 15, 'p': 20, 'n': 38, 't': 74, 'o': 41, 'A': 3, 'u': 20, 'S': 3, 'e': 86, 'r': 31, 'E': 2, 'C': 1, 'f': 10, 'F': 1, 'R': 1, 'k': 2, 'N': 2, 'v': 5, 'B': 1, 'D': 1, 's': 42, 'a': 50, 'i': 49, 'd': 16, 'h': 29, 'y': 15, 'x': 6, 'w': 4, 'g': 11, 'U': 1}

print(bool(num_alpha == num_alpha_count))
# True


###

print([i for i in range(1, 6+1)])
print([6-i for i in range(0, 6)])
print([[i for i in range(1, 3+1)] for x in range(3)])
print([[i for i in range(j, 3+j)] for j in range(1,9,3)])
# [1, 2, 3, 4, 5, 6]
# [6, 5, 4, 3, 2, 1]
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]