import sys

string = sys.argv[1]
print("your str is {}".format(string))

l_longitudes = []
longitud_media = -1
longitudes_sum = 0
longitud_counter = 0

palabras = string.split(" ")
for palabra in palabras:
    l_palabra = len(palabra)
    l_longitudes.append(l_palabra)
    longitudes_sum += l_palabra

longitud_media = longitudes_sum/len(l_longitudes)


print(f"Palabras: {palabras}")
print(f"Longitudes: {l_longitudes}")
print(f"Media Longitudes: {longitud_media}")
