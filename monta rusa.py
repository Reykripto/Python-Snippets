# roller_coaster
height = int(input("Ingrese altura: "))
credits = int(input("Ingrsese Creditos: "))

if height > 137 and credits > 10:
  print(f"Disfruta el Viaje!")
elif height < 137:
  print(f"No tienes la altura necesaria!")
elif credits < 10:
  print(f"No tienes creditos suficientes!")
else:
  print(f"datos invalidos.")