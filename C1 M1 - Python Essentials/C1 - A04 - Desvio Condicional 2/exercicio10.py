# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 04 - Desvio Condicional 2 > Questão 10:
# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível.!!! Confira:
#                   Até 5kg	         Acima de 5kg
# Filé Duplo    R$ 5,80 por kg      R$ 4,90 por kg
# Alcatra	    R$ 6,80 por kg	    R$ 5,90 por kg
# Picanha	    R$ 7,80 por kg	    R$ 6,90 por kg
# Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a
# quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da
# compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações
# da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print(" > Use [F] para 'Filé Duplo', [A] para 'Alcatra' e [P] para 'Picanha'")
tipo = input("Informe o tipo de carne comprada: ")
quantidade = float(input("\nAgora informe a quantidade (em Kg): "))
print("\n > Use [0] para 'Dinheiro' e [1] para 'Cartão Tabajara'")
pagamento = input("Por fim, informe o método de pagamento: ")

if tipo == "F":
    if quantidade <=5:
        preco = 5.8 * quantidade
    else:
        preco = 4.9 * quantidade
        
if tipo == "A":
    if quantidade <=5:
        preco = 6.8 * quantidade
    else:
        preco = 5.9 * quantidade
        
if tipo == "P":
    if quantidade <=5:
        preco = 7.8 * quantidade
    else:
        preco = 6.9 * quantidade
        
if pagamento == "1":
    desconto = (5/100)*preco
    precoFinal = preco - desconto
    pagamento = "Cartão Tabajara"
else:
    desconto = 0
    precoFinal = preco - desconto
    pagamento = "Dinheiro"
    
linha1 = ["\nTipo", "Quantidade de carne", "Preço total", "Tipo de pagamento", "Valor do Desconto", "Valor a pagar"]
print("{:^6} {:>18} {:>14} {:>18} {:>18} {:>14}" .format(*linha1))

linha2 = [tipo, "%.2f" % quantidade, "%.2f" % preco, pagamento, "%.2f" % desconto, "%.2f" % precoFinal]
print("{:^4} {:>12} {:>19} {:>20} {:>12} {:>16}" .format(*linha2))