numero_1 = 5
numero2 =2

soma = numero_1 + numero2
subtracao = numero_1 - numero2
mutiplicacao = numero_1 * numero2
divisao = numero_1 / numero2
divisao_inteira = numero_1 // numero2
modulo = numero_1 % numero2
exponenciacao = numero_1 ** numero2


print(soma) # 3
print(subtracao) # 3
print(mutiplicacao) # 10
print (divisao) #  2.5
print(divisao_inteira) # 2
print(modulo)
print(exponenciacao) 



#operadores de precedencia

print((2 + 5)  * 3)  # resultado e 21 precedencia ()

print(1 + 5**2) # resultado e 26 precedencia **

print (5 * 3 + 8) # resultado 23 precedencia * /


# operadores de comparacao

operadores = 20 == 20

print(operadores)


numero_1 = 6
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
   print("soma nao e maior que 10")
else:
   print("soma e maior que 10")   


   if soma < 10:
      print("soma nao e maior que 10")
   else:
      print("soma e maior que 10")   


soma_1 = 8 + 9
soma_2 = 7 + 5


if soma == soma_2:
   print("os resultados sao iguais")
else:
   print("os resultados sao diferentes")   



   velocidade = 50
    

if velocidade >110:
   print('acima da velocidade') 
   print('favor reduzir a velocidade')  

elif velocidade > 60:
   print('favor dirigir acima de 80km/k')

else:
   print('velocidade ok')   
      
      



n1 = 10
n2 = 3.5

print(())


#desafio3

n1 = 10
n2 = 3.5
               
         
divisao =  n1 /n2

print(n1,'/',n2,'e igual a:',divisao)

#desafio4

nome2 = input('qual o seu nome?')

idade = int(input('qual sua idade?'))
print(f"Olá, {nome2}! Você tem {idade} anos")

#desafio5
n1 = 6
n2 = 2

n1 = float(input('informe um numero: '))
n2 = float(input('informe outro  numero: '))

print(f'''

{n1} + {n2} = {n1 + n2}
{n1} - {n2} = {n1 - n2}
{n1} * {n2} = {n1 * n2}
{n1} // {n2} = {n1 // n2}
{n1} ** {n2} = {n1 ** n2}

''')


'''
#operadores logicos

#and

renda_acima_5mil = True
nome_limpo = False

if renda_acima_5mil and nome_limpo:
   print('financiamento aprovado')
else:
   print('financiamento negado')   


   #or
   renda_acima_5mil = True
   nome_limpo = False

   if renda_acima_5mil or nome_limpo:
      print('financiamento aprovado')
   else:
      print('financiamento negado')  

idade_lucas = 21
idade_carolina = 17

#operador or
if idade_lucas >= 18 or idade_carolina >= 18:
   print('pelo menos um dos dois e maior de idade')
else:
   print('lucas e carolina nao sao maiores de idade')   

   #operador and
   if idade_lucas >= 18 and idade_carolina >= 18:
      print('lucas e carolina sao maiores de idade') 
   else:
      print('pelo menos um dos dois e maior de idade')  
      

      #multiplos operadores de comparacao

      valor = 20

      if 20 <= valor < 40:
      #if valor >= 20 and valor < 40:
        print('o produto foi aceito') 
      else:
         print('produto nao aceito')  


'''
         # for

         # imprimir de 1 a 5

         
for numero in range(1,20,2) :
      print(numero)


lojas = ['rio','sampa','belo','manaus']   

for loja in lojas:
      print(loja)
      print('acabou for')

for i in range(4) :
      print(i)
      print(lojas[i]) 

#for pra string

#for letra in 'google'     
   # print(letra)

palavra = 'google'

for letra in palavra:
      print(letra + 'esta dentro da palavra google')
            



#desafio06

#listaitens

frutas = ["maca","banana","manga","uva"]
print(frutas)


#desafio7
frutas = ["maca","banana","manga","uva"]

frutas = ["maca","uva"]
print(frutas[0:3])




               
       
            
             





    





    










