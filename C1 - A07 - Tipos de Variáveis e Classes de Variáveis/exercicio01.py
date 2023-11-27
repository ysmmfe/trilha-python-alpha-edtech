# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 07 - Questão 1:
# O jogo Street Fighter foi um dos primeiros jogos eletrônicos do gênero conhecido como jogos de luta. Neste jogo, um mestre de artes
# marciais, chamado Ryu, enfrenta outros lutadores em um torneio internacional de artes marciais. Cada combate entre Ryu e um oponente
# se dá em uma série de rounds. No início de cada round, cada jogador está com 100 pontos de vida. O objetivo é atacar o oponente com
# diferentes golpes, sendo que cada golpe aplicado subtrai certa quantidade de pontos de vida do outro combatente. Perde o round aquele
# jogador cujos pontos de vida chegar primeiro à zero. Vence a luta quem ganhar o maior número de rounds. Crie um programa que simule
# uma luta entre Ryu e Ken e determine quem ganhou a luta. Entrada: A entrada consiste de uma sequência de inteiros, um em cada linha,
# representando os valores dos golpes aplicados (valores positivos) e recebidos (valores negativos) por Ryu. A luta termina quando o
# inteiro lido for 0. Um round só termina quando um dos jogadores fica com 0 ou menos pontos de vida. Você pode assumir que em cada
# round pelo menos um golpe será aplicado. Saída: A saída deverá conter apenas uma linha, contendo somente “Ryu venceu”, “Ken venceu”
# ou “Empate”, de acordo com o resultado geral da luta. Exemplo: Suponha que a sequência de entrada seja composta pelos números: 40,
# 5, -32, 9, -45, 48, -27, -64, 75, 6, 4, -7, 3, -39, 0 Então temos dois rounds. O primeiro round tem 6 golpes e Ryu ganha, pois 40 + 5
# + 9 + 48 = 102 ≥ 100. O segundo round tem 8 golpes e Ken ganha, pois 27 + 64 + 7 + 39 = 137 ≥ 100. Logo, o resultado da luta é “Empate”.
# 100, -68, 60, -32, -57, 80, -28, 10, -5, -6, 8, 2, 0 ⇢ Ryu Vence
# 65, 84, -80, -20, 0 ⇢ Empate
# 32, -32, 65, -65, 9, -9, 15, -15, 80, -80, 99, -100, 0 ⇢ Ken venceu

golpe = None 
vidaRyu = 100
vidaKen = 100
vitoriaRyu = 0
vitoriaKen = 0

while golpe != 0:
    golpe = int(input("Informe o valor do golpe: "))
    if golpe > 0:
        vidaKen -= golpe
        
    if golpe < 0:
        vidaRyu += golpe
        
    if vidaKen <= 0:
        vitoriaRyu += 1
        vidaKen = 100
        vidaRyu = 100
    elif vidaRyu <= 0:
        vitoriaKen += 1
        vidaRyu = 100
        vidaKen = 100
    
if vitoriaRyu > vitoriaKen:
    print("Ryu venceu!")
elif vitoriaKen > vitoriaRyu:
    print("Ken venceu!")
else:
    print("Empate")