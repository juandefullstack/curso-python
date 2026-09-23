"""
EJERCICIO 4 — Segundos a minutos                    (reto, hay algo nuevo)
-------------------------------------------------------------------
Pide un número de segundos y muéstralo en minutos y segundos.

Salida esperada:

    Segundos: 200
    Son 3 minutos y 20 segundos

Para esto te faltan dos herramientas que todavía no conoces. Descúbrelas
tú en el REPL antes de escribir nada. Abre python y prueba:

    >>> 200 / 60
    >>> 200 // 60
    >>> 200 % 60

Mira los tres resultados y deduce qué hace cada símbolo. Cuando lo tengas
claro, el ejercicio es inmediato.

(Si no lo sacas, dímelo — pero prueba primero.)
"""

segundos = int(input("segundos: "))

minutos = segundos // 60
segundos_restantes = segundos % 60

print(f"Son {minutos} minutos y {segundos_restantes} segundos")