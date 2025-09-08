import os
os.system('cls')

		#TABELA DE PREÇOS

print('''
      CD's À VENDA
=========================
Verde R$ 10,00
Azul R$ 20,00
Amarelo R$ 30,00
Vermelho R$ 40,00
=========================''')

		#CODIGOS WHILE

cor = input('\nDigite a cor referente ao produto: ').upper()
while cor not in 'VERDE' 'AZUL' 'AMARELO' 'VERMELHO':
	print('ERRO')
	cor = input('Digite a cor referente ao produto novamente: ').upper()

		#CONDIÇÃO MATCH

match cor:
	case 'VERMELHO':
		print(f'\nCOR: *{cor}* SELECIONADO\nR$40,00 reais')
	case 'AMARELO':
		print(f'\nCOR: *{cor}* SELECIONADO\nR$30,00 reais')
	case 'AZUL':
		print(f'\nCOR: *{cor}* SELECIONADO\nR$20,00 reais')
	case 'VERDE':
		print(f'\nCOR: *{cor}* SELECIONADO\nR$10,00 reais')
print('FIM.')