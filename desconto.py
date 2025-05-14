produto = input("produto:")
valor_total = int(input('preço:'))
porcentagem = int(input("porcentagem de desconto:"))
desconto = valor_total *(porcentagem/100)
valor_novo = valor_total-desconto 
print("O valor total do produto é de", valor_total, "com o desconto de", desconto, "ficara por", valor_novo)

print(f"O valor total do produto é de {valor_total} com desconto de {desconto} ficara por {valor_novo}")
