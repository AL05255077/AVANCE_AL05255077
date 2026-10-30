print("\n*** Nombre 1: mauricio de leon    Matricula: AL05255077    ***")
print("*** Nombre 2: alejandro urzais     Matricula:AL07293822     ***")
print("*** Nombre 3: santiago muñoz     Matricula:AL07287947     ***\n")

print("*** Ejercicio 4 TIENDA DE ACCESORIOS ***\n")

producto1 = input("Producto 1: ")
precio1 = float(input("Precio: "))
producto2 = input("Producto 2: ")
precio2 = float(input("Precio: "))
dinero = float(input("¿Cuánto dinero traes? "))

total = precio1 + precio2
print("Total de la compra: $", total, sep="")

if total > 300:
    descuento = total * 15 / 100
    total_final = total - descuento
    print("¡Tienes descuento! Pagas $", total_final, sep="")
else:
    total_final = total
    print("Sin descuento, te faltan $", 300 - total, " para llegar a $300", sep="")

if dinero >= total_final:
    print("Te alcanza, te sobran $", dinero - total_final, sep="")
else:
    print("No te alcanza, te faltan $", total_final - dinero, sep="")