import sys


cadena = sys.argv[1].replace(" ", "")
print("your string is is {}".format(cadena))

# cadena[::-1] prints cadena but backwards. Very useful so you do not have to iterate.

def isPalindromo(string):
    print(len(string))
    print(len(string)/2)
    print("---")
    isPlindromoVar = True
    for i in range(len(string)//2):
        print("index: " + str(i))
        if string[i] == string[len(string)-1-i]:
            print("Ture")
        else:
            print("False")
            isPlindromoVar = False
    return isPlindromoVar

print(f"is palindromo? : {isPalindromo(cadena)}")
