# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 8:
# Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando
# a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno
# mais baixo, junto com suas alturas.

alto = None
baixo = None

for i in range(1, 11):
    aluno = input(f"Informe o número [00] e a altura (em cm) do {i}° aluno: ")
    num = aluno[0:2]
    altura = float(aluno[3:7])
    
    if alto is None or altura > alto:
        alto = altura
        numAlto = num
        
    if baixo is None or altura < baixo:
        baixo = altura
        numBaixo = num
        
print(f"\nO aluno mais alto é o número {numAlto} com {int(alto)}cm")
print(f"O aluno mais baixo é o número {numBaixo} com {int(baixo)}cm")