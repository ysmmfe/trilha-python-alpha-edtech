# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 5:
# A série de Fibonacci é formada pela sequência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um programa que gere a série até que o valor
# seja maior que 500.

anterior = 0
atual = 1
soma = anterior + atual

print("A Série de Fibonacci (até 500) é: ")
print(f"{anterior}, {atual},", end=" ")

for i in range(1,20):
    anterior = atual
    atual = soma
    if atual <500:
        print(atual, end=", ")
    soma = anterior + atual