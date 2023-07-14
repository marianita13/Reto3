import core
import os

diccPersonal = {"data":[]}

def crearpersona():
    global diccPersonal
    if (core.checkfile("personal.json")):
        diccPersonal = core.LoadInfo("personal.json")
    else:
        core.crearInfo("personal.json", diccPersonal)

def Menu():
    os.system("clear")
    bandera = True
    print('+','-'*51,'+')
    print("|{:^12}{}{:^15}|".format(' ','ADMINISTRACION DE PERSONAL',' '))
    print('+','-'*51,'+')
    print("""1. Agregar personal
2. Buscar personal
3. Editar personal
4. Eliminar personal
5. Salir""")
    opcion = int(input("Digite una opcion: "))

    if (opcion==1):
        ids = []
        for i in range (len(diccPersonal["data"])):
            ids.append(diccPersonal["data"][i]["id"])

        id = input("Digite el Id: ")
        if id in ids:
            print("El id ya esta registrado")
            input("")
        else:
            tipos = ["Trainer", "Camper", "Admin", "Review programmer"]
            for i,item in enumerate (tipos):
                print(f'{i+1}: {item}')
            tipo = int(input("Digita una opción: "))
            ocupacion = tipos[tipo-1]    

            persona = {
                "id":id,
                "nombre": input("Ingrese el nombre: ").title(),
                "emailPersonal": input("Ingrese el email personal: "),
                "emailCorporativo": input("Ingrese el email corporativo: "),
                "celular": input("Digite el numero de celular: "),
                "telefono": input("Digite el numero fijo: "),
                "PhoneBuss": input("Digite el numero empresarial: "),
                "ocupacion": ocupacion
            }

            diccPersonal["data"].append(persona)
            core.crearInfo("personal.json", persona)
    elif (opcion==2):
        contador = 0
        id = input("Digite el Id: ")
        for i,item in enumerate(diccPersonal["data"]):
            contador +=1
            if id in item["id"]:
                os.system("clear")
                print(f"ID: {item['id']}\nNombre: {item['nombre']}\nOcupacion: {item['ocupacion']}\nEmail Personal: {item['emailPersonal']}\nEmail Corporativo: {item['emailCorporativo']}\nCelular: {item['celular']}\nTelefono: {item['telefono']}\nTelefono empresarial: {item['PhoneBuss']}")
                input("")
            elif (contador==len(diccPersonal["data"])):
                print("ID no registrado")
                input("")
    elif (opcion==3):
        contador = 0
        id = input("Digite el Id: ")
        for i,item in enumerate(diccPersonal["data"]):
            contador +=1
            if id in item["id"]:
                item["nombre"] = input("Digite el nuevo nombre: ").title() or item["nombre"]
                item["emailPersonal"] = input("Digite el email personal nuevo: ") or item["emailPersonal"]
                item["emailCorporativo"] = input("Digite el email corporativo nuevo: ") or item["emailCorporativo"]
                item["celular"] = input("Digite el nuevo numero de celular: ")

                print("NUEVOS CAMBIOS")
                for llave,valor in item.items():
                    print(f"{llave}: {valor}")
                input("")

                core.EditarData("personal.json",diccPersonal)
                break
            elif (contador == len(diccPersonal["data"])):
                print("ID no registrado")
                input("")
    elif (opcion==4):
        pass
    elif (opcion==5):
        bandera = False