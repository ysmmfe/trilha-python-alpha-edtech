import math

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))

volume = a*b*c
diagonal = math.sqrt(a**2 + b**2 + c**2)

print(f"\nO volume do paralelepípedo é: {volume:.2f}")
print(f"A diagonal principal do paralelepípedo é: {diagonal:.2f}")