x=5
# Condition
if x<10:
    print('Smaller')
if x>20:
    print('Bigger')

print('Finis')

# Indentation
# 띄어쓰기를 4번해서 들여쓰기(Indentation)를 한다
# Ide를 쓰지 않는다면, tab키는 위험하다
# python언어의 ide는 탭키를 띄어쓰기 4개로 인식해서 가능한 것임

# 파이썬에서 들여쓰기와 내어쓰기는 무언가 발생했다는 것을 의미한다.

# Nested Decision
x = 42
if x>1 :
    print('more than one')
    if x<100 :
        print('Less than 100')
print('all done')

# Multi-way
# 예약어 elif

y = 5 
if y<2 :
    print('small')
elif y<10 :
    print('medium')
else :
    print('large')
print('all done')