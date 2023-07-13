import core
import os

diccPersonal = {"data":[]}

def crearṔersona():
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
2. Editar personal
3. Eliminar personal
4. Salir""")
    opcion = int(input("Digite una opcion: "))

    if (opcion==1):
        pass
    elif (opcion==2):
        pass