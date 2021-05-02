from Lista.Nodo import Nodo

class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def vacia(self):
        return self.primero == None

    def incertar(self,fecha,usuario,afectado,codigo,error):
        if self.vacia():
            self.primero = self.ultimo = Nodo(fecha,usuario,afectado,codigo,error)
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(fecha,usuario,afectado,codigo,error)

    def retornarInfomacion(self):
        aux = self.primero
        datos = []
        while(aux != None):
            informacion = {"fecha":aux.fecha,"usuario":aux.usuario,"afectado":aux.afectado,"codigo":aux.codigo,"error":aux.error}
            datos.append(informacion)
            aux = aux.siguiente
        
        return datos

    def busqueda(self,dato1,dato2):
        aux = self.primero
        datos = []
        while(aux != None):

            if(aux.fecha == dato1 and aux.ususario == dato2) or (aux.fecha == dato1 and aux.usuario == dato2):
                informacion = {"fecha":aux.fecha,"usuario":aux.usuario,"afectado":aux.afectado,"codigo":aux.codigo,"error":aux.error}
                datos.append(informacion)
            else:
                return "Not Found"

            aux = aux.siguiente
        
        return datos
