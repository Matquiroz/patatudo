print("Registro de nota")

nombre = input("Ingrese nombre del estudiante: ")
nota = float(input("Ingrese nota final: "))

if nota >= 4.0:
    print("Aprobado")
else:
    print("Reprobado")

print("Estudiante:", nombre)
print("Nota final:", nota)
