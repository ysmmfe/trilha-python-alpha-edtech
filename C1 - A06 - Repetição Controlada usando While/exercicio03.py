# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 3:
# Crie um programa que permita verificar se um número N é fatorial ou não. Um número N é um número fatorial caso exista um número X > 0
# tal que N = X!.
# Entrada: O programa recebe um número inteiro N maior ou igual a zero.
# Saída: O programa deve imprimir Verdadeiro se N é fatorial, caso contrário deve imprimir Falso.
# Exemplo: 1 Verdadeiro, 2 Verdadeiro, 3 Falso, 6 Verdadeiro, 12 Falso, 24 Verdadeiro, 7777 Falso, 1307674368000 Verdadeiro, 943675496 Falso

num = int(input("Informe um número inteiro: "))

fac, cont = 1, 1

while fac < num:
    fac *= cont
    cont += 1
    
print(f"\t{num} é fatorial?", end=" ")
if fac == num:
    print(True)
else:
    print(False)