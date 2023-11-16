# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 10:
# Como você lê um arquivo em Python que tenha valores. Faça um programa para ler um número inteiro na primeira linha do arquivo,
# e depois ler um número com casas decimais na segunda linha (cuidado, seu usuário pode ter usado ponto decimal, mas também poderia
# ter usado vírgula como separador). E por último na terceira linha tem um nome que deve ser lido. Apenas 3 variáveis serão lidas,
# um inteiro, um float e uma string.  E imprimir essas 3 variáveis.

# Explicação:
# Para ler um arquivo que tem valores em linhas diferentes, é utilizado o arquivo.readline(), que separa o arquivo em linhas e
# escreve como desejado, conforme o exemplo.

with open("exercicio10.txt", "r") as arquivo:
    inteiro = int(arquivo.readline())
    decimal = float(arquivo.readline().replace(",", "."))
    nome = arquivo.readline()
    
print("O inteiro é: ", inteiro)
print("O decimal é: ", decimal)
print("O nome é: ", nome)