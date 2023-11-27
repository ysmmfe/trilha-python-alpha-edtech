# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 08 - Questão 3:
# Crie um programa que leia o arquivo gerado no exercício anterior e armazenar em um vetor de números inteiros (array ou List de inteiros).
# O programa deve calcular (agora usando chamadas de funções prontas em bibliotecas) e imprimir: o valor médio, mediana, o valor máximo, o
# valor mínimo, valor da amplitude, os 5 primeiros valores e os últimos 5 valores, desvio padrão e variância. Explicar sucintamente  cada
# um desses dos valores (em 2 linhas no máximo para cada valor, colocar isso no “print” para esclarecer ao usuário que usar seu programa).

import ast
import statistics

# 1. Lendo o arquivo que contém a lista gerada no exercício anterior
with open("novo_arquivo.txt", "r") as arquivo:
    mensagem = ast.literal_eval(arquivo.read()) # função para executar expressões literais com mais segurança

# 2. Calculando a média de acordo com a função da biblioteca
media = statistics.mean(mensagem)
print(f"> {media} é o valor da média aritmética, ou seja, a razão entre todos os valores e a quantidade de valores")

# 3. Calculando a mediana de acordo com a função da biblioteca
print(f"> {statistics.median(mensagem)} é o valor da mediana, ou seja, o valor que se encontra no meio dos dados em ordem crescente")

# 4. Calculando o valor máximo de acordo com a função max()
print(f"> {max(mensagem)} é o valor máximo, ou seja, é o maior valor que está na lista")

# 5. Calculando o valor mínimo de acordo com a função min()
print(f"> {min(mensagem)} é o valor mínimo, ou seja, é o menor valor que está na lista")

# 6. Calculando a amplitude da lista
print(f"> {max(mensagem) - min(mensagem)} é o valor da amplitude, ou seja, é a diferença entre o maior e o menor valor presente na lista")

# 7. Separando os 5 primeiros e os 5 últimos valores da lista
print(f"Os 5 primeiros valores são: {mensagem[:5]} pois se encontram no começo da lista")
print(f"Os últimos 5 valores são: {mensagem[-5:]} pois se encontram no final da lista")

# 8. Calculando o desvio padrão de acordo com a função da biblioteca
desvio_padrao = statistics.pstdev(mensagem)
print(f"> {desvio_padrao:.2f} é o valor do desvio padrão, ou seja, a medida da distribuição de dados em comparação com a média")

# 9. Calculando a variância de acordo com a função da biblioteca
variancia = statistics.pvariance(mensagem)
print(f"> {variancia:.2f} é o valor da variância, ou seja, a medida da distância de cada valor até a média")