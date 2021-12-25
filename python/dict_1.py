
notas = dict()



def displayData():
    print(f"Data: {notas}")

def enterData():
    alumno = input("Enter student name:")
    if alumno not in notas:
        notas[alumno] = {}
    while(True):
        asignatura = input("Enter subject: (Enter -1 to finish)")
        if asignatura == "-1":
            break;
        nota = input("Enter grade:")
        if alumno in notas and asignatura in notas[alumno]:
            print("Grade for given student and subject already exists")
        else:
            print("Adding...")
            #I know, this is pure rubbish
            updateData = {}
            updateData[alumno] = {}
            updateData[alumno][asignatura] = nota
            print(f"updateData: {updateData}")
            notas[alumno].update(updateData[alumno])
            displayData()


while True:
    opt = input("Choose: 1 - Enter data, 2 - Display data")
    if opt == "1":
        enterData()
    else:
        displayData()
