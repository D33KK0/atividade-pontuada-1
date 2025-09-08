import os
os.system('cls')

		#ANUNCIADO

print('''
=============PRODUTOS=============
MACARRÃO R$10(UNI)
FEIJÃO 1kg R$8(UNI)
ARROZ 1kg R$7(UNI)
CARNE DE PORCO R$16(UNI)

OBS: Se quantidade <= 5, o desconto será de 2%.
Se quantidade > 5 e quantidade <= 10, o desconto será de 3%.
Se quantidade > 10, o desconto será de 5%.
''')

		#NOME DO PRODUTO

nome_do_produto = input('Digite o nome do produto: ').upper()
while nome_do_produto not in 'MACARRÃO' 'FEIJÃO' 'ARROZ' 'CARNE DE PORCO':
	print('ERRO.')
	nome_do_produto = input('Digite o nome do produto novamente: ').upper()

		#CONDIÇÃO 1

if nome_do_produto == 'MACARRÃO':
	print(f'\n*{nome_do_produto}* R$10 SELECIONADO!')
elif nome_do_produto == 'FEIJÃO':
	print(f'\n*{nome_do_produto}* R$8 SELECIONADO!')
elif nome_do_produto == 'ARROZ':
	print(f'\n*{nome_do_produto}* R$7 SELECIONADO!')
elif nome_do_produto == 'CARNE DE PORCO':
	print(f'\n*{nome_do_produto}* R$16 SELECIONADO!')
else:
	print('.')

		#QUANTIDADE

quantidade = float(input('\nDigite a quantidade: '))

		#CALCULO DOS PREÇOS

preço_macarrão = quantidade * 10
preço_feijão = quantidade * 8
preço_arroz = quantidade * 7
preço_carne_de_porco = quantidade * 16

		#CONDIÇÕES 2

		# MENOR OU IGUAL A 5.
##
if quantidade <= 5:
	match nome_do_produto:
		case 'MACARRÃO':
			print(f'{nome_do_produto} R$10 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_macarrão * 0.02)} reais')
		case 'FEIJÃO':
			print(f'{nome_do_produto} R$8 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_feijão * 0.02)} reais')
		case 'ARROZ':
			print(f'{nome_do_produto} R$7 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_arroz * 0.02)} reais')
		case 'CARNE DE PORCO':
			print(f'{nome_do_produto} R$16 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_carne_de_porco * 0.02)} reais')
	
##
		# ENTRE 5 E 10.
##
elif quantidade > 5 and quantidade <= 10:
	match nome_do_produto:
		case 'MACARRÃO':
			print(f'{nome_do_produto} R$10 reais\n{quantidade} UNI. (-3%) = R${preço_feijão - (preço_macarrão * 0.03)} reais')
		case 'FEIJÃO':
			print(f'{nome_do_produto} R$8 reais\n{quantidade} UNI. (-3%) = R${preço_feijão - (preço_feijão * 0.03)} reais')
		case 'ARROZ':
			print(f'{nome_do_produto} R$7 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_arroz * 0.03)} reais')
		case 'CARNE DE PORCO':
			print(f'{nome_do_produto} R$16 reais\n{quantidade} UNI. (-3%) = R${preço_macarrão - (preço_carne_de_porco * 0.03)} reais')
##	
		# MAIOR QUE 10.
##
elif quantidade > 10:
	match nome_do_produto:
		case 'MACARRÃO':
			print(f'{nome_do_produto} R$10 reais\n{quantidade} UNI. (-5%) = R${preço_macarrão - (preço_macarrão * 0.05)} reais')
		case 'FEIJÃO':
			print(f'{nome_do_produto} R$8 reais\n{quantidade} UNI. (-5%) = R${preço_feijão - (preço_feijão * 0.05)} reais')
		case 'ARROZ':
			print(f'{nome_do_produto} R$7 reais\n{quantidade} UNI. (-5%) = R${preço_arroz - (preço_arroz * 0.05)} reais')
		case 'CARNE DE PORCO':
			print(f'{nome_do_produto} R$16 reais\n{quantidade} UNI. (-5%) = R${preço_carne_de_porco - (preço_carne_de_porco * 0.05)} reais')
print('FIM.')
	

