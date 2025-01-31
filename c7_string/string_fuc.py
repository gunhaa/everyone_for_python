str = 'Monty Python'
print(str[0:4])
print(str[6:7])
# 에러를 일으키지 않고 마지막 인덱스까지만 슬라이스한다
print(str[6:20])
# 안 넣어줄 경우 처음부터 끝까지
# 에러를 일으키지 않는다
print(str[:2])
print(str[8:])
print(str[:])

print("-----------------")
print('hihi\nhihi')

print("-----------------")

# word가 객체라서 해당 함수 호출이 가능하다.
word = "HeLlO BoB"
print(word.lower())
print(word.upper())

# 인덱스를 찾는다
# 없으면 -1 반환
result = word.find("Bo")
print(result)

# strip은 양쪽의 공백문자를 제거한다
# \t tab, \n newline 줄바꿈(unix, linux, macOS), \v vertical tab
# \f form feed, \r carriage return 줄 맨 앞으로 이동(오래된 MAC), " " space, , \r\n(windows)
greet = "   h ello bab    "
print(greet.lstrip())
print(greet.rstrip())
print(greet.strip())

line = 'Please have a nice day'
#True
print(line.startswith('Please'))
#False
print(line.startswith('p'))

# 파이썬은 2버전은 unicode도 있어서 혼선이 있었지만,
# 3에서는 모두 유니코드로 통일 되었다.