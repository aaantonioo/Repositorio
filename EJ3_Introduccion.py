class Rectangulo:
    def __init__(self,x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def perimeto(self):
        return self.x1 + self.x2 + self.y1 + self.y2
    def area(self):
        return self.x1 * self.y1
    

objeto1 = Rectangulo(0,0,5,5)
objecto2 = Rectangulo(7,9,2,3)

print("Las cordenadas del objeto1 son: ", objeto1.x1, objeto1.y1, objeto1.x2, objeto1.y2)
print("Las cordenadas del objeto2 es: ", objecto2.x1, objecto2.y1, objecto2.x2, objecto2.y2 )
print("La suma de sus lados del objeto1 es: ",objeto1.perimeto())
print("La suma de sus lados del objeto2 es: ",objecto2.perimeto())
print("El area del objeto1 es de ", objeto1.area())
print("El are del objeto2 es de: ", objecto2.area())
