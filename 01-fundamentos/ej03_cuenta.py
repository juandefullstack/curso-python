"""
EJERCICIO 3 — Cuenta del restaurante        (tres entradas, dos cálculos)
-------------------------------------------------------------------
Pide el importe de la cuenta, el porcentaje de propina y el número de
comensales. Muestra el total con propina y lo que paga cada uno.

Salida esperada:

    Importe de la cuenta: 86.40
    Porcentaje de propina: 10
    ¿Cuántos sois?: 3
    Total con propina: 95.04 €
    Cada uno paga: 31.68 €

Ojo con el número de comensales: ¿tiene sentido que sea 2.5 personas?
Elige la conversión adecuada y piensa por qué.
"""

cuenta = float(input("Importe de la cuenta: "))
porcentaje_propina = float(input("Porcentaje de propina: "))
personas = int(input("¿Cuántos sois?: "))

fraccion_propina = porcentaje_propina / 100
euros_propina = cuenta * fraccion_propina
total_con_propina = cuenta + euros_propina
por_persona = total_con_propina / personas

print(f"Total con propina: {total_con_propina:.2f} €")
print(f"Cada uno paga: {por_persona:.2f} €")