quant_vendas = int(input("Quantas vendas foram realizadas hoje? "))

soma_vendas = 0
quant_vendas100 = 0
quant_vendas50 = 0
vendas = []
maior_venda = 0

for i in range(quant_vendas):
    valor_vendas = float(input(f"Digite o valor da {i+1}° venda: "))
    soma_vendas += valor_vendas
    vendas.append(valor_vendas)

    if valor_vendas > 100:
        quant_vendas100 += 1

    if valor_vendas < 50:
        quant_vendas50 += 1

valor_medio = soma_vendas / quant_vendas
percentual_acima_100 = (quant_vendas100 * 100) / quant_vendas

maior_venda = max(vendas)
menor_venda = min(vendas)
vendas_acima_media = 0
for valor in vendas:
    if valor > valor_medio:
        vendas_acima_media += 1

print("\n========= RELATÓRIO DO DIA =========")
print(f"Quantidade de vendas realizadas: {quant_vendas}")
print(f"Valor total vendido: R${soma_vendas:.2f}")
print(f"Valor medio das vendas: R${valor_medio:.2f}")
print(f"Quantidade de vendas acima de R$100.00: {quant_vendas100}")
print(f"Quantidade de vendas abaixo de R$50.00: {quant_vendas50}")
print(f"Percentual de vendas que foram acima de R$100.00: {percentual_acima_100:.2f}%")
print(f"Maior valor de venda: R${maior_venda:.2f}")
print(f"Menor valor de venda: R${menor_venda:.2f}")
print(f"Quantidade de vendas que tiveram valor acima da media: {vendas_acima_media}")

print("\nEncerrando caixa em...")
for i in range(5, 0, -1):
    print(i)
print("Caixa encerrado!")
