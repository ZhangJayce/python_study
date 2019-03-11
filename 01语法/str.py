str1 = "hello world hello hello hello"

print(max(str1))
#替换
print(str1.replace("hello","world", -1))
print(str1)
print(str1.endswith("ld"))

#创建字符串的映射表

str2 = str.maketrans("ab","cd")#a -> c,b -> d

print("zhang jian".startswith("zhang",0,5))

print(len("zhang jian"))

print("zhang jian".encode("utf-8"))

print("一".isnumeric())
print("1".isdigit())
print("\n\t\r".isspace())

