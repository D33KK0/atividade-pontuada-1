import os
os.system('cls')

#SO PODE PEGAR UM EMPRESTIMO ATÉ 10x O VALOR DA RENDA MENSAL
#VALOR DA PRESTAÇÃO POR MÊS 30% da RENDA DO SOLICITANTE

print('''O EMPRÉSTIMO SO ACORRERÁ CASO O VALOR SOLICITADO SEJA ATÉ 10x\nO VALOR DA RENDA MENSAL DO SOLICITANTE.
A PRESTAÇÃO SO OCORRERA CASO SEJA 30% DA RENDA MENSAL DO SOLICITANTE''')

		#ANUNCIADO

renda_mensal = float(input('\nDigite sua renda mensal(Ex: R$1,200.00 reais) - R$: '))
emprestimo = float(float(input('EMPRESTIMO: ')))
parcela = float(input('Quantas Prestações/Parcelas(Ex: 10 meses): '))
valor_total_para_emprestimo = renda_mensal * 10
valor_a_ser_pago_mensalmente = emprestimo / parcela
trinta_port_cento_do_salario = (30/100) * renda_mensal

		#CONDIÇÃO

if emprestimo > (renda_mensal * 10):
	print(f'Você só pode pegar um empréstimo 10x da sua Renda Mensal.\nRENDA: R${renda_mensal}\nLIMITE DE EMPRÉSTIMO: R${valor_total_para_emprestimo} reis\nEMPRÉSTIMO SOLICITADO: R${emprestimo}')
else:
	if valor_a_ser_pago_mensalmente > trinta_port_cento_do_salario:
		print(f'Você ULTRAPASSOU o limite de prestação(30% SALARIO = {trinta_port_cento_do_salario:.3f}) permitido pela Instituição.\nEMPRÉSTIMO: R$ {emprestimo:.3f} reais.\nPARCELA/MÊS {parcela}x: R${valor_a_ser_pago_mensalmente} reais.')
	else:
		print(f'RENDA: {renda_mensal}\nEMPRÉSTIMO: {emprestimo}\nPARCELA/MÊS {parcela}x: R$ {valor_a_ser_pago_mensalmente:.2f} reais.')
print('FIM.')
