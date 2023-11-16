# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 03 - Questão 6:
# Como você pode formatar a saída em Python usando a função print()? Dê exemplos de como formatar uma saída para que um número
# seja exibido com um número específico de casas decimais. Usar também a função round() para arredondar com um número de casas
# decimais especificado.

# Explicação:
# É possível formatar a saída em Python utilizando a função print() por meio de uma string normal ou de uma f-string. Com uma
# string normal, utilizamos o método format() para substituir as posições de uma variável dentro da frase com a sintaxe. Já
# utilizando a f-string, pode-se formatar o número de casas decimais dentro da variável em {}. Utilizando a função round(),
# as casas decimais são arredondadas e aparecem de acordo com a quantidade colocada no parâmetro da função.

# Utilizando o método format para saída com 3 casas decimais
a = 8.0
b = 0.7
x = a/b
print("O valor de {0}/{1} é {2:.3f}".format(a, b, x))

# Utilizando a f-string para saída com 4 casas decimais
print(f"\nO valor de {a}/{b} é {x:.4f}")

# Utilizando a função roud() para saída com 2 casas decimais
arredondado = round(x, 2)
print("\nA valor arredondado é:", arredondado)