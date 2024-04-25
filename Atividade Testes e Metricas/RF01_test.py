# Aluno: Júlio César Abreu dos Santos
# R.A: 00019161

def valida_cpf(cpf):
    # Remover caracteres não numéricos do CPF
    cpf = ''.join(filter(str.isdigit, cpf))

    # Verificar se o CPF tem 11 dígitos
    if len(cpf) != 11:
        return False

    # Verificar se todos os dígitos são iguais (ex: 111.111.111-11)
    if cpf == cpf[0] * 11:
        return False

    # Calcular o primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = 11 - (soma % 11)
    digito1 = resto if resto < 10 else 0

    # Verificar o primeiro dígito verificador
    if digito1 != int(cpf[9]):
        return False

    # Calcular o segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = 11 - (soma % 11)
    digito2 = resto if resto < 10 else 0

    # Verificar o segundo dígito verificador
    if digito2 != int(cpf[10]):
        return False

    # CPF válido
    return True

# Exemplo de uso:
cpf = input("Digite o CPF para validar: ")
if valida_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")

input("Pressione Enter para sair...")