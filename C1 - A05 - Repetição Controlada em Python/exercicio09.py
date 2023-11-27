# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 9:
# Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro,
# para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. A
# quantidade de alunos será digitada logo no início. Ao encerrar o programa também deve ser informados os códigos e valores dos
# clientes mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dospesos dos clientes.

alto = None
baixo = None
gordo = None
magro = None
somaAltura = 0
somaPeso = 0

quantidade = int(input("Informe a quantidade de alunos: "))

for i in range(1, (quantidade+1)):
    codigo = input(f"\n{i}° cliente, informe seu código: ")
    altura = int(input("Agora informe sua altura (em cm): "))
    peso = float(input("Por último, informe seu peso (em Kg): "))
    
    somaAltura = somaAltura + altura
    somaPeso = somaPeso + peso
    
    if alto is None or altura>alto:
        alto = altura
        numAlto = codigo
        
    if baixo is None or altura<baixo:
        baixo = altura
        numBaixo = codigo
        
    if gordo is None or peso>gordo:
        gordo = peso
        numGordo = codigo
        
    if magro is None or peso<magro:
        magro = peso
        numMagro = codigo
        
mediaAltura = somaAltura/quantidade
mediaPeso = somaPeso/quantidade

print(f"\nO aluno mais alto é o número {numAlto} com {int(alto)}cm")
print(f"O aluno mais baixo é o número {numBaixo} com {int(baixo)}cm")
print(f"O aluno mais gordo é o número {numGordo} com {int(gordo)}Kg")
print(f"O aluno mais magro é o número {numMagro} com {int(magro)}Kg")
print(f"\nA média das alturas é: {mediaAltura:.1f} cm")
print(f"A média dos pesos é: {mediaPeso:.1f} Kg")