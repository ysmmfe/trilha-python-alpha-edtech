# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 02 - Operações Matemáticas Sequenciais > Questão 1:
# - A fórmula para calcular a área de uma circunferência é: área = pi . raio².
# Crie um programa para ler o valor do raio e efetuar o cálculo da área.
# Entrada: A entrada contém um número real, positivo, representando o raio.
# Saída: Seu programa deve imprimir na tela a área do círculo com 4 casas após o ponto decimal.

import math

raio = float(input("Informe o valor do raio: "))
area = math.pi * (raio**2)

print(f"A área da circunferência é {area:.4f}")