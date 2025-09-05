import os
os.system('cls')

        #EXECUTANDO CÓDIGOS 

A = int(input('Digite o valor A: '))
B = int(input('Digite o valor B: '))   
C = int(input('Digite o valor C: '))

        #SOMA

soma_a_mais_b = A + B

        #CONDIÇÃO

if soma_a_mais_b < C:
    print(f'{A} + {B} é igual a {soma_a_mais_b} menor que {C}.')
else:
    print(f'{A} + {B} é igual a {soma_a_mais_b} maior que {C}.')
print('FIM.')