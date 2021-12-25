
def tempSupMedia(listaDias):
    media = sum(listaDias)/len(listaDias)
    return [elem for elem in listaDias if elem > media]

def diasSupMedia(listaDias):
    media = sum(listaDias)/len(listaDias)
    return [idx+1 for idx,elem in enumerate(listaDias) if elem > media]

def crearDictDias(listaDias):
    claves = diasSupMedia(listaDias)
    valores = tempSupMedia(listaDias)
    d = {}
    for k,v in zip(claves, valores):
        d[k] = v
    return d


lista_dias = [11,5,6,13,7,8,9,10,11]
print(f"res1: {tempSupMedia(lista_dias)}")
print(f"res2: {crearDictDias(lista_dias)}")
