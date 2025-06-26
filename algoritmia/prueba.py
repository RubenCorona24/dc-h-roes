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
    
#Modificamos algunos cambios de prueba
#Updatded: seguimos con el juego

vidas = 4
mapa = lugar
personaje = personaje1

print(f"Dentro de un {mapa} abandonado, se encontraba el personaje {personaje.name} explorando el lugar oscuro\nsin embargo, se encontró con algo que lo dejó paralizado")
print(f"el personaje tiene {vidas} vidas solamente")
print(f"Podrá sobrevivir {personaje.name} dentro de este lugar oscuro??")

class Zombie:
    def __init__(self,vida,daño,velocidad):
        self.vida = vida
        self.daño = daño
        self.velocidad = velocidad
    
    def __str__(self):
        return f"Vida: {self.vida} Daño: {self.daño} Velocidad: {self.velocidad}"
    def atacar(self):
        print("El zombie está atacando")
        personaje.vida - self.daño

    def correr(self):
        print(f"Zombie corre a velocidad de {self.velocidad} ")

zombie1 = Zombie(120,30,50)
personaje2 = Personaje('Andy',19,90)
fruta = choice(['manzana','plátano','sandía','uvas'])
objeto = choice(['libro antiguo','reliquia','reloj','brújula','roca antigua'])
print(f"{personaje2.name} se encontraba buscando su fruta favorita, la cual era {fruta}\nPero de pronto se encontro con algo extraño, un/a {objeto} ")

print(f"Entonces {personaje1.name} apenas había llegado a {lugar} para ver que sucedía, donde se encontró con {personaje2.name} ...continuará")
#A partir de ahora trabajao en otra rama llamda rama-juegos

class Animal:
    def __init__(self,raza,color):
        self.raza= raza
        self.color = color
        
    def __str__(self):
        return f"Este animal de raza {self.raza} es de color {self.color}"
    def hacer_sonido(self):
        pass
    def comer(self):
        print(f"El {self.raza} está comiendo")

animal1 = Animal('perro','marron')






