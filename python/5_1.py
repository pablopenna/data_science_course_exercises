import sys


num = int(sys.argv[1])
print("your number is {}".format(sys.argv[1]))

result = ""

if num < 0:
    result += "1"
elif num >= 0:
    result += "0"

if (num+1)%2 == 0:
    result += "a"
elif num%3 == 0:
    result += "b"
else:
    result += "c"

print(result)

