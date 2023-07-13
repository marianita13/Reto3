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
    print('+','-'*55,'+')
    print("|{:^12}{}{:^15}|".format(' ','ADMINISTRACION DE PERSONAL',' '))
    print('+','-'*55,'+')
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
                "ocupacion":ocupacion
            }

            diccPersonal["data"].append(persona)
            core.crearInfo("personal.json", persona)
    elif (opcion==2):
        id = input("Digite el Id: ")
        for i in range (diccPersonal["data"]):
            if id in i["id"]:
                os.system("clear")
                print(f"ID: {i['id']}\nNombre: {i['nombre']}\nOcupacion: {i['ocupacion']}\nEmail Personal: {i['emailPersonal']}\nEmail Corporativo: {i['emailCorporativo']}\nCelular: {i['celular']}\nTelefono: {i['telefono']}\nTelefono empresarial: {i['PhoneBuss']}")
                input("")
    elif (opcion==3):
        pass
    elif (opcion==4):
        pass
    elif (opcion==5):
        bandera = False