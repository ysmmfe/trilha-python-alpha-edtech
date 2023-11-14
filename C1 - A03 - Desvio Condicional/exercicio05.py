# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 5:
# Crie uma função personalizada personalizada que recebe uma string e substitui substitui todas as vogais por asteriscos (*). 
#Em seguida, use essa função para processar a entrada do usuário e exibir o resultado. Será que você consegue, sem usar repetição, sem if?

def substituir(palavra):
    palavra = palavra.replace("a", "*")
    palavra = palavra.replace("e", "*")
    palavra = palavra.replace("i", "*")
    palavra = palavra.replace("o", "*")
    palavra = palavra.replace("u", "*")
    
    print("O resultado da palavra é: ", palavra)

substituir(input("Digite uma palavra: "))