class Persona:
    def __init__(self, dni, nombre, apellidos, edad):
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
    


dni = str(input("Dime el dni de la persona: "))
nombre = str(input("Dime el nombre de la persona: "))
apellidos = str(input("Dime los apellidos: "))
edad = int(input("Dime la edad de la persona: "))

obejto1 = Persona(dni,nombre, apellidos,edad)


print(f"{obejto1.nombre},{obejto1.apellidos} con DNI:{obejto1.dni} no es mayor de edad ")
