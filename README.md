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
## 2일차(1): Type과 연산(Numbers, String, Boolean), 데이터 구조(List)
### 1. 변수에 대한 이해
* 변수의 목적
  * 불필요한 중복과 반복적인 작업을 제거
* 파이썬 REPL 환경에서는 변수_가 기본적으로 최신 연산 값을 갖고 있음(인위적으로 _에 값을 할당해주면 이 기능이 작동하지 않음)
### 2. 연산자
* a // b (a를 b로 나눈 몫)
* a ** b (a를 b제곱한 값)
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
#### (3) Sting format
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
#### 빌트인 함수(built-in function)
  `.length
### 5. Boolean

### 6. 타입 변환
```python
int() # 값을 Int로 변환
float() # 값을 Float으로 변환
str() # 값을 String으로 변환
```

