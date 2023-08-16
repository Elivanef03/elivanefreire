#modificar de FANTASTICO para F A N T A S T I C O


palavra = ' FANTASTICO'

for spaco in palavra:
    print( f' {spaco}' , end=' ')




# criar um retangulo de 6x6
'''
&&&&&&
&&&&&&
&&&&&&
&&&&&&
&&&&&&
&&&&&&

'''




'''
linha = 6
coluna = 6
simbolo = '&'

for l in range(linha):
    for c in range(coluna):
        print(simbolo , end=' ')
    print()    
    '''

 # while loops ===

 # excelente para loops dependentes de uma condicao

 # eu preciso criar uma promoçâo para um produto no valor de 100 reais

 # só que a promoçao tem um porem ela começa a 100 reais e depois ela vai baixando vai para 95 reais

 # 90 reais eu quero que cada dia ela vai ficando 5 reais mais baixa

'''
valor = 100


dia = 1

while valor > 20:
  dia +=1
  print(f' no dia {dia} o produto bom ser vendido pot {valor}')

  valor -= 5
  '''

# operador ternario

idade = 20
'''

# if idade >= 16:
  #   resultado = print('voto  nao permitido')
#else:
   #  resultado = print('voto nao permitido)

resultado = 'voto permitido' if idade >= 16 else ' voto nao permitido'
print (resultado)

'''


#publicar um produto com comissao de 10% se for acima de R$: 20

valor = int(input('digite o valor do seu produto em R$:'))

while valor > 20:
    valor = (valor * 0.10) + valor
    print (f' o valor final do  seu produto sera de R${valor}')
    break