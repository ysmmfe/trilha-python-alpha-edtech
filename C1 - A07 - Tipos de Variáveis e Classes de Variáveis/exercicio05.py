# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 5:
# Faça um programa que lê uma string e conta o número de vogais, consoantes, espaços e pontuações (caracteres “.”, “,”, “!”, “?”, "-").
# Observação: é proibido o uso de funções auxiliares, como o  count(), por exemplo. A saída do programa deve ser a porcentagem de
# cada tipo de caractere na string, com 2 casas após a vírgula. Exemplo:
# Entrada: Mesmo que a realidade seja um pesadelo, nao podemos deixar de sonhar.
# Saída: Vogais: 40.58%   Consoantes: 40.58%   Espacos: 15.94%    Pontuacoes: 2.90%

frase = input("Digite uma frase: ")

frase = str.lower(frase)
vogais = "aeiou"
contVogais = 0
consoantes = "bcdfghijklmnpqrstvwxyz"
contConsoantes = 0
espacos = " "
contEspacos = 0
pontuacoes = ".,!?-"
contPontuacoes = 0

for caractere in frase:
    if caractere in vogais:
        contVogais += 1
    elif caractere in consoantes:
        contConsoantes += 1
    elif caractere == espacos:
        contEspacos += 1
    elif caractere in pontuacoes:
        contPontuacoes += 1
        
total = contVogais + contConsoantes + contEspacos + contPontuacoes
contVogais = (contVogais/total) * 100
contConsoantes = (contConsoantes/total) * 100
contEspacos = (contEspacos/total) * 100
contPontuacoes = (contPontuacoes/total) * 100

print("\nPorcentagem de cada tipo de caractere na string:")
print(f"Vogais: {contVogais:.2f}% \nConsoantes: {contConsoantes:.2f}% \nEspaços: {contEspacos:.2f}% \nPontuações: {contPontuacoes:.2f}%")