import math


num = input()
remainder = (float(num)*10) % 10
print(remainder)

if(remainder < 5):
    print(math.floor(float(num)))
else:
    print(math.ceil(float(num)))
