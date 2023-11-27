# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 08 - Questão 7:
# Crie um programa que crie um conjunto (set) dos 3 maiores compradores de ações do exercício 6. Depois crie outro conjunto dos 3 piores
# compradores de ações. O resultado final deve ser a união dos 2 conjuntos.

import statistics

quantidade_acoes = []
valor_acoes = []
continuar = 0
soma_quantidade, quantidade_valida, soma_valor, valor_valido = 0, 0, 0, 0
nomes = []

# 1. Recebendo os valores da quantidade e valor pelo usuário com tratamento de erros
while continuar != '0':
    while True:
        try:
            quantidade_acoes.append(int(input("\nInforme a quantidade de ações: ")))
            valor_acoes.append(float(input("Agora informe o valor da ação: ")))
            nomes.append(input("Por último, informe seu nome: ").upper())
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
print(f"> O valor da variância é {variancia:.2f}\n")

# 6. Calculando a quantidade de vezes que o nome aparece nos dados de entrada
contagem_nomes = {}
for nome in nomes:
    contagem_nomes[nome] = contagem_nomes.get(nome, 0) + 1 # se o nome estiver no dicionário, incrementa 1, se não, atribui 1 ao seu valor
    
print("============= Quantidade de aparição dos clientes =============")
for nome, contagem in contagem_nomes.items():
    print(f"> {nome} aparece {contagem} vez(es)")
    
# 7. Criando a lógica do set de 3 maiores e 3 menores compradores
acoes = {}
# Associando o valor total investido em ações a cada nome de cliente
for i in range(0, len(quantidade_acoes)):
    acoes[nomes[i]] = quantidade_acoes[i] * valor_acoes[i]

# Ordenando do maior pro menor (reverse) os valores de ações dentro do dicionário e repartindo apenas os 3 primeiros e 3 últimos
tres_maiores = sorted(acoes.items(), key=lambda x: x[1], reverse=True)[:3]
conjunto_tres_maiores = {nome for nome, valor in tres_maiores} # Atribuindo os nomes à um set
tres_menores = sorted(acoes.items(), key=lambda x: x[1], reverse=True)[-3:]
conjunto_tres_menores = {nome for nome, valor in tres_menores}
print("\n============= Ranking de clientes =============")
print(f"> Os três maiores compradores de ações são: {conjunto_tres_maiores}")
print(f"> Os três piores compradores de ações são:  {conjunto_tres_menores}")
resultado = conjunto_tres_maiores.union(conjunto_tres_menores)
print(f"> O resultado da união desses 2 conjuntos é: {resultado}")