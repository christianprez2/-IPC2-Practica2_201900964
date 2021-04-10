class Nodo:
    def __init__(self, nombre = "", apellido = "", telefono = 0):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.siguiente = None
        self.anterior = None

    def obtener_nombre(self):
        return self.nombre

    def obtener_apellido(self):
        return self.apellido

    def obtener_telefono(self):
        return self.telefono
    
    def obtener_siguiente(self):
        return self.siguiente

    def obtener_anterior(self):
        return self.anterior