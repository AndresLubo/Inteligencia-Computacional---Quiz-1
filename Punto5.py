#CANTIDAD DE ALUMNOS DE CADA CLASE
aRedes = int(input("Ingrese la cantidad de alumnos de la clase de redes: "))
aContabilidad = int(input("Ingrese la cantidad de alumnos de la clase de contabilidad: "))
aDisenio = int(input("Ingrese la cantidad de alumnos de la clase de diseño: "))


#Alumnos totales 
aTotales = aRedes + aContabilidad + aDisenio

print(f"La cantidad de alumnos totales es: {aTotales}")
print(f"El porcentaje de estudiantes que pertenecen a Redes es: {round((aRedes * 100) / aTotales)}%")
print(f"El porcentaje de estudiantes que pertenecen a Contabilidad es: {round((aContabilidad * 100) / aTotales)}%")
print(f"El porcentaje de estudiantes que pertenecen a Diseño es: {round((aDisenio * 100) / aTotales)}%")
