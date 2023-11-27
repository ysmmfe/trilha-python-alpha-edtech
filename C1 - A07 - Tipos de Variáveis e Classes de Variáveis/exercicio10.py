# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 10:
# Escreva um programa que verifica o uso correto de parênteses em uma equação. Para os fins deste exercício, consideramos
# que o uso de parênteses foi empregado de forma adequada se cada “(” possui o seu respectivo “)”.
# Exemplo: 8 + ( 9 + 10) ⇢ correto. Exemplo: ((9 + (5 + 8) + 10) + (3 + 10)) + 5 ⇢ correto. Exemplo: 3 * (8 + (5 * 9 ^ 8) + 3 ⇢ incorreto.

equacao = input("Digite uma equação que contenha parênteses: ")

cont = 0

for caractere in equacao:
    if caractere == "(":
        cont += 1           # contador funcionando pra saber se a quantidade de parênteses é o mesmo e se eles estão em ordem correta.
                            # ex: "(" ... ")" -> correto.   ")" ... "(" -> ordem incorreta.
    elif caractere == ")":
        cont -= 1
        if cont < 0:        # caso esteja na ordem incorreta, o contador será negativo e já retorna o resultado
            break
        
if cont == 0:
    print("\nOs parênteses estão sendo usados corretamente!")
else:
    print("\nOs parênteses não estão corretos na equação")