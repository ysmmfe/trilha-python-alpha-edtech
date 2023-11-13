num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

maior1 = (num1+num2)/2 + abs(num2-num1)/2
maior2 = int((maior1+num3)/2 + abs(num3-maior1)/2)

print(f"\nO maior dos 3 valores recebidos é {maior2}")