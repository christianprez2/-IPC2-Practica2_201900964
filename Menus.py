from Funcionalidad import Funcionalidad

class Menu:

    def __init__(self):
        self.menu = """
************** MENU **************
1. Ingresar nuevo contacto
2. Buscar contacto
3. Visualizar agenda
4. Salida
**********************************"""
        self.funcionalidad = Funcionalidad()

    def menu_principal(self):
            seleccion = 0
            finalizar = True
            while finalizar:
                print(self.menu)
                try:
                    seleccion = int(input('\033[93m' + "Selecciona una opción:" + '\033[0m'))
                except:
                    pass
                if seleccion is 1:
                    self.funcionalidad.ingresar_contacto()
                    seleccion = 0
                elif seleccion is 2:
                    self.funcionalidad.buscar_contacto()
                    seleccion = 0
                elif seleccion is 3:
                    self.funcionalidad.visualizar()
                    seleccion = 0
                elif seleccion is 4:
                    print('\033[91m' + "Finalizando aplicacion..." + '\033[0m')
                    seleccion = 0
                    finalizar = False
                else:
                    print('\033[91m'+ "Selección incorrecta, ingresa una opción válida..." + '\033[0m')
    