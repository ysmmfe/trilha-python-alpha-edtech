# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 4:
# Crie um programa que permita imprimir uma representação de um tabuleiro de xadrez.
# Entrada: O programa recebe um número inteiro, maior ou igual a 1, que indica a dimensão do tabuleiro.
# Saída: O programa deve desenhar o tabuleiro com dois caracteres que representam as divisões em cores diferentes conforme exemplos
# apresentados a seguir. (dica: print(“x”,end=””) não muda de linha)
# Exemplos:
# 3     4       5       1
# oxo   oxox    oxoxo   o
# xox   xoxo    xoxox
# oxo   oxox    oxoxo
#       xoxo    xoxox
#               oxoxo

dimensao = int(input("Informe um número inteiro: "))

i, j = 1, 1

while i <= dimensao:
    
    if i % 2 != 0:
        while j <= dimensao:
            if j % 2 != 0:
                print("o ", end="")
            else:
                print("x ", end="")
                
            j += 1
    else:
        while j <= dimensao:
            if j % 2 != 0:
                print("x ", end="")
            else:
                print("o ", end="")
                
            j += 1
    
    print("\n", end="")    
    j = 1
    i += 1