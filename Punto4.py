#Notas de los talleres 
taller1 = float(input("Ingrese la nota del taller 1: "))
taller2 = float(input("Ingrese la nota del taller 2: "))
taller3 = float(input("Ingrese la nota del taller 3: "))

#Nota de examen
examen = round(float(input("Ingrese la nota del Examen: ")))

#Nota del proyecto
pFinal = round(float(input("Ingrese la nota del Proyecto final: ")))


notaTalleres = round((taller1 + taller2 + taller3) / 3)

notaFinal = (notaTalleres * 0.50) + (examen * 0.30) + (pFinal * 0.20)

print(f"\nSu nota de talleres es: {notaTalleres}")
print(f"Su nota de examen es: {examen}")
print(f"Su nota de proyecto final es: {pFinal}")
print(f"Su nota final es: {notaFinal}")
