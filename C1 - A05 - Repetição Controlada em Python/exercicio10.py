# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 05 - Questão 10:
# Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e
# ao final mostrar o número de votos de cada candidato.

candidato1 = 0
candidato2 = 0
candidato3 = 0

eleitores = int(input("Informe o número total de eleitores: "))

for i in range(1, (eleitores+1)):
    voto = input(f"\n{i}° eleitor, digite o número do candidato para votar: [1, 2 ou 3] -> ")
    
    if voto=='1':
        candidato1 = candidato1 + 1
        
    if voto=='2':
        candidato2 = candidato2 + 1
        
    if voto=='3':
        candidato3 = candidato3 + 1
        
print("\nO número de votos de cada candidato foi:")
print(f"Candidato 1: {candidato1} voto(s)")
print(f"Candidato 2: {candidato2} voto(s)")
print(f"Candidato 3: {candidato3} voto(s)")