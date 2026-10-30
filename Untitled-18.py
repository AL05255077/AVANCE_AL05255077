print("\n*** Nombre 1: mauricio de leon    Matricula: AL05255077    ***")
print("*** Nombre 2: alejandro urzais     Matricula:AL07293822     ***")
print("*** Nombre 3: santiago muñoz     Matricula:AL07287947     ***\n")

print("*** Ejercicio 15 Rango en tu videojuego ***\n")

# int() convierte el texto a número entero para poder comparar y hacer cuentas
puntos = int(input("\n¿Cuántos puntos tienes? "))
# Si el usuario escribe 2500, ahora puntos vale 2500

print("\n===== TU RANGO =====")

# Empezamos por el rango MÁS ALTO
# ¿2500 es mayor o igual que 3000? False, pasa a la siguiente
if puntos >= 3000:
    print("Rango: DIAMANTE")
    print("¡Ya estás en el rango máximo!")

# ¿2500 es mayor o igual que 2000? True, entra aquí y TERMINA
elif puntos >= 2000:
    # Esta fórmula dice: faltan = 3000 - 2500
    faltan = 3000 - puntos
    # Ahora faltan vale 500
    print("Rango: ORO")
    print(f"Te faltan {faltan} puntos para Diamante")

elif puntos >= 1000:
    faltan = 2000 - puntos
    print("Rango: PLATA")
    print(f"Te faltan {faltan} puntos para Oro")

# else: tiene menos de 1000
else:
    faltan = 1000 - puntos
    print("Rango: BRONCE")
    print(f"Te faltan {faltan} puntos para Plata")
    