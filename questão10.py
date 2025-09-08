import os
os.system('cls')

		#ANUNCIADO

print('''
==========================================
Combustível - Quantidade Vendida - Desconto por Litro

Álcool - Até 25 litros - 10%

Álcool - Acima de 25 litros - 20%

Gasolina - Até 25 litros - 15%

Gasolina - Acima de 25 litros - 30%
==========================================''')

		#CODIGOS

litros = int(input('\nDigite a quantidade de litros: '))

preço_gasolina = 6.59 * litros
preço_alcool = 3.79 * litros

print('A = ÀLCOOL\nG = GASOLINA')
tipo_de_gasolina = input('Digite o tipo de gasolina: ').upper()
while tipo_de_gasolina not in 'A' 'G' 'GASOLINA' 'ALCOOL' 'ÀLCOOL':
	print('ERRO.\nDIGITE NOVAMENTE.')
	tipo_de_gasolina = input('Digite o tipo de gasolina: ').upper()

		#CONDIÇÕES 1
		
if tipo_de_gasolina == 'A' 'ALCOOL' 'ÁLCOOL':
	if litros > 25:
			print(f'*{tipo_de_gasolina}* SELECIONADO\n20% de DESCONTO\nTOTAL: R${preço_alcool - (preço_alcool * 0.20)}')
	elif litros > 25:
			print(f'*{tipo_de_gasolina}* SELECIONADO\n30% de DESCONTO\nTOTAL: R${preço_gasolina - (preço_gasolina * 0.30)}')

		#CONDIÇÃO 2

elif litros >= 1 and litros <= 25:
	if tipo_de_gasolina == 'A' 'ALCOOL':
			print(f'*{tipo_de_gasolina}* SELECIONADO\n20% de DESCONTO\nTOTAL: R${preço_alcool - (preço_alcool * 0.10)}')
	elif tipo_de_gasolina == 'G' 'GASOLINA':
			print(f'*{tipo_de_gasolina}* SELECIONADO\n30% de DESCONTO\nTOTAL: R${preço_gasolina - (preço_gasolina * 0.15)}')
print('FIM.')
