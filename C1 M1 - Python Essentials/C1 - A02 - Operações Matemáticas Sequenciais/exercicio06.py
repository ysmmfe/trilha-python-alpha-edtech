# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 02 - Operações Matemáticas Sequenciais > Questão 6:
# Faça um programa que leia três números inteiros e apresente o maior dos três valores. Nesta questão está proibido usar if (isto é,
# não deve se usar nenhuma estrutura condicional) ou a função max, mas vai precisar usar a função abs(z) que retorna com o valor do
# módulo, sem sinal do parâmetro. Dica: A seguinte fórmula permite calcular o maior valor dados os números x e y: 
# Max(x,y) = (x+y)/2 + abs(y-x)/2

num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

maior1 = (num1+num2)/2 + abs(num2-num1)/2
maior2 = int((maior1+num3)/2 + abs(num3-maior1)/2)

print(f"\nO maior dos 3 valores recebidos é {maior2}")