# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 02 - Questão 9:
# Eratóstenes de Cirene foi conhecido por calcular a circunferência da Terra ( https://pt.wikipedia.org/wiki/Erat%C3%B3stenes ). 
# Ele foi diretor da famosa Biblioteca de Alexandria e, lendo um dos manuscritos dessa instituição, tomou conhecimento de que, num
# determinado dia, num determinado horário, na cidade de Siena, não havia formação de sombra nos objetos, pois o sol estava no ponto
# mais alto do céu, com seus raios perpendiculares à superfície de Siena (popularmente, a pino). Este fato poderia ter passado
# despercebido para a maioria das pessoas, mas, intrigado, Eratóstenes resolveu checar se, neste mesmo dia e horário, o sol estaria a
# pino em Alexandria. Ele percebeu que não estava e a única explicação para tal discrepância seria a Terra ser redonda, pois, caso
# fosse plana, o sol também estaria no zênite em Alexandria. Eratóstenes percebeu que poderia calcular a circunferência da Terra fazendo
# um experimento em Alexandria no mesmo dia e horário em que o Sol estava no zênite em Siena. Para tanto, fincou uma estaca perpendicular
# ao chão de Alexandria e obteve um triângulo retângulo formado pela estaca, pela sombra no chão e pela reta que liga o fim da sombra ao
# topo da estaca (hipotenusa). O ângulo A formado entre a estaca e a hipotenusa é o mesmo que o ângulo entre a reta imaginária de um raio
# solar ao centro da Terra e a reta estendendo a estaca também ao centro da Terra. Caso Eratóstenes soubesse a distância entre Alexandria
# e Siena, seria possível determinar a circunferência da Terra. Ele, então, contratou um itinerante para medir a distância entre as duas
# cidades e constatou que a distância era de 5000 estádios. Cada estádio mede 176,4 metros. O ângulo A foi calculado e seu valor era 7,2°.
# Logo, 360° correspondem a 250000 estádios, isto é, 44100 km. Escreva um programa que calcule a circunferência C de um determinado planeta,
# com base na observação do ângulo A, entre duas localidades C1 e C2, e na distância D, em estádios, entre elas. Suponha que as localidades
# estejam no mesmo meridiano de um planeta esférico. O seu programa deverá imprimir a circunferência do planeta em estádios e em quilômetros

anguloDistancia = float(input("Informe o ângulo da distância entre C1 e C2: "))
distanciaEstadios = int(input("Agora informe a distância em estádios entre C1 e C2: "))

numVoltas = 360/anguloDistancia
circunferenciaEstadios = numVoltas * distanciaEstadios
circunferenciaKm = (circunferenciaEstadios * 176.4) /1000

print(f"\nA circunferência do planeta corresponde a {circunferenciaEstadios:.1f} estadios, ou seja, {circunferenciaKm:.1f} km")