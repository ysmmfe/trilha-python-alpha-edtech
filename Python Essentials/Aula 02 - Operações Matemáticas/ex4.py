import math

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
x = float(input("Agora informe o primeiro ponto flutuante: "))
y = float(input("Informe o segundo ponto flutuante: "))

expressao = a + b * x - math.sqrt(b) + ((a+b) / (x-y))

print(f"O resultado da expressão é {expressao:.2f}")