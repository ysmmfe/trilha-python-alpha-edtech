# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 08 - Questão 2:
# Crie um programa que leia o arquivo gerado no exercício anterior e armazenar em um vetor de números inteiros (array ou List de inteiros).
# O programa deve calcular sem usar funções prontas e imprimir: o valor médio, o valor máximo, o valor mínimo, os 5 primeiros valores e os
# últimos 5 valores. Se houver algum valor menor ou igual a zero, que é um valor impossível, o seu programa deve substituir esse valor pela
# média calculada (portanto, os valores faltantes ou inválidos não devem ser utilizados nos cálculos de média, mínimo, máximo). Armazenar
# em outro arquivo o vetor novo sem valores inválidos.

import ast

soma = 0
maximo = None
minimo = None
total_valido = 0

# 1. Lendo o arquivo que contém a lista gerada no exercício anterior
with open("arquivo.txt", "r") as arquivo:
    mensagem = ast.literal_eval(arquivo.read()) # função para executar expressões literais com mais segurança

# 2. Achando os valores válidos (>0), somando o total e calculando maior e menor valor
for i in range(0, len(mensagem)):
    if mensagem[i] > 0:
        soma += mensagem[i]
        if maximo is None or mensagem[i] > maximo:
            maximo = mensagem[i]
        elif minimo is None or mensagem[i] < minimo:
            minimo = mensagem[i]
        total_valido += 1

media = int(soma/total_valido)

# 3. Substituindo os valores negativos pela média dos valores válidos
for i in range(len(mensagem)):
    if mensagem[i] < 0:
        mensagem[i] = media

# 5. Separando os 5 primeiros e os 5 últimos valores da lista
primeiros_valores = mensagem[:5]    # Interessante criar um for para imprimir os números fora da lista,
ultimos_valores = mensagem[-5:]     # talvez em uma modificação futura.
    
# 6. Armazenando a lista de valores válidos em um arquivo
with open("novo_arquivo.txt", "w") as arquivo2:
    arquivo2.write(str(mensagem))

print(f"O valor médio da lista é: {media}")
print(f"O maior valor da lista é: {maximo}")
print(f"O menor valor da lista é: {minimo}")
print(f"Os 5 primeiros valores são: {primeiros_valores}")
print(f"Os 5 últimos valores são: {ultimos_valores}")