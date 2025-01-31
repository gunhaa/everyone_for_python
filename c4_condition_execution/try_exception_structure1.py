
# 프로그램이 중단 위험에 있는 코드를 try - except로 감싸서
# 프로그램을 종료시키지 않고 다음 코드 블록으로 진행시킬 수 있다.

astr = 'hello bab'
try:
    istr = int(astr)
except:
    istr = -1

print('First', istr)

astr='123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second', istr)