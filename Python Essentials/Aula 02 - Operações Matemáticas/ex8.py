import math

a = float(input("Informe um número diferente de 0: "))
b = float(input("Agora informe outro número real: "))
c = float(input("Agora informe outro número real: "))
x = float(input("Agora informe outro número real: "))

delta = b**2 - 4*a*c
bhaskara = (-b + math.sqrt(delta)) / (2 * a)
bhaskara2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"\nAs raízes possíveis de x são {bhaskara:.1f} e {bhaskara2:.1f}, já o valor de x informado foi {x}")