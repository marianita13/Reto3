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
    os.system("cls")
    bandera=True
    print('+','-'*50,'+')
    print("|{:^11}{}{:^13}|".format(' ','ADMINISTRACION DE INVENTARIO',' '))
    print('+','-'*50,'+')
    print("""1. Agregar inventario
2. Agregar Perifes
3. Buscar inventario
4. Editar inventario
5. Eliminar inventario
6. Salir""")
    opcion = int(input("Digite una opcion: "))

    if opcion==1:
        os.system("cls")
        print('+','-'*41,'+')
        print("|{:^12}{}{:^15}|".format(' ','AGREGAR INVENTARIO',' '))
        print('+','-'*41,'+')
        ids = []
        for i in range(len(diccInventario['data'])):
            ids.append(diccInventario['data'][i]['Id'])
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
                    contador=0
                elif (contador==len(AreasInfo['data'])):
                    print("Esta area no esta registrada")
            
            contadorC = 0
            for i,itemC in enumerate (AreasInfo["data"]):
                contadorC+=1
                if area == itemC["nombre"]:
                    for x,item in enumerate (itemC["salones"]):
                        print(f'{x+1}: {item["nombre"]}')
                    salones = int(input("A que salon pertenece?: "))
                    contador = 0
                    for f,item in enumerate(itemC["salones"]):
                        contador+=1
                        if salones == f+1:
                            salon = item["nombre"]
                        elif (contador==len(itemC["salones"])):
                            print("Este salon no esta registrado")
            data = {
                "Id":id,
                "Area":area,
                "Salon":salon,
                "Perife":[]
            }
            diccInventario["data"].append(data)
            core.crearInfo("inventario.json",data)

    elif (opcion==2):
        os.system("cls")
        print('+','-'*40,'+')
        print("|{:^12}{}{:^15}|".format(' ','AGREGAR PERIFES',' '))
        print('+','-'*40,'+')
        Id_pc = input('Digite el Id del pc: ')
        contador = 0
        banderaO=False
        for i,item in enumerate (diccInventario["data"]):
            contador+=1
            if (item['Id']==Id_pc):
                if (len(item['Perife'])==3):
                    print ("Ya se han agregado todos los perifericos al equipo seleccionado")
                    input("")
                    break
                objetos = ["Audifonos", "Teclado", "Mouse"]
                for l,itemX in enumerate(objetos):
                    print(f'{l+1}: {itemX}')
                op = int(input("Elije una: "))
                for i,itemJ in enumerate(objetos):
                    if op == i+1:
                        objeto = objetos[i]
                        if (len(item['Perife'])==0):
                            data = {
                                    'nombre':objeto,
                                    'Id': input(f'Digite el Id del {objeto}: '),
                                    "marca" : input("Digite la marca: ")
                                }
                            item['Perife'].append(data)
                            core.EditarData("inventario.json",diccInventario)
                        else: 
                            contadorA = 0
                            for i,itemL in enumerate(item['Perife']):
                                contadorA+=1
                                if (itemL["nombre"]==objeto):
                                    print("Este objeto ya esta asignado.")
                                    input("")
                                    banderaO=True
                                    break
                                elif (contadorA==len(item["Perife"])):
                                    data = {
                                        'nombre':objeto,
                                        'Id': input(f'Digite el Id del {objeto}: '),
                                        "marca" : input("Digite la marca: ")
                                    }
                                    item['Perife'].append(data)
                                    core.EditarData("inventario.json",diccInventario)
                                    banderaO=True
                                    break
                    elif (op>=4):
                        print("Esta opcion no existe.")
                        input("")
                        break
            elif (banderaO==True):
                break
            elif (contador==len(diccInventario["data"])):
                print('El Id no esta registrado: ')
                input("")
                break

    elif (opcion==3):
        os.system("cls")
        print('+','-'*41,'+')
        print("|{:^12}{}{:^14}|".format(' ','BUSCAR INVENTARIO',' '))
        print('+','-'*41,'+')
        id_Pc = input("Digite el Id del pc: ")
        contadorI = 0
        banderaB = False
        for item in diccInventario["data"]:
            contadorI+=1
            if item["Id"]==id_Pc:
                os.system("cls")
                print(f"Id Pc: {item['Id']}\nArea: {item['Area']}\nSalon: {item['Salon']}\n")
                print("PERIFERICOS ASIGNADOS")
                for x,itemW in enumerate(item["Perife"]):
                    print(f"{x+1}. {itemW['nombre']}")
                input("")
                banderaB = True         
            elif (banderaB==True):
                break
            elif (contadorI==len(item)):
                print('No se encontro ningun Pc con ese Id')
                input("")
    elif (opcion==4):
        os.system("cls")
        print('+','-'*41,'+')
        print("|{:^12}{}{:^14}|".format(' ','EDITAR INVENTARIO',' '))
        print('+','-'*41,'+')
        id_Pc = input("Digite el Id del pc: ")
        contadorI = 0
        for item in diccInventario["data"]:
            contadorI+=1
            if item["Id"]==id_Pc:
                for i,itemA in enumerate (AreasInfo["data"]):
                    print(f'{i+1}: {itemA["nombre"]}')
                contador = 0
                areas = int(input("A que area desea cambiarlo?: "))
                for i,itemB in enumerate (AreasInfo["data"]):
                    contador+=1
                    if areas == i+1:
                        item["Area"] = itemB["nombre"]
                        contador=0
                    elif (contador==len(AreasInfo['data'])):
                        print("Esta area no esta registrada")
                
                contadorC = 0
                for i,itemC in enumerate (AreasInfo["data"]):
                    contadorC+=1
                    if item["Area"] == itemC["nombre"]:
                        for x,itemQ in enumerate (itemC["salones"]):
                            print(f'{x+1}: {itemQ["nombre"]}')
                        salones = int(input("A que salon desea cambiarlo?: "))
                        contador = 0
                        for f,itemX in enumerate(itemC["salones"]):
                            contador+=1
                            if salones == f+1:
                                item["Salon"] = itemX["nombre"]
                            elif (contador==len(itemC["salones"])):
                                print("Este salon no esta registrado")
                os.system("clear")
                print("NUEVOS CAMBIOS")
                for llave,valor in item.items():
                    print(f"{llave}: {valor}")
                input("")

                core.EditarData("inventario.json",diccInventario)
                break

            elif(contadorI==len(diccInventario["data"])):
                print("Este computador no esta registrado")
                input("")
    elif (opcion==5):
        os.system("cls")
        print('+','-'*45,'+')
        print("|{:^12}{}{:^14}|".format(' ','ELIMINAR INVENTARIO',' '))
        print('+','-'*45,'+')
        id_Pc = input("Digite el Id del pc: ")
        contadorI = 0
        for item in diccInventario["data"]:
            contadorI+=1
            if item["Id"]==id_Pc:
                os.system("cls")
                print("Deseas eliminar:\n1. Pc\n2. Un periferico")
                opcionE = int(input(": "))
                if opcionE == 1:
                    diccInventario["data"].remove(item)
                    core.EditarData("inventario.json",diccInventario)
                elif opcionE==2:
                    if (len(item['Perife'])==0):
                        print("Noe existen perifericos asignados.")
                        input("")
                    else:
                        for i,valor in enumerate(item["Perife"]):
                            print(f'{i+1}. {valor["nombre"]}')
                        Perife =int(input("Cual deseas eliminar?: "))
                        for o,eliminar in enumerate(item['Perife']):
                            if (Perife==(o+1)):
                                item["Perife"].remove(eliminar)
                                core.EditarData("inventario.json",diccInventario)
                                print("Incidencia eliminada corecctamente.")
                                input("")
    elif (opcion==6):
        bandera=False
