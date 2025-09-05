import os
os.system('cls')

        #COMANDOS 0

nome = input('Digite seu nome: ')
print('''
  DIGITE SEU SEXO!

M = MASCULINO
F = FEMININO
      
      |
      ''')

        #LER SEXO ABAIXO 1

sexo = str(input('Qual seu sexo(M/F): ')).upper()
while sexo not in 'M' 'F':
    print('Erro.')
    sexo = str(input('Digite seu sexo novamente (M/F): ')).upper()
if sexo == 'M':
    print(f'''
    PERFEITO!
          
SEXO "MASCULINO" selecionado.
          ''')
    
        #LER SEXO ABAIXO 1.2 

elif sexo == 'F':
    print(f'''
    PERFEITO!
          
SEXO "FEMINIO" selecionado.
          ''')
    
        #LER ESTADO CIVIL BAIXO 2

estado_civil = input('Digite seu estado civil  S = SOLEIRO(A) ou C = CASADO(A): ').upper()
while estado_civil not in 'S' 'C':
    print('ERRO.')
    print('OBS: Escreva "S" ou "C", por favor.')
    estado_civil = input('Digite seu estado civil, novamente  S = SOLEIRO(A) ou C = CASADO(A): ').upper()
if estado_civil == 'C':

                #CASO SEJA FEMININO ESTADO CIVIL 2.1
                
    match sexo:
        case 'F': #SEXO FEMININO NA CONDIÇÃO DE SER CASADA (ESTADO CIVIL) 2.1
            tempo_de_casamento = float(input('Tempo de casameto em ANOS (caso seja em meses, use um número fracional. EX: 1, 2, 3 meses (0.1, 0.2, 0.3...), por favor): '))
            if tempo_de_casamento < 1:
                print(f'''\nNOME: {nome}
                \nSEXO: {sexo}
                \nESTADO CIVIL {estado_civil} 
                \nTEMPO DE CASAMENTO: {tempo_de_casamento} meses
                        ''')
            else:
                print(f'''\nNOME: {nome})
                \nSEXO: {sexo}
                \nESTADO CIVIL {estado_civil}
                \nTEMPO DE CASAMETO {tempo_de_casamento} anos
                        ''')

                #CASO SEJA MASCULINO NA CONDIÇÃO DE SER CASADO (ESTADO CIVIL) 2.2

        case 'M': #CASO SEJA MASCULINO ESTADO CIVIL 2.2
            print(f'''\nNOME: {nome}
            \nSEXO: {sexo}
            \nESTADO CIVIL {estado_civil}
                    ''')
            
                #CASO SEJA MASCULINO ESTADO CIVIL 3
                
if estado_civil == 'S':
    print(f'''\nNOME: {nome}
    \nSEXO: {sexo}
    \nESTADO CIVIL {estado_civil}
            ''')
print('FIM.')

            #FINAL




#           #               #           #            #OPÇÃO DE REINICIO #            #           #               #               #




reinicio = input('Quer tentar de novo? (S/N): ').upper()
if reinicio == 'S':
    nome = input('Digite seu nome: ')
print('''
  DIGITE SEU SEXO!

M = MASCULINO
F = FEMININO
      
      |
      ''')

        #LER SEXO ABAIXO 1

sexo = str(input('Qual seu sexo(M/F): ')).upper()
while sexo not in 'M' 'F':
        print('Erro.')
sexo = str(input('Digite seu sexo novamente (M/F): ')).upper()
if sexo == 'M':
        print(f'''
    PERFEITO!
          
SEXO "MASCULINO" selecionado.
          ''')
    
        #LER SEXO ABAIXO 1.2 

elif sexo == 'F':
        print(f'''
    PERFEITO!
          
SEXO "FEMINIO" selecionado.
          ''')
    
        #LER ESTADO CIVIL BAIXO 2

estado_civil = input('Digite seu estado civil  S = SOLEIRO(A) ou C = CASADO(A): ').upper()
while estado_civil not in 'S' 'C':
        print('ERRO.')
        print('OBS: Escreva "S" ou "C", por favor.')
estado_civil = input('Digite seu estado civil, novamente  S = SOLEIRO(A) ou C = CASADO(A): ').upper()
if estado_civil == 'C':

                #CASO SEJA FEMININO ESTADO CIVIL 2.1
                
        match sexo:
            case 'F': #SEXO FEMININO NA CONDIÇÃO DE SER CASADA (ESTADO CIVIL) 2.1
                tempo_de_casamento = float(input('Tempo de casameto em ANOS (caso seja em meses, use um número fracional. EX: 1, 2, 3 meses (0.1, 0.2, 0.3...), por favor): '))
                if tempo_de_casamento < 1:  
                    print(f'''\nNOME: {nome}
                \nSEXO: {sexo}
                \nESTADO CIVIL {estado_civil} 
                \nTEMPO DE CASAMENTO: {tempo_de_casamento} meses
                        ''')
                else:
                    print(f'''\nNOME: {nome})
                \nSEXO: {sexo}
                \nESTADO CIVIL {estado_civil}
                \nTEMPO DE CASAMETO {tempo_de_casamento} anos
                        ''')

                #CASO SEJA MASCULINO NA CONDIÇÃO DE SER CASADO (ESTADO CIVIL) 2.2

            case 'M': #CASO SEJA MASCULINO ESTADO CIVIL 2.2
                print(f'''\nNOME: {nome}
            \nSEXO: {sexo}
            \nESTADO CIVIL {estado_civil}
                    ''')
            
                #CASO SEJA MASCULINO ESTADO CIVIL 3
                
if estado_civil == 'S':
        print(f'''\nNOME: {nome}
    \nSEXO: {sexo}
    \nESTADO CIVIL {estado_civil}
            ''')
print('FIM.')

            #FINAL
reinicio = input('Quer tentar de novo? (S/N): ').upper()
print('FIM.')







