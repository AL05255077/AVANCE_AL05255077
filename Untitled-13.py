print("\n*** Nombre 1: mauricio de leon    Matricula: AL05255077    ***")
print("*** Nombre 2: alejandro urzais     Matricula:AL07293822     ***")
print("*** Nombre 3: santiago muñoz     Matricula:AL07287947     ***\n")

print("*** Ejercicio 3 WI-FI DEL CAFÉ ***\n")

contrasena_cafe = "Latte2026"

nombre = input("¿Cómo te llamas? ")
contrasena = input("Escribe la contraseña: ")
gasto = float(input("¿Cuánto gastaste? "))

if contrasena == contrasena_cafe:
    print("Conectado al Wi-Fi, bienvenida", nombre)
else:
    print("Contraseña incorrecta")

if gasto >= 100:
    print("Tienes 1 horas de Wi-Fi\n")
else:
    print("Tienes 30 minutos de Wi-Fi\n")