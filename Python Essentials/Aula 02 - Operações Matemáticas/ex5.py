nome = input("Informe o seu nome: ")
salariofixo = float(input("Informe o seu salário: "))
totalvendas = int(input("Informe o total em dinheiro das vendas efetuadas no mês: "))

comissao = (5/100) * totalvendas
salariototal = salariofixo + comissao

print(f"\n{nome} vai receber R${salariototal:.2f} no fim do mês")