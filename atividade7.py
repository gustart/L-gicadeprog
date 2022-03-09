val_produto =  float(input("Digite o valor do produto: "))
porcentagem1 = 10 / 100
porcentagem2 = 20 / 100
desconto  = val_produto * porcentagem1
valor_com_desconto = val_produto -  desconto 
juros = val_produto * porcentagem2
val_com_juros = val_produto + juros
val_parcelado_juros = val_com_juros / 10
parcelado = val_produto / 5


print(f"O produto custa: {val_produto}")
print(f"valor do pagamento a vista {valor_com_desconto}")
print(f"5x de {parcelado} sem juros")
print(f"Valor do produto dividido em 10 com 20% de juros: {val_parcelado_juros}, Totalizando {val_com_juros}")