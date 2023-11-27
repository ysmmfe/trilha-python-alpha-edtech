# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 4:
# Um pantograma ou pangrama (do grego, pan ou pantós = todos, + grama = letra) é uma frase em que são usadas todas as letras
# do alfabeto de determinada língua. Crie um programa que permita verificar se uma frase é ou não um pantograma. Considere
# que o usuário digitará apenas uma frase. A entrada contém uma frase sem acentos que pode ter letras maiúsculas ou minúsculas,
# ou sinais de pontuação.

frase = input("Escreva uma frase: ")

frase = str.lower(frase)
alfabeto = "abcdefghijklmnopqrstuvwxyz"
cont = 0
contLetra = ""

for letra in frase:
    if letra in alfabeto and letra not in contLetra:
        contLetra += letra
        cont += 1
        
if cont == 26:
    print("Essa frase é um pantograma!")
else:
    print("Essa frase não é um pantograma")