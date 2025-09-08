import os
from re import A

os.system('cls')

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

	#CALCULOS/OPERAÇÕES

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2

opr = str(input('Digite a operação que deseja (+, -, *, /): ')) #PARTE DO QUESTIONAMENTO 1

	#FIM DO "PARTE DO QUESTIONAMENTO 1".

while opr not in '+' '-' '*' '/':
	opr = input('Operação inválida. Digite umas das operações (+, -, *, /): ') #   QUESTIONAMENTO 2
match opr:
	case '+':
		print(f'Adição: {soma}')
	case '-':
		print(f'Subtração: {subtracao}')
	case '*':
		print(f'Multiplicação: {multiplicacao:.2f}')
	case '/':
		print(f'Divisão: {divisao:.2f}')
print('FIM.')