name = input("Ingrese el nombre:")
print (name.upper())
longitud_sin_espacios = len(name.replace(" ",""))
print (f"El nombre tiene {longitud_sin_espacios} elementos")
print(name.replace(" ",""))