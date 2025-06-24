print("Esto es una prueba .py")
from random import *
num = randint(1,1000)
print(f"El número seleccionado es: {num}")
opcion = input("Estás convencido con tu número? (N/S): ")
if opcion == 'N':
    print("Vale, se te asignará otro número")
    new_num = randint(1,1000)
    print(f"Tu nuevo número es: {new_num}")
elif opcion == 'S':
    print("Que bueno que te gusto tu número, a partir de ella jugaras con el asignado")
else:
    print("Opción No Válida")
lugares = ['parque','hospital','casa','museo','bosque','playa']
def asignar_area(*lugares):
    area = choice(lugares)
    return area

lugar = asignar_area(lugares)
print(f"Nuestro mapa cuenta con {len(lugares)} areas, los cuales son: {lugares}, el lugar SELECCIONADO es: {lugar}")
class Personaje:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"El personaje llamado {self.name} tiene {self.age} años"
    def explorar(self):
        print(f"{self.name} está explorando el lugar")

def contruir_personaje():
    name = input("Nommbre del personaje: ")
    age = int(input("años del personaje: "))
    return Personaje(name,age)

personaje1 = contruir_personaje()
print(personaje1)
    
#Modificamos algunos cambios de prueba