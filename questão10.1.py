# Preços por litro
PRECO_ALCOOL = 3.79
PRECO_GASOLINA = 6.59

# Entrada de dados
litros = float(input("Digite a quantidade de litros vendidos: "))
tipo = input("Digite o tipo de combustível (A para álcool, G para gasolina): ").upper()

# Cálculo do desconto
if tipo == 'A':
    if litros <= 25:
        desconto = 0.10  # 10%
    else:
        desconto = 0.20  # 20%
    preco_base = PRECO_ALCOOL
elif tipo == 'G':
    if litros <= 25:
        desconto = 0.15  # 15%
    else:
        desconto = 0.30  # 30%
    preco_base = PRECO_GASOLINA
else:
    print("Tipo de combustível inválido.")
    exit()

# Cálculo do valor com desconto
valor_bruto = litros * preco_base
valor_desconto = valor_bruto * desconto
valor_final = valor_bruto - valor_desconto

# Saída
print(f"\nResumo da Compra:")
print(f"Tipo de combustível: {'Álcool' if tipo == 'A' else 'Gasolina'}")
print(f"Litros vendidos: {litros:.2f} L")
print(f"Preço por litro: R$ {preco_base:.2f}")
print(f"Desconto aplicado: {desconto * 100:.0f}%")
print(f"Valor a ser pago: R$ {valor_final:.2f}")
