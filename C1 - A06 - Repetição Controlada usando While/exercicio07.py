# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 7:
# Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível
# somente por ele mesmo e por 1.

num = int(input("Informe um número inteiro: "))

i = 2
primo = True # Assume inicialmente que o número é primo

if num == 2:
    print("O número 2 é um número primo! ")
elif num < 2:
    print(f"O número {num} não é um número primo")
else:
    while i <= num // 2:
        if num % i == 0:
            primo = False
            break
        i += 1
        
# Verifica se é primo ou não
if primo:
    print(f"O número {num} é um número primo!")
else:
    print(f"O número {num} não é um número primo.")