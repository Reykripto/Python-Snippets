# nivel de ph
ph = int(input("Ingrese el valor del ph 0 a 14: "))
if ph > 7:
    print(f"Basico")
elif ph < 7:
    print(f"Acido")
else:    
    print(f"Neutro")
