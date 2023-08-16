# for loop - utilizando is e else
# para compras confirmadas




compra_confirmada = True
dados_compra = 'compra no valor de R$ 12.50 e entrega confirmada'


for enviar in range(3):
    print(dados_compra)
    print('detalhes enviados para seu email')
    break
else:
    print('falha na compra')



#for loop - Nested loops (laços aninhados)

    #outer loop (laço externo)

      #tinner loop (loop interno)
'''
for numero1 in range(5):
  print(numero1)
  for numero2 in range(5):
      print(numero1,numero2)
 '''     

for numero1 in range(1,6):
  print('produto' + str(numero1))
  for numero2 in range(5):
       print(numero1,numero2)  