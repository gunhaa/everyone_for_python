
str1 = "a\nb"
print(str1)
# 하나의 문자 취급을 해 len은 3이 된다.
print(len(str1))
str2 = "a\rb"
print(str2)
# windows식 줄바꿈이지만, len은 4로 잡힌다
str3 = "a\r\nb"
print(str3)
print(len(str3))