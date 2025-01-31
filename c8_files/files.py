import os 

# print(os.getcwd())
fhand = open('c8_files/mbox.txt')

# 개행문자가  포함되어 있는데, 한줄을 \n 더 입력해줘서 개행이 두칸씩된다.
# for line in fhand:
#     print(line)
# fhand.close()  # 파일을 닫아야 함

# with open('mbox.txt') as fhand:
#     for line in fhand:
#         print(line, end="")  

# 전체 파일을 열고 하나의 string으로 만듬
# 줄은 \n으로 분리된다
result = fhand.read()
print(result[:20])
print(result)