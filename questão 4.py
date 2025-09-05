import os
os.system('cls')

        #COMANDOS

print('''
==========LOJA DE FRUTA==========

    --ATÉ 5 Kg--
      
MORANGO: R$ 2,50 kg 
MAÇÃ: R$ 1,80 kg

    --ACIMA 5 Kg--

MORANGO: R$ 2,20 kg  
MAÇÃ: R$ 1,50 kg     

OBS: Acima ou igual 10kg - !! 10% desconto !!''')

quantidade_de_kg_morango = float(input('\nquantos kg morango: '))
quantidade_de_kg_maçã = float(input('quantas kg maçãs: '))

        #CONDIÇÃO 1

if quantidade_de_kg_maçã and quantidade_de_kg_morango > 5 and quantidade_de_kg_maçã and quantidade_de_kg_morango < 10:

        # CONDIÇÃO(1.2) >5 e <10

    preço_da_maçã = quantidade_de_kg_maçã * 1.5
    preço_do_morango = quantidade_de_kg_morango * 2.2

    print(f'\nVocê aqueriu {quantidade_de_kg_maçã} kg de maçã por R$ {preço_da_maçã:.2f} reais.')
    print(f'Voc adqueriu {quantidade_de_kg_morango} kg de morango por R$ {preço_do_morango:.2f} reias.')
elif quantidade_de_kg_morango and quantidade_de_kg_maçã <= 5:

        # CONDIÇÃO(1.3) <= 5

    preço_da_maçã2 = quantidade_de_kg_maçã * 1.8
    preço_do_morango2 = quantidade_de_kg_morango * 2.5

    print(f'\nVocê aqueriu {quantidade_de_kg_maçã} kg de maçã por R$ {preço_da_maçã2:.2f} reais.')
    print(f'Voc adqueriu {quantidade_de_kg_morango} kg de morango por R$ {preço_do_morango2:.2f} reias.')

        # CONDIÇÃO 2

elif quantidade_de_kg_maçã and quantidade_de_kg_morango > 10:

        # CONDIÇÃO(2.1) > 10
    preço_da_maçã3 = quantidade_de_kg_maçã * 1.5
    preço_do_morango3 = quantidade_de_kg_morango * 2.2
    porcentagem = preço_da_maçã3 * 10
    desconto_maçã_aplicado = porcentagem/100
    desconto_maçã = preço_da_maçã3 - desconto_maçã_aplicado
    desconto_morango = preço_do_morango3 - desconto_maçã_aplicado
    print(f'\nVocê aqueriu {quantidade_de_kg_maçã} kg de maçã por R$ {preço_da_maçã3:.2f} reais com DESCONTO 10%.')
    print(f'Voc adqueriu {quantidade_de_kg_morango} kg de morango por R$ {preço_do_morango3:.2f} reias DESCONTO 10%.')
print('FIM.')







    

