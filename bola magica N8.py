# bola magica N8
import random
Preguntar = str(input("Ingrese su pregunta: "))
respuesta = random.randint(1, 9)
if respuesta == 1: 
    print(f"Si definitivamente!")
elif respuesta == 2:
    print(f"Esta decidido!")
elif respuesta == 3:
    print(f"Sin duda!")
elif respuesta == 4:
    print(f"No lo se, Intenta de Nuevo!")
elif respuesta == 5:
    print(f"Mejor no te Digo!")
elif respuesta == 6:
    print(f"Mis Fuentes Dicen que No!")
elif respuesta == 7:
    print(f"No se ve Bien!")
elif respuesta == 8:
    print(f"Muy dudoso!")
elif respuesta == 9:
    print(f"Vuelve a Preguntar!")