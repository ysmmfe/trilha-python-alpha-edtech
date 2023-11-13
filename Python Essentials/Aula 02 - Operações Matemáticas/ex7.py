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


print(f"O valor pode ser decomposto em {qntdNotas200} nota(s) de R$200, {qntdNotas100} nota de R$100, {qntdNotas50} nota de R$50, {qntdNotas20} nota(s) de R$20, {qntdNotas10} nota de R$10, {qntdNotas5} nota de R$5, {qntdNotas2} notas de R$2 e {qntdNotas1} nota de R$1")