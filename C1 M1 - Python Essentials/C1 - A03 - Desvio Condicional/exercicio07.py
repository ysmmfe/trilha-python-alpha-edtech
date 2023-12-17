# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 03 - Desvio Condicional > Questão 7:
# Como você pode formatar a saída de dados de maneira a criar uma tabela ou uma matriz com alinhamentos apropriados em Python? 
# Dê um exemplo de como você pode criar uma tabela simples usando `print()` e formatação (pesquisar o caracter escape de tabulação \t). 
# Por exemplo, imprimir a tabela abaixo fixa:
# Preço      Desconto (%)	Produto    
# 2,50	         5	        Caneta
# 10,75	        10	        Caderno
# 23,25	        15	        Mochila

# Com o exemplo da questão
linha1 = ["\nPreço", "Desconto (%)", "Produto"]
print("{:^6} {:>16} {:>11}" .format(*linha1))

linha2 = [2.50, 5, "Caneta"]
print("{:^4} {:>6} {:>21}" .format(*linha2))

linha3 = [10.75, 10, "Caderno"]
print("{:^6} {:>5} {:>21}" .format(*linha3))

linha4 = [23.25, 15, "Mochila\n"]
print("{:^6} {:>5} {:>22}" .format(*linha4))