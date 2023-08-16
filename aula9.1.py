valor = int(input('digite o valor do seu produto em R$:'))

while valor > 20:
    valor = (valor * 0.10) + valor
    print (f' o valor final do  seu produto sera de R${valor}')
    break