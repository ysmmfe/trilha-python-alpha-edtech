anguloDistancia = float(input("Informe o ângulo da distância entre C1 e C2: "))
distanciaEstadios = int(input("Agora informe a distância em estádios entre C1 e C2: "))

numVoltas = 360/anguloDistancia
circunferenciaEstadios = numVoltas * distanciaEstadios
circunferenciaKm = (circunferenciaEstadios * 176.4) /1000

print(f"\nA circunferência do planeta corresponde a {circunferenciaEstadios:.1f} estadios, ou seja, {circunferenciaKm:.1f} km")