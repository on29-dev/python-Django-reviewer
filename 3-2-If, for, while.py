# 간단~ 순서대로 출력1
# 숫자 1부터 100까지 for와 while을 이용해서 출력해보세요.

# while
i = 0
while i < 100:
  i += 1
  print(i) 

# for
for n in range(0, 100):
  print(n + 1)


# 어렵지 않아요: 1~100까지 다 더하기
n = 0
for i in range(1, 101):
  n += i
print(n)

# sum()을 활용
print(sum(range(1, 101)))

# 어렵지 않아요: 1~100 중 일부 더하기
# 1) 1~100까지 숫자 중 2와 3의 약수만 더하기
n = []
for i in range(1, 101):
  if i % 6 == 0:
    n.append(i)
  elif i % 3 == 0:
    n.append(i)
  elif i % 2 == 0:
    n.append(i)
  else:
    pass
print(sum(n))

# 조금 힘들껄요: fizzbuzz 문제
# 1~100까지 수를 출력하면서 3의 배수일 경우 'fizz', 5의 배수일 경우 'buzz', 15의 배수일 경우 'fizzbuzz'를 출력하세요
# 3의 배수나 5의 배수보다 15의 배수가 먼저 나와야 합니다. 안 그러면 15의 배수가 먼저 걸러지거든요.
for i in range(1, 101):
  if i % 15 == 0:
    print('fizzbuzz')
  elif i % 5 == 0:
    print('buzz')
  elif i % 3 == 0:
    print('fizz')
  else:
    print(i)

# 어렵죠?: 소수판별
# 1~1000까지 숫자 중에 소수만 출력
# 1과 자기 자신으로만 나누어 떨어지는 숫자
for i in range(1, 1001):
  n = []  
  for k in range(1, i + 1):
    if i % k == 0:
      n.append(k)
    else:
      pass
  if len(n) == 2 or len(n) == 1:
    print(i)
  else: 
    pass
# 해설
for i in range(1, 1000+1):
  key = True
  for j in range(2, i):
    if i % j == 0:
      key = False
      break
  if key:
    print(i)
