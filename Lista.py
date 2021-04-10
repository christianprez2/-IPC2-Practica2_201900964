from Nodo import Nodo

class Lista:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.envergadura = 0
        self.listaContactos = []
    
    def push(self, nombre, apellido, numero):
        nodo = Nodo(nombre, apellido, numero)
        if self.envergadura == 0:
            self.cabeza = nodo
            self.ultimo = nodo
            self.ultimo.siguiente = self.cabeza
        else:
            self.ultimo.siguiente = nodo
            nodo.siguiente = self.cabeza
        self.ultimo = nodo
        self.envergadura+=1
        
    def buscar(self, numero):
        nodo = self.cabeza
        existe = False
        contador = 0
        while(contador < self.envergadura and existe != True):
            if(numero == nodo.obtener_telefono()):
                existe = True
                return nodo
            else:
                nodo = nodo.siguiente
                contador+=1
        return False
        
    def guardar_lista(self):
        nodo = self.cabeza
        contador = 0
        #print("")
        #print("******** Contactos Cargados ******")
        while(contador < self.envergadura):
            #print("             "+str(contador+1)+ "."+ " "+nodo.obtener_nombre())
            nodo = nodo.siguiente
            self.listaContactos.append(nodo.obtener_nombre()+","+nodo.obtener_apellido()+","+str(nodo.obtener_telefono()))
            contador+=1
        #print("**********************************")

    def buscar_indice(self, indice):
        contador = 1
        nodo = self.cabeza
        while(contador!=int(indice)):
            nodo = nodo.siguiente
            contador +=1
        return nodo

    def obtener_tamano(self):
        return self.envergadura

