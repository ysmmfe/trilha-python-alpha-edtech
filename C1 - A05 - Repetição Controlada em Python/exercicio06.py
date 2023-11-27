# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 6:
# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. Além do valor do
# fatorial, responda quantos zeros tem no final do número resultado

# Obtendo o fatorial a ser calculado
fac = int(input("Informe um número: "))
print(f"O fatorial de {fac} é:", end=" ")

# Calculando o fatorial e imprimindo na tela
for i in range((fac-1), 0, -1):
    fac = fac * i

print(fac)
zero = 0

# Contando a quantidade de zeros no final do fatorial
for x in reversed(str(fac)):
    if x == '0':
        zero = zero + 1
    else:
        break
    
print(f"O número {fac} tem {zero} zero(s) no final")