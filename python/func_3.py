
def getFrecuenciaDict(cadena):
    listaPalabras = cadena.split(" ")
    dictFrec = dict()
    for palabra in listaPalabras:
        if palabra in dictFrec:
            dictFrec[palabra] += 1
        else:
            dictFrec[palabra] = 1
    return dictFrec

def mostFrequentWord(frecuenciaDict):
    maxKey = None
    maxValue = 0
    for k,v in frecuenciaDict.items():
        if v > maxValue:
            maxKey = k
            maxValue = v
    return (maxKey, maxValue)

#Alternative function using comprehentions
#A dict cannot reference itsel on a dict comprehension:
#    https://stackoverflow.com/a/67453653
def getFrecuenciaDictComprehension(cadena):
    listaPalabras = cadena.split(" ")
    dictFrec = dict()
    dictFrec = {k : (dictFrec[k]+1)  if k in dictFrec else 1 for k in listaPalabras}
    return dictFrec

#Alternative function using comprehentions
def mostFrequentWordComprehension(frecuenciaDict):
    maxKey = None
    maxValue = 0
    for k,v in frecuenciaDict.items():
        if v > maxValue:
            maxKey = k
            maxValue = v
    return (maxKey, maxValue)

cadena = input("Escribe cadena: ")
if cadena == "":
    cadena = "a a a b b c casa coche camion casa casa camion casa casa casa"
d = getFrecuenciaDict(cadena)
print(f"frecuencias: {d}")
t = mostFrequentWord(d)
print(f"Most frequent: {t}")
dc = getFrecuenciaDictComprehension(cadena)
print(f"Testing comprehension #1: {dc}")
