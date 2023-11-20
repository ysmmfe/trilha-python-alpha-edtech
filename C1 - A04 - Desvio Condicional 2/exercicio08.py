# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 04 - Questão 8:
# Um posto está vendendo combustíveis com a seguinte tabela de descontos:
# Álcool: até 20 litros, desconto de 3% por litro. Acima de 20 litros, desconto de 5% por litro
# Gasolina: até 20 litros, desconto de 4% por litro. Acima de 20 litros, desconto de 6% por litro
# Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina),
# calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$2,50 o preço do litro do álcool é R$1,90

litros = float(input("Informe o número de litros vendidos: "))
print("\n > Use [A] para 'Álcool' e [G] para 'Gasolina':")
combustivel = input("Agora informe o tipo de combustível: ")

if combustivel=="A":
    preco = 1.9 * litros
    if litros<=20:
        preco = preco - ((3/100)*litros)
    else:
        preco = preco - ((5/100)*litros)
        
if combustivel=="G":
    preco = 2.5 * litros
    if litros<=20:
        preco = preco - ((4/100)*litros)
    else:
        preco = preco - ((6/100)*litros)

print(f"\nO valor a ser pago pelo cliente é de R${preco:.2f}")