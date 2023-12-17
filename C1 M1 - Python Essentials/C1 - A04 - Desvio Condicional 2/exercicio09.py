# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 04 - Desvio Condicional 2 > Questão 9:
# Uma frutaria está vendendo frutas com a seguinte tabela de preços:
#           Até 5kg	            Acima de 5kg
# Morango   R$ 2,50 por kg      R$ 2,20 por kg   
# Maçã	    R$ 1,80 por kg	    R$ 1,50 por kg
# Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre
# este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor
# a ser pago pelo cliente.

morango = float(input("Informe a quantidade (em Kg) de morangos adquiridos: "))
maca = float(input("Informe a quantidade (em Kg) de maçãs adquiridas: "))

if morango <=5:
    precoMorango = 2.5 * morango
else:
    precoMorango = 2.2 * morango
    
if maca <=5:
    precoMaca = 1.8 * maca
else:
    precoMaca = 1.5 * maca

total = precoMaca+precoMorango
if (maca+morango) > 8 or total > 25:
    total = total - ((10/100)*total)
    
print(f"\n\tO valor a ser pago pelo cliente é de R${total:.2f}")