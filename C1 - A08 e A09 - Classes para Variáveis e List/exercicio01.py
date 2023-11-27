# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 08 - Questão 1:
# Você está desenvolvendo um sistema de análise de dados financeiros e precisa criar um programa em Python para realizar operações
# avançadas em um conjunto de dados representado por uma lista de números inteiros (poderia ser a quantidade de ações compradas de
# uma determinada empresa). Crie um programa que leia esses dados e armazene em uma List de números inteiros (dica: usar o método
# append da uma List), montando assim um vetor de números inteiros. Salvar esse vetor em um arquivo, para utilizar nos próximos exercícios.

dados = []
numero = 0

# Implementando tratamento de erros
while numero != -1:
    while True:
        try:
            numero = int((input("Informe um número inteiro: ")))
            break
        except ValueError:
            print("[INVÁLIDO] - Por favor, informe um número inteiro válido")
    
    dados.append(numero)

# Escrevendo os dados no arquivo
with open("arquivo.txt", "w") as arquivo:
    arquivo.write(str(dados))