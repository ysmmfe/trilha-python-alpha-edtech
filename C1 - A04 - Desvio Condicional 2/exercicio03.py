# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 04 - Questão 3:
# Faça um programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
# quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 2, 5, 10, 20, 50, 100 e 200 reais.
# O valor mínimo é de 10 reais e o máximo de 1000 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

valor = float(input("Informe o valor do saque: R$"))

if 10 <= valor <1000:
    if valor%2==0:
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
        
        qntdNotas2 = resto//2
        qntdNotas1 = resto%2
        
        print(f"\nSerão fornecidas: \n{int(qntdNotas200)} nota(s) de R$200\n{int(qntdNotas100)} nota de R$100\n{int(qntdNotas50)} " + 
              f"nota de R$50\n{int(qntdNotas20)} nota(s) de R$20\n{int(qntdNotas10)} nota de R$10\n{int(qntdNotas2)} notas de R$2")
    else:
        valor = valor - 5
        qntdNotas5 = 1
        
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
        
        qntdNotas2 = resto//2
        qntdNotas1 = resto%2
        
        print(f"\nSerão fornecidas:\n{int(qntdNotas200)} nota(s) de R$200\n{int(qntdNotas100)} nota de R$100\n{int(qntdNotas50)} " + 
              f"nota de R$50\n{int(qntdNotas20)} nota(s) de R$20\n{int(qntdNotas10)} nota de R$10\n{int(qntdNotas5)} nota de R$5\n{int(qntdNotas2)} notas de R$2")
else:
    if valor < 10 :
        print("Você não atingiu o valor mínimo para o saque!")
    else:
        print("Você ultrapassou o valor máximo para o saque!")