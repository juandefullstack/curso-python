"""

-------------------------------------------------------------------
EJERCICIO 2 — Índice de masa corporal          (nuevo: DOS entradas)
-------------------------------------------------------------------
Pide el peso en kilos y la altura en metros. Muestra el IMC con 1 decimal.

    imc = peso / (altura * altura)

Salida esperada:

    Peso en kg: 74
    Altura en metros: 1.78
    Tu IMC es 23.4

Lo único nuevo: necesitas dos input(), porque ahora hay dos datos que
vienen de fuera. Sigue habiendo un solo bloque de cada tipo: entrada,
cálculo, salida.


.1f es para redondear a un decimal
"""

peso = float(input("¿Cuál es tu peso?:"))
altura = float(input("¿Y tu altura?:"))

imc = peso / (altura * altura)

print(f"Peso en kg: {peso:.0f}")
print(f"Altura en metros: {altura:.2f}")
print(f"Tu IMC es {imc:.1f}")