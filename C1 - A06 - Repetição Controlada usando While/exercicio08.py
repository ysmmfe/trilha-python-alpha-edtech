# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 8:
# Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá
# mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o
# estilo e o número de testes (divisões) executados.

n = int(input("Informe um número inteiro: "))

divisoes = 0
numero = 2

print(f"Os números primos entre 1 e {n} são: ", end="")
while numero <= n:
    primo = True
    divisor = 2
    
    while divisor <= int(numero**0.5):
        divisoes += 1
        
        if numero % divisor == 0:
            primo = False
            break
        divisor += 1

    if primo:
        print(numero, end=", ")

    numero += 1

print(f"\nOcorreram {divisoes} divisões!")
