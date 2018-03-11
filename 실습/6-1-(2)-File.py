f = open('./g_file.txt', 'w')
for i in range(10):
    content = "hello world!\n"
    f.write(content)

f.close()


k = open('./g_file.txt', 'a')
for i in range(10):
    k.write("hello python!\n")

k.close()

j = open('/Users/kwak/Documents/dev/python-Django-reviewer/실습/g_file.txt', 'r')
for _ in range(10):
    print(j.readline())

j.seek(0)
print(j.read())

j.close()