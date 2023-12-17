# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 05 - Repetição Controlada em Python > Questão 3:
# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 0 a 10. O usuário deve informar de
# qual número ele deseja ver a tabuada

num = int(input("Informe qual número você deseja ver a tabuada: "))

print("\nA tabuada de", num, "é:")
for i in range(11):
    mult = i * num
    print(f"{i} x {num} = {mult}")