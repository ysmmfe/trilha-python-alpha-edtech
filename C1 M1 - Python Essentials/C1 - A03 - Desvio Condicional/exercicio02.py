# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 03 - Desvio Condicional > Questão 2:
# Em Python, não existem funções nativas chamadas left(), right(), ou substring(). No entanto, é possível alcançar comportamentos
# semelhantes usando técnicas de fatiamento (slicing) de strings. Explique como você pode exibir partes específicas de uma string
# usando slicing e, em seguida, demonstre isso com um exemplo (dica: pesquisar como fazer slicing de uma string em Python?).

# Explicação: 
# É possível exibir partes específicas de uma string utilizando a técnica slicing, com formato de parâmetros nome_string = [a:b:c],
# onde "a" é o ponto inicial do "corte" da string, "b" é o ponto final do corte que finaliza o intervalo desejado e "c" é o
# parâmetrode incremento, que determina o intervalo entre os números do intervalo principal do fatiamento. Segue em anexo o exemplo
# de uso do slicing.

nome = input("Digite seu nome: ")

print("\nA primeira letra do seu nome é: ", nome[:1])
print("A última letra do seu nome é: ", nome[-1:])
print("\nAs letras ímpares do seu nome são: ", nome[::2])
print("As letras pares do seu nome são: ", nome[1::2])