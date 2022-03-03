inversion = float(input("Ingrese el monto invertido: "))

telecomunicaciones = inversion * 0.10
sistemas = inversion * 0.25 
administracion = inversion * 0.35
contabilidad = inversion * 0.30

print(f"\nEl total invertido es: {inversion}$\nLos cuales serán invertidos de tal manera: \n")
print(f"Telecomunicaciones con el {10}%: {telecomunicaciones}$")
print(f"Sistemas con el {25}%: {sistemas}$")
print(f"Administración con el {35}%: {administracion}$")
print(f"Contabilidad con el {30}%: {contabilidad}$")
