# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 02 - Operações Matemáticas Sequenciais > Questão 2:
# Faça um programa que leia os comprimentos dos 3 lados a, b, c de um paralelepípedo. Então calcule o seu volume e sua diagonal principal
# dados pelas seguintes expressões, respectivamente:
# V = a . b . c
# d = sqrt (a2 + b2 + c2), sendo sqrt a função raiz quadrada da biblioteca math atribuindo os resultados às variáveis V e d.
# A seguir, apresente as variáveis com as mensagens correspondentes. A saída deve imprimir duas casas decimais. 

import math

a = int(input("Informe o lado a: "))
b = int(input("Informe o lado b: "))
c = int(input("Informe o lado c: "))

volume = a*b*c
diagonal = math.sqrt(a**2 + b**2 + c**2)

print(f"\nO volume do paralelepípedo é: {volume:.2f}")
print(f"A diagonal principal do paralelepípedo é: {diagonal:.2f}")