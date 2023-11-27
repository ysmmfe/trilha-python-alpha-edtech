# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 4:
# Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número.
# Não utilize a função de potência da linguagem.

base = int(input("Informe a base: "))
expoente = int(input("Agora informe o expoente: "))
mult = 1

for i in range(1, (expoente+1)):
    mult = mult * base
print(f"\nA potência {base}^{expoente} é = {mult}")