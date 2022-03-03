inversion1 = float(input("Ingrese el valor de la inversión de la persona 1: "))
inversion2 = float(input("Ingrese el valor de la inversión de la persona 2: "))
inversion3 = float(input("Ingrese el valor de la inversión de la persona 3: "))


inversionTotal = inversion1 + inversion2 + inversion3

print(f"\nEl total de la inversión es: {inversionTotal}\n")
print(f"La persona 1 invirtió: {inversion1}$\nLo que corresponde a un: {round((inversion1 * 100) / inversionTotal)}% de la inversión")
print(f"La persona 2 invirtió: {inversion2}$\nLo que corresponde a un: {round((inversion2 * 100) / inversionTotal)}% de la inversión")
print(f"La persona 3 invirtió: {inversion3}$\nLo que corresponde a un: {round((inversion3 * 100) / inversionTotal)}% de la inversión")
