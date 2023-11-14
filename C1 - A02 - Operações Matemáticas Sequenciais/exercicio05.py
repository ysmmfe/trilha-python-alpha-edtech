# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 5:
# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). 
# Sabendo que este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês,
# com duas casas decimais.

nome = input("Informe o seu nome: ")
salariofixo = float(input("Informe o seu salário: "))
totalvendas = int(input("Informe o total em dinheiro das vendas efetuadas no mês: "))

comissao = (5/100) * totalvendas
salariototal = salariofixo + comissao

print(f"\n{nome} vai receber R${salariototal:.2f} no fim do mês")