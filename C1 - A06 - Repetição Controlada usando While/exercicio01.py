# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 1:
# Faça Desenvolva um programa que simule o funcionamento de uma máquina de somar.
# Entrada: O seu programa receberá um número inteiro não negativo N que denota a quantidade de números que seu programa
# receberá para computar o valor total da soma. Na sequência seu programa receberá N números reais.
# Saída: O seu programa deve imprimir a frase “Total:  ” seguida do valor da soma (com duas casas decimais de precisão).

quantidade = int(input("Informe a quantidade de números a receber: "))
soma = 0
i = 1

while(i <= quantidade):
    num = float(input(f"Digite o {i}° número: "))
    soma += num
    i += 1
    
print(f"Total: {soma:.2f}")