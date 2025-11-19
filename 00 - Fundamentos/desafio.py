# Separar as funções existentes de saque, depósito e extrato em funções.
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

# Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes:
# sacar, depositar e visualizar histórico. Além disso, para a vesão 2 do sistema precisamos criar duas novas funções:
# criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

# Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada
# função vai ter uma regra de passagem de argumentos. O retorno e aforma como serão chamadas, pode ser definida por
# você da forma que achar melhor.

# A função saque deve receber os argumentos apenas por nome (keyword only). Sugestão de argumentos: saldo, valor,
# extrato, limite, numero_saques, limite_saques. Sugestão de retorno: saldo e extrato.

# A função depósito deve receber os argumentos apenas por posição (positional only). Sugestão de argumentos: saldo,
# valor, extrato. Sugestão de retorno: saldo e extrato.

# A função extrato deve receber os argumentos por posição e nome (positional only e keyword only). Argumentos posionais:
# saldo; argumentos nomeados: extrato.

# Precisamos criar duas novas funções: criar usuário e criar conta corrente. Fique a vontade para adicionar mais
# funções, por exemplo: listar contas.

# O programa deve armazenar os usuários em uma lista, um usuário é composto por: nome, data de nascimento, cpf e
# endereço. O endereço é uma string com o formato: logradouro, nro- bairro - cidade/sigla estado. Deve ser armazenado
# somente os números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

# O programa deve armazenar contas em uma lista. Uma conta é composta por: agência, número da conta e usuário.
# O número da conta é sequencial, iniciando em 1. O número da agência é fixo: "0001". O usuário pode ter mais de uma conta,
# mas uma conta pertence a somente um usuário.

# Para vincular um usuário a uma conta, filtre a lista de usuários buscando o número do cpf informado para cada
# usuário da lista.

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
tupla = ()
def setDeposito(valor, saldo):
    saldo += valor
    return saldo

def addMensagemExtrato (extrato, /, valor, mensagem):
    extrato += f"{mensagem} {valor:.2f}\n"
    return extrato

def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo = setDeposito(valor, saldo)
        extrato = addMensagemExtrato(extrato, valor, "Deposito : R$")
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")
        return


def sacar(saldo, valor, extrato):
    saldo -= valor
    extrato = addMensagemExtrato(extrato, valor, "Saque: R$ " )
    return saldo, extrato

def incrementaSaque(numeroSaques):
    return numeroSaques + 1

while True:

    opcao = input(menu)

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo, extrato = sacar(saldo, valor, extrato)
            numero_saques  = incrementaSaque(numero_saques)

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
