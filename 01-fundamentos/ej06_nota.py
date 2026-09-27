"""
Pide una nota del 0 al 10 y muestra la calificación:
menos de 5 → Suspenso · 5 a 6.9 → Aprobado · 7 a 8.9 → Notable · 9 o más → Sobresaliente
"""

nota = float(input("Dime que nota he sacado: "))

if nota < 5:
    print(f"{nota:.2f} Suspenso")
elif nota < 7:
    print(f"{nota:.2f} Aprobado")
elif nota < 9:
    print(f"{nota:.2f} Notable")
else:
    print(f"{nota:.2f} Sobresaliente")