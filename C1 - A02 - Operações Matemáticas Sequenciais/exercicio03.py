# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 3:
# A conversão de graus Fahrenheit para Celsius é dada pela expressão: C . 1.8 = F - 32
# e a conversão de Kelvin para graus Celsius é dada por: C = k - 273.15. Faça um programa que recebe como entrada
# a temperatura em graus Celsius e realize duas conversões: uma para Fahrenheit e outra para Kelvin.

celsius = int(input("Informe a temperatura em °C: "))

fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f"{celsius}°C são {fahrenheit}°F e {kelvin}°K")