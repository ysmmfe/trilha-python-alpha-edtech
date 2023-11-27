# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 08 - Questão 5:
# Crie um novo programa baseado no exercício anterior que tenha 2 valores, um valor inteiro (por exemplo, quantidade de ações compradas)
# e um valor correspondente em ponto flutuante (valor real) (por exemplo, poderia representar o valor de uma ação desta compra
# correspondente). Agora o programa deve calcular todos os valores estatísticos do número inteiro (quantidade de ações) e depois calcular
# os valores correspondentes do número real (valor da ação).

import statistics

quantidade_acoes = []
valor_acoes = []
continuar = 0
soma_quantidade, quantidade_valida, soma_valor, valor_valido = 0, 0, 0, 0

# 1. Recebendo os valores da quantidade e valor pelo usuário com tratamento de erros
while continuar != '0':
    while True:
        try:
            quantidade_acoes.append(int(input("\nInforme a quantidade de ações: ")))
            valor_acoes.append(float(input("Agora informe o valor da ação: ")))
            continuar = input("\n[1] para sim, [0] para não. Deseja continuar? -> ")
            break
        except ValueError:
            print("[INVÁLIDO] - Por favor, informe uma quantidade válida!")

# 2. Achando os valores válidos da quantidade de ações e substituindo os inválidos pela respectiva média
for i in range(0, len(quantidade_acoes)):
    if quantidade_acoes[i] > 0:
        soma_quantidade += quantidade_acoes[i]
        quantidade_valida += 1

media_quantidade = int(soma_quantidade/quantidade_valida)

for i in range(0, len(quantidade_acoes)):
    if quantidade_acoes[i] < 0:
        quantidade_acoes[i] = media_quantidade

# 3. Achando os valores válidos do valor das ações e substituindo os inválidos pela respectiva média
for i in range(0, len(valor_acoes)):
    if valor_acoes[i] > 0:
        soma_valor += valor_acoes[i]
        valor_valido += 1

media_valor = int(soma_valor/valor_valido)

for i in range(0, len(valor_acoes)):
    if valor_acoes[i] < 0:
        valor_acoes[i] = media_valor

# 4. Calculando os valores estatísticos da quantidade de ações
print("\n============= Estatísticas da quantidade de ações =============")
media = statistics.mean(quantidade_acoes)
print(f"> O valor da média aritmética é {media}")
print(f"> O valor da mediana é {statistics.median(quantidade_acoes)}")
print(f"> O valor máximo é {max(quantidade_acoes)}")
print(f"> O valor mínimo é {min(quantidade_acoes)}")
print(f"> O valor da amplitude é {max(quantidade_acoes) - min(quantidade_acoes)}")
desvio_padrao = statistics.pstdev(quantidade_acoes)
print(f"> O valor do desvio padrão é {desvio_padrao:.2f}")
variancia = statistics.pvariance(quantidade_acoes)
print(f"> O valor da variância é {variancia:.2f}")

# 5. Calculando os valores estatísticos do valor das ações
print("\n============= Estatísticas do valor das ações =============")
media = statistics.mean(valor_acoes)
print(f"> O valor da média aritmética é {media}")
print(f"> O valor da mediana é {statistics.median(valor_acoes)}")
print(f"> O valor máximo é {max(valor_acoes)}")
print(f"> O valor mínimo é {min(valor_acoes)}")
print(f"> O valor da amplitude é {max(valor_acoes) - min(valor_acoes)}")
desvio_padrao = statistics.pstdev(valor_acoes)
print(f"> O valor do desvio padrão é {desvio_padrao:.2f}")
variancia = statistics.pvariance(valor_acoes)
print(f"> O valor da variância é {variancia:.2f}")