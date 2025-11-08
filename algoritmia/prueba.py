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
    def __init__(self,name,age,vida):
        self.name = name
        self.age = age
        self.vida = vida
    def __str__(self):
        return f"El personaje llamado {self.name} tiene {self.age} años"
    def explorar(self):
        print(f"{self.name} está explorando el lugar")

def contruir_personaje():
    name = input("Nommbre del personaje: ")
    age = int(input("años del personaje: "))
    vida = int(input("Salud del personaje: "))
    return Personaje(name,age,vida)

personaje1 = contruir_personaje()
print(personaje1)
print(personaje1.explorar())
##Hola, este es un mensaje desde GitHub 

class Animal(Personaje):
    def __init__(self, name, age,raza):
        super().__init__(name, age)
        self.raza = raza

    def hacer_sonido(self):
        print("El animal hace sonido")
    def comer(self):
        print("El animal está comiendo")

    def cazar(self):
        print("El animal está cazando su comida")
    def __str__(self):
        return f"El animal se llama {self.name} y tiene {self.age} años, es un {self.raza}"

animal1 = Animal('Sandy',19,'perro')
print(animal1)
animal2 = Animal('Violeta',3,'mono')
print(animal2)


print(f"De repente, el {animal2.raza} se encuentra con un {animal1.raza}, y entonc  s empiezan a jugar, el {animal1.raza} le pregunta como se llama. el {animal2.raza} le dice {animal2.name}, y tu?\n{animal1.name} dijo el {animal1.raza}")


