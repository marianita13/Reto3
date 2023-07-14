import core
import json
import os

diccInventario = {"data":[]}
AreasInfo = {}

def buscarInfoAreas():
    with open('data/'+'areas.json') as file:
        InfoAreas = json.load(file)
        AreasInfo.update(InfoAreas)

def crearInventario():
    global diccInventario
    if (core.checkfile("inventario.json")):
        diccInventario = core.LoadInfo("inventario.json")
    else:
        core.crearInfo("inventario.json", diccInventario)

def Menu():
    os.system("clear")
    bandera=True
    print('+','-'*50,'+')
    print("|{:^11}{}{:^13}|".format(' ','ADMINISTRACION DE INVENTARIO',' '))
    print('+','-'*50,'+')
    print("""1. Agregar inventario
2. Buscar inventario
3. Editar inventario
4. Eliminar inventario
5. Salir""")
    opcion = int(input("Digite una opcion: "))

    if opcion==1:
        os.system("clear")
        print('+','-'*41,'+')
        print("|{:^12}{}{:^15}|".format(' ','AGREGAR PERSONAL',' '))
        print('+','-'*41,'+')
        ids = []
        for i in range(len(diccInventario['data'])):
            ids.append(i["id"])
        id = input("Ingrese el Id del Pc: ")
        if id in ids:
            print("El ID ya está registrado.")
            input("")
        else:
            for i,itemA in enumerate (AreasInfo["data"]):
                print(f'{i+1}: {itemA["nombre"]}')
            contador = 0
            areas = int(input("A que area pertenece?: "))
            for i,itemB in enumerate (AreasInfo["data"]):
                contador+=1
                if areas == i+1:
                    area = itemB["nombre"]
                elif (contador==len(AreasInfo['data'])):
                    print("Esta area no esta registrada")
            
            contadorC = 0
            for i,itemC in enumerate (AreasInfo["data"]):
                contadorC+=1
                if area == itemC["nombre"]:
                    for x,item in enumerate (itemC["salones"]):
                        print(f'{x+1}: {item["nombre"]}')
                    salones = int(input("A que area pertenece?: "))
                    contador = 0
                    for f,item in enumerate(itemC["salones"]):
                        contador+=1
                        if salones == f+1:
                            salon = item["nombre"]
                        elif (contador==len(itemC["salones"])):
                            print("Este salon no esta registrado")
                else:
                    pass

            data = {
                "Id":id,
                "Area":area,
                "Salon":salon,
                "Perife":[]
            }

            idP = input("Digite el id del pc: ")
            idsP = []
            for i in range (len(diccInventario["data"][id]["Perife"])):
                idsP.append(diccInventario["data"][i]["id"])

            id = input("Digite el Id: ")
            if idP in idsP:
                print("El id ya esta registrado")
                input("")

    elif (opcion==2):
        pass
    elif (opcion==3):
        pass
    elif (opcion==4):
        pass
    elif (opcion==5):
        bandera=False