# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 03 - Desvio Condicional > Questão 1:
# Leia o primeiro nome do usuário e o último nome do usuário (o usuário sabe que não pode colocar espaço em branco nem sinais especiais),
# (o usuário é obediente). Montar o email do usuário como nome.sobrenome@gmail.com e pesquise como concatenar strings no Python.

primeiroNome = input("Informe o seu primeiro nome: ")
ultimoNome = input("Agora informe o seu último nome: ")

# utilizando f string
#print(f"O seu email será: {primeiroNome}.{ultimoNome}@gmail.com")

# Utilizando concatenação de string, como exemplificado na questão
print("\nO seu e-mail será: " + primeiroNome + "." + ultimoNome + "@gmail.com")