print("\n*** Nombre 1: mauricio de leon    Matricula: AL05255077    ***")
print("*** Nombre 2: alejandro urzais     Matricula:AL07293822     ***")
print("*** Nombre 3: santiago muñoz     Matricula:AL07287947     ***\n")

print("*** Ejercicio 4 MI META DE AHORRO ***\n")

producto = input("¿Qué quieres comprar? ")
precio = float(input("¿Cuánto cuestan? "))
ahorrado = float(input("¿Cuánto tienes ahorrado? "))
ahorro_semanal = float(input("¿Cuánto ahorras por semana? "))

if ahorrado >= precio:
    print("¡Ya puedes comprar tus", producto + "!")
else:
    faltante = precio - ahorrado
    semanas = faltante / ahorro_semanal
    print("Te faltan $", faltante, " para tus ", producto, sep="")
    print("Ahorrando $", ahorro_semanal, " por semana, los tendrás en ", semanas, " semanas", sep="")
    print("\n")