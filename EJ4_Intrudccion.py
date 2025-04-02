class Articulo:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.iva = 21
        self.stock = 100
    
    def __str__(self):
        return str(f"{self.nombre} ") + str(f"Precio: {self.precio}€ ") +str(f"IVA: {self.iva}% ")
    
    def incrementar_stock(self,cantidad):
        #self.cuantos_quedan += cantidad
        pass
    
    def vender(self, cantidad):
        if cantidad > self.stock:
            print("No hay stock")
        return self.stock == self.stock - cantidad


def main():
    lista_objetos= []
    seguir = ""
    while seguir != "no":
        nombre_articulo = str(input("Dime el nombre del articulo: "))
        precio = int(input("Dime el precio del articulo: "))
        #cantidad = int("Dime la cantidad que te quieres llevar: ")
        objeto1 = Articulo(nombre_articulo,precio)
        #objeto1.vender(cantidad)
        lista_objetos.append(objeto1)
        
        seguir = input("¿Quieres seguir añadiendo objetos?: ").lower()
    
    seguir2 = ""
    while seguir2 != "no":

        for elemento in lista_objetos:
            print (elemento)

        posicion = int(input("Cual quieres comprar: "))
        cuantos = int(input("Cuantos quieres comprar: "))
        lista_objetos[posicion].vender(cuantos)
        seguir2 = input("¿Quieres seguir comprando?: ")



main()