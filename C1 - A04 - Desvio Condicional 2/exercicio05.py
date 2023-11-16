# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 04 - Questão 5:
# Faça um programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

# Utilizando apenas divisão inteira
numero = float(input("Digite um número: "))

if numero//1 == numero:
    print(f"{int(numero)} é um número inteiro!")
else:
    print(f"{numero} é um número decimal!")

# Utilizando a função de arredondamento
num = float(input("Digite um número: "))

if num == round(num):
    print("O número é inteiro")
else:
    print("O número é decimal")