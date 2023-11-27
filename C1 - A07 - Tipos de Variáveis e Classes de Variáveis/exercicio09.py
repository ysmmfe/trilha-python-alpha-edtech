# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 9:
# Palíndromos são palavras ou frases que podem ser lidas da esquerda para a direita ou da direita para a esquerda (pular os
# espaços ou pontuação). Criar um programa que leia uma frase e verifique se essa frase é palíndromo ou não.

frase = input("Digite uma frase: ")
frase_invertida = ""
frase_final = ""
    
caractere = " .,!-?:;_"
for letra in frase:
    if letra not in caractere:
        frase_final += letra
        
for letra in range(len(frase_final) - 1, -1, -1): # range(a, b, c) em que 'a' é a ultima letra (total string - 1), 'b' é a primeira letra (0-1) 
                                            # e 'c' é a ordem de volta, ou seja, uma casa do final até o começo da string
    frase_invertida += frase_final[letra]
        
if frase_invertida == frase_final:
    print(f"{frase_final} invertido é {frase_invertida}\nA frase é um palíndromo!")
else:
    print(f"{frase_final} invertido é {frase_invertida}\nA frase não é um palíndromo")