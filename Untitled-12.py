print("\n*** Nombre 1: mauricio de leon    Matricula: AL05255077    ***")
print("*** Nombre 2: alejandro urzais     Matricula:AL07293822     ***")
print("*** Nombre 3: santiago muñoz     Matricula:AL07287947     ***\n")

print("*** Ejercicio 2 CREA TU CUENTA ***\n")

nombre = input("¿Cómo te llamas? ")
anio = int(input("¿En qué año naciste? "))
red_social = input("¿Cuál es tu red social favorita? ")

edad = 2026 - anio
print(nombre + ", tienes", edad, "años")

if edad >= 13:
    print("Tu cuenta en", red_social, "fue creada")
else:
    print("Todavía no puedes crear tu cuenta, te faltan", 13 - edad, "años")

if edad >= 18:
    print("Compras dentro de la app activadas\n")
else:
    print("Compras dentro de la app desactivadas\n")