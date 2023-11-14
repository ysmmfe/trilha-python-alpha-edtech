# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 4:
# Leia dois números inteiros a, b, e dois números em ponto flutuante x, y. Então calcule a expressão: 
# a + bx – sqrt(b) + ( (a+b) / (x-y) ), atribuindo o resultado à variável expressao. A seguir, mostre
# a variável expressão com a mensagem correspondente. A saída deve imprimir duas casas decimais.

import math

a = int(input("Informe o primeiro número: "))
b = int(input("Informe o segundo número: "))
x = float(input("Agora informe o primeiro ponto flutuante: "))
y = float(input("Informe o segundo ponto flutuante: "))

expressao = a + b * x - math.sqrt(b) + ((a+b) / (x-y))

print(f"O resultado da expressão é {expressao:.2f}")