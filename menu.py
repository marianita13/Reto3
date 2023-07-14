import core
import os
import areas
import insidencias
import inventario
import personal

if __name__ == '__main__':
    bandera = True
    while (bandera==True):
        try:
            os.system("clear")
            print('+','-'*40,'+')
            print("|{:^9}{}{:^9}|".format(' ','ADMINISTRACION DE CAMPUS',' '))
            print('+','-'*40,'+')
            print("""1. Areas de Campus
2. Personal de Campus
3. Inventario salones de Campus
4. Insidencias de Campus
5. Salir""")
            opcion = int(input("Digite una opcion: "))
            if (opcion==1):
                areas.crearArea()
                areas.Menu()
            elif (opcion==2):
                personal.crearpersona()
                personal.Menu()
            elif (opcion==3):
                inventario.buscarInfoAreas()
                inventario.crearInventario()
                inventario.Menu()
            elif (opcion==4):
                pass
            elif (opcion==5):
                bandera = False
                
        except:
            print("Opcion no valida")
            input("")
