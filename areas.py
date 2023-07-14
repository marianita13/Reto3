import core
import os

diccAreas = {"data":[]}

def crearArea():
    global diccAreas
    if (core.checkfile("areas.json")):
        diccAreas = core.LoadInfo("areas.json")
    else:
        core.crearInfo("areas.json", diccAreas)

def Menu():
    os.system("clear")
    bandera = True
    print('+','-'*48,'+')
    print("|{:^12}{}{:^15}|".format(' ','ADMINISTRACION DE AREAS',' '))
    print('+','-'*48,'+')
    print("""1. Agregar Area
2. Agregar Salon
3. Eliminar Area o salon
4. Salir""")
    opcion = int(input("Digite una opcion: "))

    if (opcion==1):
        os.system("clear")
        print('+','-'*36,'+')
        print("|{:^12}{}{:^14}|".format(' ','AGREGAR AREA',' '))
        print('+','-'*36,'+')
        nombre = input("Nombre del area: ").title()
        id = input("Id del area: ")
        data = {
            "id":id,
            "nombre":nombre,
            "salones":[]
        }
        diccAreas['data'].append(data)
        core.crearInfo("areas.json",data)
        print("Area registrada")
        input("")
    elif (opcion==2):
        os.system("clear")
        print('+','-'*37,'+')
        print("|{:^12}{}{:^14}|".format(' ','AGREGAR SALON',' '))
        print('+','-'*37,'+')
        id = input("Digite el Id del area: ")
        contadorSalon = 0
        for i in diccAreas['data']:
            contadorSalon+=1
            if i["id"]==id:
                nombreSalon= input("Nombre del salon: ").title()
                idSalon = input("Id del salon: ")
                data = {
                    "id":idSalon,
                    "nombre":nombreSalon
                }
                i["salones"].append(data)
                core.EditarData("areas.json",diccAreas)
            elif ((contadorSalon) == (len(diccAreas['data']))):
                print("No existe ninguna area con este ID")
                input("")
    elif (opcion==3):
        os.system("clear")
        print('+','-'*43,'+')
        print("|{:^12}{}{:^14}|".format(' ','ELIMINAR AREA O SALON',' '))
        print('+','-'*43,'+')
        opcion = int(input("Desea eliminar:\n1. Area\n2. Salon\n: "))
        contador = 0
        area = input("Digite el nombre del area: ").title()
        for i,item in enumerate (diccAreas['data']):
            contador+=1
            if (opcion==1):
                if (area==item["nombre"]):
                    print(diccAreas['data'])
                    diccAreas['data'].pop(i)
                    print("Area eliminada")
                    core.EditarData("areas.json",diccAreas)
                    break
                elif (contador == len(diccAreas['data'])):
                    print("No existe ninguna area con este ID")
            elif (opcion==2):
                if (area==item["nombre"]):
                    salon = input("Digite el nombre del salon: ").title()
                    for a,item2 in enumerate(item["salones"]):
                        if (salon == item2["nombre"]):
                            item["salones"].remove(item2)
                            print("Salon eliminado")
                            core.EditarData("areas.json",diccAreas)

    elif (opcion==4):
        bandera=False