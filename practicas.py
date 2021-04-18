#%% conversor de dolares a bolivianos
dolares = input("¿Cuantos tienes en Bs.?")
dolares = float(dolares)
valor_bs=6.9
dolares = dolares*valor_bs
dolares = round(dolares,2)
dolares = str(dolares)
print("Tienes "+dolares+" Bs.")

#%% termina en 7?
num = int(input("Termina en 7?:"))
if num%10==7:
    print("si")
else:
    print("no")

#%% serie fibonacci
n = int(input("cuantos numeros fibonacci?"))
a = 0
b = 1
for x in range(n):
    c = b+a
    a = b
    b = c    
    print (a)

#%% serie fibonacci con while
n = int(input("cuantos numeros fibonacci?"))
a = 0
b = 1
while n > 0:
    c = b+a
    a = b
    b = c
    n -= 1 
    print (a)

#%% tablas de multiplicar
for i in range(1, 11):
    for j in range(1, 11):
        print(j,"*",i,"=", i*j, end="\t")
    print("")
# %%
key = "contraseña"
password = input("Introduce la contraseña: ")
while key != password.lower():
    print("La contaseña no coincide")
#    break
# else:
#     print("La contraseña no coincide")
# %% diferencia entre tupla y lista tuplas
# sintaxis
tupla = (1,2)
lista = [1,2]
# no se puede eliminar un elemento de la tupla ni ordenarla
b    = [1,2]   
b[0] = 3    # [3, 2]
# 
a    = (1,2)
a[0] = 3    # Error 
# se puede agregar elementos a ambas pero la identificaion de la tupla cambia
a     = (1,2)
b     = [1,2]  
id(a)          # 140230916716520
id(b)          # 748527696
a   += (3,)    # (1, 2, 3)
b   += [3]     # [1, 2, 3]
id(a)          # 140230916878160
id(b)          # 748527696
# la lista es mutable pero no puede ser usada como clave en un diccionario, la tupla si
a    = (1,2)
b    = [1,2] 
c = {a: 1}     # OK
c = {b: 1}     # Error

# %% CLASE HOTEL
class Hotel:
     def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0
     def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

     def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes
     def ocupacion_total(self):
        return self.huespedes
    
hotel = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=20)    
hotel = Hotel(50, 20)
hotel.anadir_huespedes(3)
hotel.checkout(1)
hotel.ocupacion_total() # 2
print(hotel.huespedes) # 20

# %% clase alumno
#defino mi lista
alumnado = []

#defino una clase Alumno
class Alumno: 
# se inicia el constructor de instancias y propiedades de instancia
    
    def __init__(self, id_alumno, nombre, grado, alumnos):
        self.id_alumno = id_alumno      #incializo variables de instancia
        self.nombre = nombre            
        self.grado = grado            
        self.alumnos = alumnos
    
    def agregar(self, id_alumno, nombre, grado, alumnos):

        new_item = {
		    "id_alumno": id_alumno, 
		    "nombre": nombre,
		    "grado": grado
		    }

        self.alumnos.append(new_item)
        print('El Alumno ingresado es: ')
        print(
		    "\tid_alumno: ", id_alumno, "\n",
		    "\tnombre: ", nombre, "\n",
            "\tgrado: ", grado, "\n",
		    		)


    def mostrar(self, alumnos):    

        if len(alumnos) == 0:
            print('No existen alumnos en la lista')
        else:
            i = 0
            for dictionary in alumnos:
                i += 1
                print(f"Alumno #{i} :")
                print(
		    		"\tid_alumno: ", dictionary["id_alumno"], "\n",
		    		"\tnombre: ", dictionary["nombre"], "\n",
                    "\tgrado: ", dictionary["grado"], "\n",
		    		)
    
    def borrar(self, alumnos):
        OpcionBorrar = int(input('Ingrese el alumno a borrar: '))-1
        del alumnos[OpcionBorrar]

         
def Menu():

    while True:

        command = str(input('''
            ¿Que deseas hacer?

            [a]Añadir Alumno
            [b]Mostrar Alumnos
            [c]Eliminar Alumnos
            [s]Salir
        '''))

        alumnos = alumnado
        id_alumno = ''
        nombre = ''
        grado = ''
        matricular = Alumno(id_alumno,nombre,grado,alumnos)

        if  command.lower() == 'a':
            id_alumno = str(input('Escribe la identificacion del Alumno : '))
            nombre = str(input('Escribe el nombre del Alumno : '))
            grado = str(input('Escribe el grado academico: '))
            print('')
            matricular.agregar(id_alumno,nombre,grado,alumnos)

        elif command.lower() == 'b':
            matricular.mostrar(alumnos)

        elif command.lower() == 'c':
            matricular.borrar(alumnos)

        elif command.lower() == 's':
            break
        else:
            print('Comando no encontrado.')

if __name__ == '__main__':
    print()
    print('B I E N V E N I D O  A L  S I S T E M A  D E   M A T R I C U L A S')
    Menu()

# %%
