
rawstr = input("Enter a Number: ")

try:
    convert = int(rawstr)
except:
    convert = -1

if(convert != -1):
    print("Enter Number")
else:
    print("why enter string")