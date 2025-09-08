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

OBS: Acima ou igual 10kg e preço maior que R$ 15,00 reias - !! 10% desconto !!''')

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
		desconto_morango = preço_do_morango3 - (preço_do_morango3 * 0.10)
		desconto_da_maçã = preço_da_maçã3 - (preço_da_maçã3 * 0.10)
		print(f'''\nVocê aqueriu {quantidade_de_kg_maçã} kg de maçã por R$ {desconto_da_maçã:.2f} reais com DESCONTO 10%.
Voc adqueriu {quantidade_de_kg_morango} kg de morango por R$ {desconto_morango:.2f} reias DESCONTO 10%.')
''')
				#CONDIÇÃO 3
elif preço_da_maçã and preço_do_morango > 15:
		preço_da_maçã4 = quantidade_de_kg_maçã * 1.5
		preço_do_morango4 = quantidade_de_kg_morango * 2.2
		desconto_morango = preço_do_morango4 - (preço_do_morango4 * 0.10)
		desconto_da_maçã = preço_da_maçã4 - (preço_da_maçã4 * 0.10)
		print(f'''\nVocê aqueriu {quantidade_de_kg_maçã} kg de maçã por R$ {desconto_da_maçã:.2f} reais com DESCONTO 10%.
Voce adqueriu {quantidade_de_kg_morango} kg de morango por R$ {desconto_morango:.2f} reias DESCONTO 10%.')
''')
