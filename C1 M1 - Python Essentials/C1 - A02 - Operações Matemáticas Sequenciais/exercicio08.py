# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 02 - Operações Matemáticas Sequenciais > Questão 8:
# Faça um programa que leia quatro números reais a ≠ 0, b, c, x. 
# Verificar a fórmula de Bháskara, se o valor de x é uma das raízes da equação a.x²+b.x+c=0.
# Observação: suponha que a, b e c são tais que b² - 4ac >= 0

import math

a = float(input("Informe um número diferente de 0 (a): "))
b = float(input("Agora informe outro número real (b): "))
c = float(input("Agora informe outro número real (c): "))
x = float(input("Agora informe outro número real (x): "))

delta = b**2 - 4*a*c
bhaskara = (-b + math.sqrt(delta)) / (2 * a)
bhaskara2 = (-b - math.sqrt(delta)) / (2 * a)

print(f"\nAs raízes possíveis de x são {bhaskara:.1f} e {bhaskara2:.1f}, já o valor de x informado foi {x}")