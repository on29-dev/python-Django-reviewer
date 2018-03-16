with open('./new.txt', 'w') as f: # f = open()
  f. write("안녕하세요! with입니다.")

if not f.closed:
  print("파일이 꺼지지 않았습니다... 큰일났어요...")