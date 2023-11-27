# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 6:
# A série de Fibonacci é formada pela seqüência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Onde cada número é a soma dos 2 anteriores da
# série. Faça um programa que gere a série até que o valor seja maior que 500.

anterior = 0
atual = 1
soma = anterior + atual

print("A Série de Fibonacci (até 500) é: ")
print(f"{anterior}, {atual},", end=" ")

while soma < 500:
    anterior = atual
    atual = soma
    print(atual, end=", ")
    soma = anterior + atual