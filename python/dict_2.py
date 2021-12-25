compra = dict()

def displayData():
    print(f"Data: {compra}")

def getTotal(compraDict):
    return sum(list(compraDict.values()))

def showTotal(compraDict):
    print("Articulo | Precio")
    for x, y in zip(list(compraDict.keys()), list(compraDict.values())):
        print(f"{x} | {y}")
    print(f"Total compra: {getTotal(compraDict)}")

while True:
    articulo = input("Nombre articulo (0 to total, -1 to finish): ")
    if articulo == "-1":
        break
    if articulo == "0":
        showTotal(compra)
        continue
    precio = float(input("Precio articulo: "))
    compra.update({articulo: precio})
    displayData()
