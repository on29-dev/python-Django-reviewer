# python-Django-reviewer
[Python & Django 웹프로그래밍 BOOT CAMP](https://fastcampus.teachable.com/courses/enrolled/277684) 리뷰
---
## 1일차: 파이썬의 실행
### 1. 프로그래밍
* 프로그래밍 = 컴퓨터에서 실행되는 특정 작업을 수행하는 명령 모음을 만드는 행위
* 컴퓨터 사고력(Computational Thinking)을 키우는 것에 프로그래밍이 도움이 된다.
### 2. 컴퓨터 사고력(Computational Thinking)
* 문제를 해결하기 위해 방법을 찾는 힘
### 3. 인터프리터와 컴파일러
#### 인터프리터 언어
* 인간에 더 가까운 언어
* 인터프리터는 우리가 쓴 코드를 실시간으로 컴퓨터에게 기계어로 전달한다.
* 컴퓨터와의 즉각적인 소통에 유리
* 많은 양의 정보를 전달하기에는 느리다.
* 동시통역사 느낌
#### 컴파일러 언어
* 컴퓨터에 더 가까운 언어
* 우리가 쓴 코드를 컴파일링이라는 과정을 통해 컴퓨터에 전달한다.
* 많은 양의 정보를 전달하기에 빠르다.
* 번역서 느낌
---
## 2일차(1-2): Type과 연산(Numbers, String, Boolean), 데이터 구조(List)
### 1. 변수에 대한 이해
* 변수의 목적
  * 불필요한 중복과 반복적인 작업을 제거
* 파이썬 REPL 환경에서는 변수`_`가 기본적으로 최신 연산 값을 갖고 있음(인위적으로 _에 값을 할당해주면 이 기능이 작동하지 않음)
### 2. 연산자
* `a // b` (a를 b로 나눈 몫)
* `a ** b` (a를 b제곱한 값)
* 제곱을 함수로 구현할 수 있음
```python
pow(a, b)
a ** b 
```
### 3. Number
Int와 Float은 상호 연산 가능
#### (1) Int
* 일반적인 정수
#### (2) Float
* 소수(0.1 등)을 포함한 실수
### 4. String
#### (1) print() 함수
  * REPL 환경이 아닌 상황에서 값을 출력하려면 써 줘야 하며, javascript의 console.log()와 비슷한 기능
  * print(출력하고자 하는 값[, end="출력값 끝에 붙이고 싶은 값"])
#### (2) input() 함수
  * 사용자로부터 값을 받아오기 위해 사용
  * 타입은 String
#### (3) String format
  ```python
  "안녕하세요 %s씨, %d년 새해 복 많이 받으세요"%("Obama", 2018)
  "안녕하세요 {name}씨, 오늘은 {day}입니다.".format(
    name = "Obama",
    day = "목요일"
  )
  ```
#### (4) Number와 덧셈 연산시 TypeError 발생
#### (5) 자바스크립트와 같이 String끼리 덧셈 연산을 할 경우 문장을 이어붙임
  ```python
  print('Py' + 'thon')
  # Python
  ```
#### (6) 특징
  * 순서가 있는 자료형
    * indexing이 되어 있어서 순서대로 값을 찾을 수 있음
    * `len()`과 `슬라이싱` 사용 가능
  ```python
  # 슬라이싱 사례
  string = 'Python'
  print(string[1]) # 'y'
  print(string[-1]) # 'n' (맨 마지막 글자 출력)
  print(string[0:3]) # 'Pyt' (0이상 3미만까지(0,1,2) 출력)
  print(string[0:-1]) # 'Pytho' (0이상 맨 마지막 글자 미만 출력)
  print(string[:]) # 'Python' (전체 출력)
  print(string[0:7:2]) # 'Pto' (0이상 3미만 중 2스텝씩 건너뛰어 출력)
  print(string[::2]) # 'Pto' (String 중 짝수번째 글자만 출력)
  ```
  * Immutable(수정불가)
    * Mutable(수정가능)의 반댓말
    * 문자열 중간의 일부를 변경할 수 없다.(List는 변경가능하나 String은 불가)
  ```python
  p = 'Python'
  p[0] = "J" # TypeError: 'str' object does not support item assignment (JavaScript의 경우 에러를 출력시키지 않지만 마찬가지로 변경되지도 않는다.) 
  ```

#### 빌트인 함수(built-in function)
  ```python
  len()
  len('hi') # 2
  ```
### 5. Boolean
#### (1) 참/거짓을 확인
  * `bool(인자)'
    * 인자의 참/거짓을 확인해줌
  * True(참)의 친구들
    * 
  * False(거짓)의 친구들
    * `[]` 빈 리스트
    * `''` 빈 문자열
    * `0` 숫자 0
    * `None` NoneFalse 친구들 
  ```python
  1 in [1, 2, 3] # True
  'j' not in 'jupyter notebook' # False
  ```
#### (2) `and` 와 `or`
  * and
    * 좌항과 우항이 모두 참일 경우 True
    * 나머지 모든 경우는 False
  * or
    * 좌항과 우항이 모두 거짓일 경우 False
    * 나머지 모든 경우는 True

### 6. List
#### (1) 특징
  * Mutable
    * String과 다르게 수정 가능하여 목록의 일부를 수정할 수 있다.
  * `append()`, `del`, `reverse()`, `sort()`, `pop()`, `insert()`, `extend()`, `count()`, `remove()`
    * 원하는 값을 리스트형태로 뽑아내려면 `슬라이싱`을 사용해야 한다.
    * 위 메소드와 키워드는 모두 원본 리스트를 변경한다.
  * `+` 덧셈 연산과 `extend()`
    * 리스트가 합쳐지지만 원본 리스트를 변경하지 않는다. 원본 리스트를 변경하고자 하면 `extend()` 메소드를 사용해야 한다. 
    * 성능 면에서 `extend()`가 우수하다고 한다.
  ```python
  # append()
  likes = []
  
  likes.append('hi')
  likes.append(9)
  likes.append(2.5)
  print(likes) # ['hi', 9, 2.5]
  
  # del
  del likes[0]
  print(likes) # [9, 2.5]

  # reverse()
  likes.reverse()
  print(likes) #[2.5, 9]

  # pop()
  # del과 pop()의 차이점은 
  # 1. 차수를 입력하는 del과 값을 입력하는 pop()이라는 점과 
  # 2. 결과값을 반환하지 않는 del과 뽑아낸 값을 반환해주는 pop()이라는 점
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  del numbers[0]
  number.pop(4)
  
  # insert(넣고자 하는 위치의 차수, 넣고자 하는 값)
  numbers = [1, 2, 3, 4, 6]
  numbers.insert(0, 0)
  print(numbers) # [0, 1, 2, 3, 4, 6]
  numbers.insert(-1, 5)
  print(numbers) # [0, 1, 2, 3, 4, 5, 6]
  
  # 덧셈연산과 extend()
  print([1, 2, 3] + [4, 5, 6]) # [1, 2, 3, 4, 5, 6]
  numbers = [1, 2, 3]
  numbers2 = [4, 5, 6]
  numbers + numbers2
  print(numbers) # [1, 2, 3] 원본 배열이 변경되지 않았다.
  numbers.extend(numbers2)
  print(numbers) # [1, 2, 3, 4, 5, 6] 원본 배열이 변경되었다.
  print(numbers2) # [4, 5, 6] 인자로 쓰인 배열은 그대로 남아있다.
  ```
#### (2) 리스트 복사
  * Python의 모든 값은 객체
    * 모든 값이 call by reference(기본자료형이 call by value인 JavaScript와 다른 점)
    * 참고 문서 (https://item4.github.io/2015-07-18/Some-Ambiguousness-in-Python-Tutorial-Call-by-What/)
    * 의도치 않은 결과를 방지하기 위해 `copy()`를 사용
  * 원본 값이 변경되는 것은 자료형이 객체형인지 아닌지가 아니라 `mutable`/`immutable`의 속성에 의해 결정된다.
  ```python
  a = [1, 2, 3]
  b = a
  b.append(4)
  print(b) # [1, 2, 3, 4]
  print(a) # [1, 2, 3, 4] # 의도치 않게 a까지 변경됨(a와 b는 모두 같은 곳을 참조하기 때문)

  # copy() 사용
  a = [1, 2, 3]
  b = a.copy
  b.append(4)
  print(a) # [1, 2, 3]
  print(b) # [1, 2, 3, 4] # a는 변경되지 않았다.
  ```

### 7. 타입 변환
```python
int() # 값을 Int로 변환
float() # 값을 Float으로 변환
str() # 값을 String으로 변환
```
---
## 3일차(1): 흐름 제어(If, for, while)
### 1. If
#### (1) 기본문법
```python
# python에서는 indent(tab)이 중요하다.
# colon(:)을 빼먹지 말 것.
if bool:
  # bool이 참이면 실행되는 부분
  print("bool is True!")
elif bool:
  # if의 bool이 거짓이고 elif의 bool이 참이면 실행되는 부분
  print("bool is True!!")
else:
  # 모든 bool이 거짓인 경우 실행되는 부분
  print("bools are all False")
```
#### (2) `random 모듈`과 `abs`
  * `random 모듈`
    * 빌트인(built-in, 내장)
    * `import random`을 통해 호출하여 사용
  ```python
  import random
  n = random.randint(1, 10)
  print(n) #`1~10 중 랜덤한 정수값을 출력
  ```
  * `abs`
    * `abs(시작값 - 끝값)`을 통해 시작값과 끝값의 차이(절대값)를 반환
  ```python
  print(abs(10 - 15)) # 5
  ```
### 2. 반복문 while
#### (1) 기본문법
```python
while bool:
  print('bool이 참인 경우 계속해서 실행합니다.')
  break # 조건문과 함께 사용하여 특정 조건에서 반복을 정지시킵니다.

# 예제
n = 1
while n <= 100:
  print(n)
  n += 1
  if n > 100:
    break
```
### 3. 반목문 for
#### (1) 기본문법
* 순서가 있는 자료형과 같이 사용하게 됨 `String` `List`
```python
for el in [1, 2, 3]:
  print(el)
  # 1
  # 2
  # 3
```
#### (2) 메소드 & 키워드 활용 `range()` `break` `pass` `sum()`
* `range()`
  * 범위 설정
  * `range([시작숫자부터(default는 0),] 끝 숫자미만까지)` 
```python
for i in range(100):
  print(i)

# range()와 list()를 활용해 간편하게 리스트 만들기
list(range(1, 100+1)) # [1, 2, 3, ... 98, 99, 100]
```
* `break`
  * 특정 조건에서 반복을 멈춘다.
```python
for i in range(100):
  print(i)
  if i > 30:
    break
  # 1
  # 2 ...
  # 31
```
* `pass`
  * 특정 조건에서 반복문의 실행을 스킵하여 패스하고 다음으로 넘어간다.
  * 비어있는 for문, 함수, 클래스 생성시 에러를 방지하는 팁으로 사용할 수 있음
  * format()은 [고급 문자열 포매팅] https://wikidocs.net/13 나 2일차 3. (3) String format 참고
```python
for i in range(1, 100+1):
  if i % 2 == 0:
    print('{} 짝수입니다.'.format(i))
  else:
    pass
  # 2 짝수입니다.
  # 4 짝수입니다. ...
  # 100 짝수입니다.
```
* `sum()`
  * 범위 안에 있는 모든 수들의 합을 반환
```python
sum([1, 2, 3, 4, 5]) # 15
```
