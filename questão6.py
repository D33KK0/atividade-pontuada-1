import os
os.system('cls')
from emoji import emojize

		#INTRODUÇÃO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

		#CONDIÇÕES

if media >= 6:
	print(emojize(f'Sua média é {media}: APROVADO ✔️'))
elif media >= 4.1 < 6:
	print(emojize(f'Sua média é {media}: RECUPERAÇÃO 🙁', ))
elif media < 4:
	print(emojize(f'Sua média é {media}: REPROVADO ❌'))
