# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 05 - Repetição Controlada em Python > Questão 2:
# Faça um programa que imprima na tela apenas os números entre 1 e 50, quesejam múltiplos de um número X (entrada).

multiplo = int(input("Informe o número divisor: "))
print(f"Os múltiplos de {multiplo} (entre 1 e 50) são:")

for i in range(1, 51):
    if i % multiplo == 0:
        print(i, end=", ")