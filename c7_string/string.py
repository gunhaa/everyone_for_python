
# 파이썬의 문자열

# 기본적으로 index(좌표)를 가지며, 0부터 시작한다.
# 예전에는 효율때문에 0부터 시작했지만, 요즘은 관습적으로 0으로 시작한다.
# 인덱스는 연산자이며, 대괄호[]를 이용한 문법으로 사용할 수 있다.
# 범위를 벗어난 index의 호출은 에러를 일으킨다.

str = 'abcd'
try:
    print(str[4])
except:
    print("out of index")
    print("this str len is", len(str))


fruit = 'banana'
for char in fruit:
    print(char)

for i in range (0, len(fruit)):
    print(fruit[i])