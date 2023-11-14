# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 3:
# Leia o nome completo do usuário (o usuário sabe que não pode colocar caracteres especiais) (o usuário é obediente). "Calcule" o
# primeiro nome do usuário, sabendo que existe 1 espaço em branco terminando o primeiro nome. "Calcule" o último sobrenome do
# usuário, sabendo que existe 1 espaço em branco antes do último sobrenome. Montar o email do usuário como nome.sobrenome@gmail.com. 
# Lembre que não pode usar comando if ainda nestas questões. Você precisa uma função find() ou search() um caracter dentro de uma string.

nomeCompleto = input("Informe seu nome completo: ")

x = nomeCompleto.find(' ')
nome = nomeCompleto[0:x]
print("\nO seu primeiro nome é: ", nome)

y = nomeCompleto.rfind(' ')
sobrenome = nomeCompleto[y+1:]
print("O seu último sobrenome é: ", sobrenome)

print(f"O seu e-mail seria: {nome}.{sobrenome}@gmail.com")