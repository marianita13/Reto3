import core
import json
import os
from datetime import datetime
import time

diccIncidencias = {"data":[]}
AreasInfo = {}
InventarioInfo = {}
personalInfo = {}

def buscarInfoAreas():
    with open('data/'+'areas.json') as file:
        InfoAreas = json.load(file)
        AreasInfo.update(InfoAreas)

def buscarInfoInventario():
    with open('data/'+'inventario.json') as file:
        InfoInve = json.load(file)
        InventarioInfo.update(InfoInve)

def buscarInfoPersonal():
    with open('data/'+'personal.json') as file:
        InfoPerson = json.load(file)
        personalInfo.update(InfoPerson)

def crearIncidencias():
    global diccIncidencias
    if (core.checkfile("incidencias.json")):
        diccIncidencias = core.LoadInfo("incidencias.json")
    else:
        core.crearInfo("incidencias.json", diccIncidencias)

def Menu():
    os.system("cls")
    bandera=True
    print('+','-'*50,'+')
    print("|{:^11}{}{:^13}|".format(' ','ADMINISTRACION DE INCIDENCIAS',' '))
    print('+','-'*50,'+')
    print("""1. Agregar incidencia
2. Buscar incidencia
3. Eliminar incidencia
4. Salir""")
    opcion = int(input("Digite una opcion: "))

    if (opcion==1):
        os.system("cls")
        print('+','-'*43,'+')
        print("|{:^12}{}{:^14}|".format(' ','AGREGAR INCIDENCIA',' '))
        print('+','-'*43,'+')
        if (len(diccIncidencias['data'])==0):
            tipo = {
                "Hardware":[],
                "Software":[]
            }
            diccIncidencias['data'].append(tipo)
            core.crearInfo("incidencias.json",tipo)
            print("Ya puedes crear incidencias")
            input("")
        else:
            os.system("cls")
            print("Que tipo de incidencia es?:\n1. Hardware\n2. Software")
            opcionT= int(input(": "))
            categorias = ["Leve","Moderada","Critica"]
            for i,item in enumerate (categorias):
                print(f'{i+1}. {item}')
            prioridad = categorias[int(input(": "))-1]
            fecha = datetime.now().strftime("%Y-%m-%d")
            descripcion = input("\nDescriba la incidencia:\t").capitalize()
            os.system("cls")
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
            os.system("cls")
            for i,itemC in enumerate (AreasInfo["data"]):
                contadorC+=1
                banderaS=False
                if area == itemC["nombre"]:
                    for x,item in enumerate (itemC["salones"]):
                        print(f'{x+1}: {item["nombre"]}')
                    salones = int(input("A que salon pertenece?: "))
                    contador = 0
                    for f,item in enumerate(itemC["salones"]):
                        contador+=1
                        if salones == f+1:
                            salon = item["nombre"]
                            banderaS= True
                        elif(banderaS==True):
                            break
                        elif (contador==len(itemC["salones"])):
                            print("Este salon no esta registrado")
            os.system("cls")
            for i,itemO in enumerate (personalInfo["data"]):
                print(f'{i+1}: {itemO["nombre"]}')
            contador = 0
            personas = int(input("Quien reporta la incidencia?: "))
            for i,itemK in enumerate (personalInfo["data"]):
                contador+=1
                if personas == i+1:
                    nombre = itemK["nombre"]
                    ocupacion = itemK["ocupacion"]
                    contador=0
                elif (contador==len(personalInfo['data'])):
                    print("Esta persona no esta registrada")
            
            data = {
                "codigo": '',
                "prioridad" : prioridad,
                "fecha_creacion" : fecha,
                "descripcion" : descripcion,
                "area" : area,
                "salon" : salon,
                "usuario": nombre,
                "cargo":ocupacion
            }
            if (opcionT==1):
                for i,item in enumerate(diccIncidencias["data"]):
                    if len(item["Hardware"])==0:
                        codigo=str(1).zfill(2)
                    else:
                        codigo=str(len(item["Hardware"])+1).zfill(2)
                data["codigo"]=codigo
                item["Hardware"].append(data)
                core.EditarData("incidencias.json",diccIncidencias)
            elif (opcionT==2):
                for i,item in enumerate(diccIncidencias["data"]):
                    if len(item["Software"])==0:
                        codigo=str(1).zfill(2)
                    else:
                        codigo=str(len(item["Software"])+1).zfill(2)
                data["codigo"]=codigo
                item["Software"].append(data)
                core.EditarData("incidencias.json",diccIncidencias)

    elif (opcion==2):
        os.system("cls")
        print('+','-'*43,'+')
        print("|{:^12}{}{:^14}|".format(' ','BUSCAR INCIDENCIA',' '))
        print('+','-'*43,'+')
        print("Incidencia tipo:\n1. Hardware\n2. Software")
        opcionB = int(input(": "))
        os.system("cls")
        if opcionB==1:
            for i, item in enumerate(diccIncidencias["data"]):
                info = item["Hardware"]
                print("INCIDENCIAS EN HARDWARE")
                for a,itemD in enumerate(info):
                    print(f'{a+1}.{itemD["codigo"]}')
                op = int(input("Elije una: "))
                datosInc = diccIncidencias['data'][i]['Hardware'][op-1]
                for key,valor in datosInc.items():
                    print(f'{key}: {valor}')
            input("")
        elif opcionB==2:
            for i, item in enumerate(diccIncidencias["data"]):
                info = item["Software"]
                print("INCIDENCIAS EN Software")
                for a,itemD in enumerate(info):
                    print(f'{a+1}.{itemD["codigo"]}')
                op = int(input("Elije una: "))
                datosInc = diccIncidencias['data'][i]['Software'][op-1]
                for key,valor in datosInc.items():
                    print(f'{key}: {valor}')
            input("")

    elif(opcion==3):
        os.system("cls")
        print('+','-'*47,'+')
        print("|{:^12}{}{:^14}|".format(' ','ELIMINAR INCIDENCIA',' '))
        print('+','-'*47,'+')
        print("Incidencia tipo:\n1. Hardware\n2. Software")
        opcionB = int(input(": "))
        os.system("cls")
        if opcionB==1:
            for i, item in enumerate(diccIncidencias["data"]):
                info = item["Hardware"]
                print("INICIANDO ELIMINACION DE INFORMACIÓN...")
                for a,itemM in enumerate(info):
                    print(f'{a+1}.{itemM["codigo"]}')
                op = int(input("Elije una: "))
                datosInc = diccIncidencias['data'][i]['Hardware'][op-1]
                diccIncidencias["data"][i]["Hardware"].remove(datosInc)
                core.EditarData("incidencias.json",diccIncidencias)
    elif(opcion==4):
        bandera=False