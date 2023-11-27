# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 6:
# Crie um programa que leia um texto e inverte todas as letras e imprima o resultado. Não deve usar mais de uma string,
# apenas usar a mesma variável string que leu.

frase = input("Digite uma frase: ")

print("O resultado da inversão é: ", end="")
for letra in range(len(frase) - 1, -1, -1): # range(a, b, c) em que 'a' é a ultima letra (total string - 1), 'b' é a primeira letra (0-1) 
                                            # e 'c' é a ordem de volta, ou seja, uma casa do final até o começo da string
    print(frase[letra], end="")