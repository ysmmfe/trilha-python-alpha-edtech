# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 10:
# Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma
# mensagem de erro e voltando a pedir as informações. Mas faça no máximo 3 tentativas.

nome = input("Digite seu nome: ")
senha = input("Agora digite sua senha: ")
cont = 1

while senha == nome and cont <=3:
    print("[ERROR] - A senha é igual ao nome do usuário. Tente novamente.")
    print(f"\n\t> Essa é a sua {cont}° tentativa ")
    nome = input("Digite seu nome: ")
    senha = input("Agora digite sua senha: ")
    cont += 1