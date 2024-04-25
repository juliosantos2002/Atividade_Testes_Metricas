import re
from datetime import datetime

def valida_cartao(numero, nome, validade, codigo_seguranca):
    # Validar número do cartão (16 dígitos)
    if not re.match(r'^\d{16}$', numero):
        return ("Inválido", "Compra negada")
    
    # Validar nome do titular (não pode ser vazio)
    if not nome:
        return ("Inválido", "Compra negada")
    
    # Validar formato de validade (MM/AA)
    try:
        validade_dt = datetime.strptime(validade, '%m/%y')
    except ValueError:
        return ("Inválido", "Compra negada")
    
    # Validar código de segurança (3 dígitos)
    if not re.match(r'^\d{3}$', codigo_seguranca):
        return ("Inválido", "Compra negada")
    
    # Verificar se a data de validade está no futuro
    if validade_dt < datetime.now():
        return ("Inválido", "Compra negada")
    
    # Cartão válido e compra autorizada
    return ("Válido", "Compra autorizada")

# Exemplo de uso:
numero_cartao = input("Digite o número do cartão: ")
nome_titular = input("Digite o nome do titular: ")
validade = input("Digite a validade (MM/AA): ")
codigo_seguranca = input("Digite o código de segurança: ")

resultado_validacao, resultado_compra = valida_cartao(numero_cartao, nome_titular, validade, codigo_seguranca)
print(f"Resultado da validação: {resultado_validacao}")
print(f"Resultado da compra: {resultado_compra}")


input("Pressione Enter para sair...")