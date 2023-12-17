# Trilha Python - Alpha EdTech
# Autor: https://github.com/ysmmfe

# Ciclo 1 > Módulo 1 - Python Essentials > Aula 04 - Desvio Condicional 2 > Questão 2:
# Faça um programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida.
# (obs.: o ano 2000 foi bissexto e o ano 1900 não foi bissexto, pesquisar!!!).

data = input("Digite uma data no formado dd/mm/aaaa: ")

dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:])

if(ano%100==0 and (not ano%400==0) and mes==2 and dia>=29): # ex: anos 1700, 1800, 1900, 2100, etc não são bissextos
    print(">>Essa não é uma data válida<<")
else:
    if (not ano%4==0) and mes==2 and dia>=29: 
        print(">>Essa não é uma data válida<<")
    else:
        if (mes <1 or mes >12) or (dia<1 or dia>31):
            print(">>Essa não é uma data válida<<")
        else:
            if (mes==4 or mes==6 or mes==9 or mes==11) and dia>30:
                print(">>Essa não é uma data válida<<")
            else:
                if(mes==1 or mes==3 or mes==5 or mes==7 or mes==8 or mes==10 or mes==12) and dia>31:
                    print(">>Essa não é uma data válida<<")
                else:
                    print("\tEssa data é válida!")