# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 7:
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível
# somente por ele mesmo e por 1.

num = int(input("Informe um número inteiro: "))

i = 2
if num == 2:
    print("O número 2 é um número primo! ")

while i <= num:
    if num%i==0:
        print(f"O número {num} não é um número primo")
        break
    else:
        print(f"O número {num} é um número primo!")
        break
i += 1