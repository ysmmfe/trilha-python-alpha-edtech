# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 3:
# Faça um programa que leia uma string e remova todas as suas vogais. Considere que o usuário digitará apenas palavras (strings) sem acento.

frase = input("Digite uma frase: ")

vogais = "aeiou" # Especificando quais letras devem ser procuradas na frase
frase_final = "" 

for letra in frase:
    if letra not in vogais:
        frase_final += letra # Recebendo como resultado apenas as letras que não são iguais à variável 'vogais'
        
print("> A frase digitada sem vogais é:", frase_final)