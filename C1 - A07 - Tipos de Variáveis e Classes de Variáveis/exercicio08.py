# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 8:
# Ler um nome completo, com vários nomes e sobrenomes. Extrair o último sobrenome (verificar o separador espaço entre os nomes).
# Colocar as iniciais dos nomes anteriores, exceto o último sobrenome, em que cada inicial em maiúscula e acompanhada com um ponto.
# Lembrar de colocar uma vírgula entre o último sobrenome e as iniciais. Isto é a formação de nomes de autores em citações no padrão ABNT.
# Exemplo: Paulo Marcotti ⇢ Marcotti, P. Exemplo: Joaquim DA SILVA xavier ⇢ Xavier, J. D. S. Exemplo: Pedro Alvares CABRAL ⇢ Cabral, P. A.

nome_completo = input("Digite o nome completo [não considerar preposições]: ").lower()

for letra in range(0, len(nome_completo), 1):
    if nome_completo[-letra] == " ":
        print(nome_completo[-letra + 1].upper() + nome_completo[-letra + 2:] + ", ", end="")
        nome_completo = nome_completo[:-letra]
        break
    
for letra in nome_completo:
    if letra == nome_completo[0]:
        print(letra.upper() + ". ", end="")
    
    if letra == " ":
        nome_completo = nome_completo[nome_completo.index(letra)+1:]