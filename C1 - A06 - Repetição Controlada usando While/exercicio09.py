# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# C1 > Python Essentials > Aula 06 - Questão 9:
# Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B
# seja 200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para
# que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento. Utilizando loop com while.
# populacaoA = 80000    crescimentoA = 1.03
# populacaoB = 200000   crescimentoB = 1.015

populacaoA = 80000
crescimentoA = 1.03
populacaoB = 200000
crescimentoB = 1.015
anos = 0

while populacaoA < populacaoB:
    populacaoA = populacaoA * crescimentoA
    populacaoB = populacaoB * crescimentoB
    anos = anos + 1
    
print(f"Serão necessários {anos} anos")