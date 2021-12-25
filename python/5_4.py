import sys


num = int(sys.argv[1])

divisores = []
for i in range(num+1):
    if i!=0 and num%i == 0:
        divisores.append(i)

print(f"Divisores: {divisores}")

if len(divisores)==2 or num==1:
    print("True")
else:
    print("False")

