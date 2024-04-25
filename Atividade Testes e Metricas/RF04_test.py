def operacao_and_binaria(binario1, binario2):
    # Converter os números binários para inteiros
    num1 = int(binario1, 2)
    num2 = int(binario2, 2)
    
    # Realizar a operação lógica AND
    resultado = num1 & num2
    
    # Converter o resultado de volta para binário
    resultado_binario = bin(resultado)[2:]
    
    return resultado_binario

# Exemplo de uso:
try:
    binario1 = input("Digite o primeiro número binário: ")
    binario2 = input("Digite o segundo número binário: ")

    resultado = operacao_and_binaria(binario1, binario2)
    print(f"Resultado da operação AND: {resultado}")
except ValueError:
    print("Por favor, insira um número binário válido.")


input("Pressione Enter para sair...")