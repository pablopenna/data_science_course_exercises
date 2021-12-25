import sys


num = int(sys.argv[1])
print("your number is {}".format(sys.argv[1]))

divisores = []
for i in range(num):
    if i!=0 and num%i == 0:
        divisores.append(i)

print(f"result: {divisores}")

