
str = 'hello' + "there"
print(str)
# 오류 발생
# str = str + 1
print(type(str))
print(type(1))
print(type(1.0))
print("-------------------")
print(float(99) + 100)
i=42
print(type(i))
f=float(i)
print(f)
print(type(f))


# 파이썬3에서 나누기가 개선되었음
print("-------------------")
print(10/2)
print(9/2)
print(99/100)
# 파이썬3에서 integer 나누기 결과는 부동소수점이 나온다

print(10.0/2.0)
print(99.0/100.0)

# String Conversions
print("-------------------")

sval = '123'
print(type(sval))
# 오류 발생
# print(sval +1)

ival = int(sval)
print(type(ival))
print(ival+1)
nsv = 'hello bab'
# 오류 발생
# 숫자만 가능
# niv = int(nsv)


# builtin function input
name = input('who are you?')
print('welcome' , name)
