"""
EJERCICIO 1 — Conversor de temperaturas
=======================================

Escribe TÚ todo el código de este fichero. Está vacío a propósito.

QUÉ DEBE HACER EL PROGRAMA
--------------------------
1. Pedir al usuario una temperatura en grados Celsius.
2. Mostrar esa temperatura convertida a Fahrenheit y a Kelvin.
3. Los dos resultados deben salir con UN solo decimal.

Ejemplo exacto de cómo debe verse al ejecutarlo:

    Introduce los grados Celsius: 23.5
    23.5 °C son 74.3 °F
    23.5 °C son 296.6 K

FÓRMULAS
--------
    fahrenheit = celsius * 9 / 5 + 32
    kelvin     = celsius + 273.15

REGLAS
------
- Sin importar ninguna librería.
- Nada de copiar y pegar: escríbelo tú, letra a letra.
- Si algo falla, LEE el mensaje de error entero antes de tocar nada.

PISTAS (solo si te atascas)
---------------------------
- input() sirve para pedir datos. Devuelve SIEMPRE texto, nunca un número.
- float("23.5") convierte ese texto en un número decimal.
- Las f-strings formatean texto:  f"Hola {nombre}"
- Para un decimal:  f"{valor:.1f}"

RETOS EXTRA (opcionales, intenta al menos el primero)
-----------------------------------------------------
A) Que el programa no se rompa si escribo "hola" en vez de un número.
B) Que si la temperatura está por debajo de -273.15 °C avise de que
   eso es físicamente imposible y no muestre conversión.

Cuando lo tengas funcionando, dímelo y lo reviso línea a línea.
"""

# Tu código empieza aquí:

celsius = float(input("Introduce los grados Celsius: "))

fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15

print(f"{celsius} ºC son {fahrenheit:.1f} ºF")
print(f"{celsius} ºC son {kelvin:.1f} K")