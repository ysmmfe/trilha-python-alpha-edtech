# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 2:
# Faça um programa que lê um caractere C (uma string de tamanho 1) e uma string S. O programa deve imprimir a string S com todos os
# caracteres C (maiúsculos e minúsculos) removidos. (Dica: Você pode usar o comando str.lower() para converter uma string str para
# letras minúsculas), (dica 2: não vale usar a função replace).

c = input("Digite o caractere a ser procurado: ")
s = input("Agora informe a frase: ")

frase = str.lower(s) # Converte a string para letras minúsculas
frase_final = ""

for letra in frase:
    if letra != c:
        frase_final += letra # Recebendo como resultado apenas as letras que não são iguais à variável 'c'
        
print(f"> A frase digitada sem o caractere {c} é:", frase_final)