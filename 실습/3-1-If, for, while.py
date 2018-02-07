### 어렵지 않아요.
inputValue = float(input('1~10 사이의 실수를 입력하세요.'))
if inputValue < 3:
  print('3보다 작아요')
elif inputValue >= 3 and inputValue < 6:
  print('3보다 같거나 크고 6보다 작네요')
else:
  print('6과 같거나 보다 크네요!')


### 조금 힘들껄요: 랜덤 숫자 맞추기
import random

ranNum = random.randint(1, 100)
inputNum = int(input('1~100 사이의 정수를 입력해서 랜덤 수를 맞혀보세요.'))
if abs(inputNum - ranNum) <= 10:
  print('아깝네요.')
elif inputNum != ranNum:
  print('틀렸습니다.')
else:
  print('정답입니다.')
  
### 어렵지 않아요: 랜덤 숫자 맞추기
import random

ranNum = random.randint(1, 100)
while True:
  inputNum = int(input('1~100 사이의 정수를 입력해서 랜덤 수를 맞혀보세요.'))
  if abs(inputNum - ranNum) <= 10:
    print('아깝네요.')
  elif inputNum != ranNum:
    print('틀렸습니다.')
  else:
    print('정답입니다.')
    break