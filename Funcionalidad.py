from Lista import Lista
import os

class Funcionalidad:
    def __init__(self):
        self.lista = Lista()
        self.nodo = None
    
    
    def ingresar_contacto(self):
        nombre = input('\033[93m' + "Ingrese el nombre: " + '\033[0m')
        apellido = input('\033[93m' + "Ingrese el apellido: " + '\033[0m')
        numero = input('\033[93m' + "Ingrese el número de teléfono: " + '\033[0m')
        print(self.lista.buscar(numero))
        if self.lista.buscar(numero) == False:
            self.lista.push(nombre, apellido, numero)
            print('\033[92m' + "El contacto ha sido agregado exitosamente!." + '\033[0m')
        else:
            print('\033[91m' + "El contacto ya existe." + '\033[0m')
    
    def buscar_contacto(self):
        numero = input('\033[93m' + "Ingrese el número que desea buscar: " + '\033[0m')
        if self.lista.buscar(numero) == False:
            decision = input('\033[93m' + "El contacto no existe, desea agregarlo? (y/n)" + '\033[0m')
            if decision == "y":
                nombre = input('\033[93m' + "Ingrese el nombre: " + '\033[0m')
                apellido = input('\033[93m' + "Ingrese el apellido: " + '\033[0m')
                self.lista.push(nombre, apellido, numero)
                print('\033[92m' + "El contacto ha sido agregado exitosamente!." + '\033[0m')
            elif decision == "n":
                pass
        else:
            print("")
            print('\033[92m' + "El contacto ha encontrado." + '\033[0m')
            print('\033[92m' + "**************************" + '\033[0m')
            print('\033[92m' + "Nombre: " + self.lista.buscar(numero).obtener_nombre() +'\033[0m')
            print('\033[92m' + "Apellida: " + self.lista.buscar(numero).obtener_apellido() +'\033[0m')
            print('\033[92m' + "Número de teléfono: " + self.lista.buscar(numero).obtener_telefono() +'\033[0m')
            print('\033[92m' + "**************************" + '\033[0m')

    def visualizar(self):
        self.lista.guardar_lista()
        inicio = "digraph G {\nrankdir=TB\n\nAgenda[shape=plaintext label=\"Agenda\"]\n"
        contactos = "contacto$[shape=box label=\"Nombre: #\n Apellido: %\n Teléfono: &\"]\n"
        primera = "Agenda -> contacto0 [style=invis]\n"
        transicion = "contacto$->contacto# [dir=both]\n"
        contador = 0
        crear = open("grafico.dot", "a+", encoding='utf-8')
        crear.write(inicio)
        for x in self.lista.listaContactos:
            crear.write(contactos.replace("$",str(contador)).replace("#",x.split(",",2)[0]).replace("%",x.split(",",2)[1]).replace("&",x.split(",",2)[2]))
            contador+=1
        crear.write(primera)
        for i in range(contador):
            if i < contador-1:
                crear.write(transicion.replace("$",str(i)).replace("#",str(i+1)))
            else:
                break
        crear.write("}")
        crear.close()
        os.system("dot -Tpng grafico.dot -o grafico.png")
        os.system("grafico.png")
        os.remove("grafico.dot")
