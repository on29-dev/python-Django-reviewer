# # 경로에는 상대경로와 절대경로
# # w, r, a

# f = open("./hello.txt", "r")
# content = f.read()
# print(content)
# f.seek(0)
# print(f.read())
# print(f.read())
# print(f.read())
# # 한번 읽으면 커서가 끝으로 가므로 계속 불러와도 소용이 없다.
# # 이럴 때.seek(0)을 이용한다.

# # for i in range(2, 10+1):
# #     content = "\n" + str(i) + "번째 줄입니다."
# #     f.write(content)

# f.close()

###


f = open("/Users/kwak/Documents/dev/python-Django-reviewer/실습/hello.txt", "r")
content = f.read()
print(content)
f.seek(0)
print(f.read())
print(f.read())
print(f.read())
# 한번 읽으면 커서가 끝으로 가므로 계속 불러와도 소용이 없다.
# 이럴 때.seek(0)을 이용한다.
# seek(n) n번째 글자로 커서 이동

# for i in range(2, 10+1):
#     content = "\n" + str(i) + "번째 줄입니다."
#     f.write(content)

f.close()