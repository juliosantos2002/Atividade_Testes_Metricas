def converter_real_para_dolar(valor_real, taxa_cambio):
    valor_dolar = valor_real / taxa_cambio
    return valor_dolar

# Exemplo de uso:
try:
    valor_real = float(input("Digite o valor em reais: "))
    taxa_cambio = float(input("Digite a taxa de câmbio atual (EX: 5.20): "))

    valor_convertido = converter_real_para_dolar(valor_real, taxa_cambio)
    print(f"Valor convertido em dólar: ${valor_convertido:.2f}")
except ValueError:
    print("Por favor, insira um valor numérico válido.")
    
input("Pressione Enter para sair...")
