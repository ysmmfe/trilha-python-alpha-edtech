# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 04 - Desvio Condicional 2 > Questão 6:
# Faça um programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve
# ser acompanhado de uma frase que diga se o número é: par ou ímpar; positivo ou negativo; inteiro ou decimal.

num1 = float(input("Informe o primeiro número: "))
num2 = float(input("Informe o segundo número: "))
operacao = input("Qual operação deseja utilizar? [+, -, *, /] -> ")
resultado = 0

if operacao=="+":
    resultado = num1 + num2
else:
    if operacao=="-":
        resultado = num1 - num2
    else:
        if operacao=="*":
            resultado = num1 * num2
        else:
            if operacao=="/":
                resultado = num1/num2
            else:
                print("Essa não é uma operação válida!")
                
print("\nO resultado da operação é: ", resultado)

if resultado%2==0:
    print("Esse resultado é par")
else:
    print("Esse resultado é ímpar")
    
if resultado>=0:
    print("Esse resultado é positivo")
else:
    print("Esse resultado é negativo")
    
if resultado//1==resultado:
    print("Esse resultado é inteiro")
else:
    print("Esse resultado é decimal")