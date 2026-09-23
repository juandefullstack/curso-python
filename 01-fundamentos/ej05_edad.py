"""
Pide la edad al usuario. Si es mayor o igual a 18, muestra "Puedes pasar". Si no, muestra cuántos años le faltan: "Te faltan 3 años".
"""

edad = int(input("¿Qué edad tienes? "))

if edad >= 18:
    print("Puedes pasar")
else:
    anios_restantes = 18 - edad
    print(f"Te faltan {anios_restantes} años")