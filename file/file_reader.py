# with open('file/pi_digit.txt') as file_object:
#     contents = file_object.read()
#     print(contents)

# 关键字with在不需要访问文件之后将其关闭，
# 这样就把关闭文件的选择权交给了python，python自会在合适的时候自动将文件关闭
# open函数返回一个表示文件file/pi_digit.txt的对象，python将这个对象存储在变量contents中

# 逐行读取，用for循环
# 读取结果会多俩行空白，因为每行末尾都有看不到的换行符，以及print语句也会加上一个换行符
# file_name = 'file/pi_digit.txt'
# with open(file_name) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# “使用关键字with时，open()返回的文件对象只在with代码块内可用”
# file_name = 'file/pi_digit.txt'
# with open(file_name) as file_object:
#     lines  = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# 使用文件的内容
file_name = 'file/pi_digit.txt'
with open(file_name) as file_object:
    lines  = file_object.readlines()

pi_string = ""

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print(pi_string[:12])
print(len(pi_string))