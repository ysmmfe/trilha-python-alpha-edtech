# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 04 - Questão 7:
# Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são: "Telefonou para a vítima?", "Esteve no local
# do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?". O programa deve no final emitir uma
# classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada
# como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente”.

print(" > Use [0] para 'não' e [1] para 'sim':")
classificacao = 0

pergunta1 = int(input("Telefonou para a vítima? "))
if pergunta1 == 1:
    classificacao = classificacao + 1
    
pergunta2 = int(input("Esteve no local do crime? "))
if pergunta2 == 1:
    classificacao = classificacao + 1
    
pergunta3 = int(input("Mora perto da vítima? "))
if pergunta3 == 1:
    classificacao = classificacao + 1
    
pergunta4 = int(input("Devia para a vítima? "))
if pergunta4 == 1:
    classificacao = classificacao + 1
    
pergunta5 = int(input("Já trabalhou com a vítima? "))
if pergunta5 == 1:
    classificacao = classificacao + 1

if classificacao==5:
    resultado = "Culpado"
else:
    if classificacao >=3:
        resultado = "Cúmplice"
    else:
        if classificacao >=2:
            resultado = "Suspeita"
        else:
            resultado = "Inocente"

print("\nA sua classificação é: ", resultado)