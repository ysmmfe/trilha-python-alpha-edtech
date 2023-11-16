# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 04 - Questão 4:
# Faça um Programa que peça um número inteiro e determine se ele é par ou ímpar. Dica: utilize o operador módulo (resto da divisão).

num = int(input("Informe um número inteiro: "))

if num%2 ==0 :
    print(f"O número {num} é par!")
else:
    print(f"O número {num} é ímpar!")