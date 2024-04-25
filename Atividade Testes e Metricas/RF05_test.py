import re

def valida_placa(placa):
    # Remover espaços em branco e converter para maiúsculas
    placa = placa.strip().upper()
    
    # Verificar se a placa tem o formato correto (3 letras seguidas de 4 números)
    if not re.match(r'^[A-Z]{3}\d{4}$', placa):
        return "Inválido"
    
    # Placa válida
    return "Válido"

# Exemplo de uso:
placa = input("Digite a placa do veículo: ")
resultado = valida_placa(placa)
print(f"A placa é {resultado}.")

input("Pressione Enter para sair...")