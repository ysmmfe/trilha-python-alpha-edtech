# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 2:
# Faça um temporizador de segundos (contagem regressiva) que passe a atualizar o tempo mais raramente. A contagem com o intervalo entre
# cada atualização fique dois segundos maior após cada uma delas. Por exemplo, se ele iniciar o temporizador com 50 segundos, então
# receberá atualizações dizendo que faltam 50, 48, 44, 38, 30, 20 e 8 segundos (note que os intervalos entre as notificações foram 2,
# 4, 6, 8, 10 e 12 segundos). Desenvolva um programa que exiba em quais segundos o temporizador receberá atualizações, dado que o
# programa tenha sido inicializado com um tempo igual a N.
# Observação importante: seu programa não precisa consultar o relógio do computador, só fazer uma contagem regressiva.
# Entrada: O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.
# Saída: Seu programa deve escrever a saída conforme os exemplos abaixo.
# Exemplo 1:                Exemplo 2:
# N = 10                    N = 50
# Faltam 10 segundos        Faltam 50 segundos
# Faltam 8 segundos         Faltam 48 segundos
# Faltam 4 segundos         Faltam 44 segundos
# Acabou                    Faltam 38 segundos
#                           Faltam 30 segundos
#                           Faltam 20 segundos
#                           Faltam 8 segundos
#                           Acabou

tempoInicial = int(input("Informe o tempo inicial: "))

i = 1

while tempoInicial > 0:
    print(f"Faltam {tempoInicial} segundos")
    tempoInicial -= 2 * i
    i += 1

print("Acabou")