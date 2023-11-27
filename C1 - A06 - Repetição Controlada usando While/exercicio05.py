# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 5:
# Ao observar a curva de velocidade de um motor, um engenheiro percebeu que sempre ocorria uma queda de velocidade quando medições eram
# feitas em intervalos de 10 ms. Após realizar alguns testes, ele observou que tais quedas não ocorriam necessariamente no mesmo momento.
# Intrigado pela falta de padrão, agora ele quer a sua ajuda para saber: dado um caso de teste, qual a primeira medição em que ocorreu
# uma queda de velocidade?
# Entradas: A primeira entrada é um número inteiro N, representando a quantidade de medições de velocidade do motor em um determinado
# teste. Cada uma das próximas N entradas consiste de um único inteiro M (0 ≤ M ≤ 10000) representando o número de RPM (rotações por
# minuto) daquela medida.
# Saídas: A saída é o índice da medição em que ocorreu a primeira queda de velocidade. Caso não aconteça nenhuma queda, o seu programa
# deve imprimir o número 0. (dica: não precisa armazenar os valores em nenhuma lista ou array/vetor, já no mesmo instante da leitura
# deve ser feito o cálculo se o valor lido é menor que o número imediatamente anterior).
# Exemplo 1:        Exemplo 2:          Exemplo 3:
# Entradas:         Entradas:           Entradas:
# 3                 5                   4
# 1                 100                 1
# 4                 199                 2
# 2                 199                 2
# Saída: 3          198                 2
#                   0                   Saída: 0
#                   Saída: 4

medicoes = int(input("Informe a quantidade de medições: "))

cont, anterior = 1, 0
queda = 0

while cont < medicoes+1:
    num = int(input())
    if num >= anterior:
        anterior = num
    else:
        if queda == 0:
            queda = cont
        
    cont += 1
print("saida", queda)