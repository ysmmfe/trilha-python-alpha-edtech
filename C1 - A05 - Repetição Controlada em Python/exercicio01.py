# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 1:
# Faça um programa que que leia 5 números e informe o maior número. Faça o mesmo programa informar a soma e a média dos números.

maior = None
soma = 0

for i in range(1, 6):
    num = float(input(f"Informe o {i}° número: "))
    soma = soma + num
    if maior is None or num > maior:
        maior = num

media = soma/5

print("\nO maior número é: ", maior)
print(f"A soma dos números informados é: {soma:.2f}")
print(f"A média dos números informados é: {media:.2f}")