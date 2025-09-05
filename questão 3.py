import os
os.system('cls')

#EXECUÇÃO COMANDOS

A = int(input('Digite um número: '))
B = int(input('Digite outro número: '))
C1_adição = A + B
C2_multiplicação = A * B

#CONDIÇÕES

if A > B or A < B:
    print(f'A multiplicação de {A} por {B} é igual a {C2_multiplicação}.')
elif A == B:
    print(f'Os números {A} e {B} são iguais. Portanto, a soma é {C1_adição}.')
print('FIM.')