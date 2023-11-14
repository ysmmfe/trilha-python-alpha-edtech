# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 7:
# Faça um programa que leia um valor inteiro representando um valor em reais e calcule o menor número de cédulas possíveis no qual o
# valor pode ser decomposto. As cédulas consideradas são as de R$200.00, R$100.00, R$50.00, R$20.00, R$10.00, R$5.00, R$2.00 e R$1.00. 
# Seu programa deve imprimir a quantidade de cada cédula. Dica: divisão inteira usa // e resto da divisão usa %
# Assim valor total R$ 1317,00 quantas notas de R$ 200,00. qtdNotas200 = valorTotal // 200 resulta 6 notas de 200
# e agora o resto seria restoValor = valorTotal % 200, que resulta 117

valor = int(input("Informe um valor em reais: "))

qntdNotas200 = valor//200
resto = valor%200

qntdNotas100 = resto//100
resto = resto%100

qntdNotas50 = resto//50
resto = resto%50

qntdNotas20 = resto//20
resto = resto%20

qntdNotas10 = resto//10
resto = resto%10

qntdNotas5 = resto//5
resto = resto%5

qntdNotas2 = resto//2
qntdNotas1 = resto%2

print(f"O valor pode ser decomposto em {qntdNotas200} nota(s) de R$200, {qntdNotas100} nota de R$100, {qntdNotas50} nota de R$50 " +
      f"{qntdNotas20} nota(s) de R$20, {qntdNotas10} nota de R$10, {qntdNotas5} nota de R$5, {qntdNotas2} notas de R$2 e {qntdNotas1} " +
      "nota de R$1")