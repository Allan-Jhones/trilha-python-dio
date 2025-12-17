# Separar as funções existentes de saque, depósito e extrato em funções.
# Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.
import textwrap


# Precisamos deixar nosso código mais modularizado, para isso vamos criar funções para as operações existentes:
# sacar, depositar e visualizar histórico. Além disso, para a vesão 2 do sistema precisamos criar duas novas funções:
# criar usuário (cliente do banco) e criar conta corrente (vincular com usuário).

# Devemos criar funções para todas as operações do sistema. Para exercitar tudo o que aprendemos neste módulo, cada
# função vai ter uma regra de passagem de argumentos. O retorno e a forma como serão chamadas, pode ser definida por
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


def menu():
    menu = """

    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo usuário
    [q]\tSair

    => """
    return input(textwrap.dedent(menu))



def criar_usuario():
    nome = str(input("Digite seu nome: "))
    dataNascimento = int(input("Digite sua data de nascimento: "))
    cpf = str(input("Digite seu CPF: "))
    endereco = str("Informe o seu endereço: ")
    usuario = []
def get_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def set_deposito(valor, saldo, /):
    saldo += valor
    return saldo

def add_mensagem_extrato (extrato, /, valor, mensagem):
    extrato += f"{mensagem} {valor:.2f}\n"
    return extrato

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo = set_deposito(valor, saldo)
        extrato = add_mensagem_extrato(extrato, valor, "Deposito : R$")
        return saldo, extrato
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, extrato, limite, numero_saques, limite_saques):
    valor = float(input("Informe o valor do saque: "))
    excedeu_saldo = valor > saldo
    excedeu_limte = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print ("Operação falhou! Você não tem saldo suficiente!")
    elif excedeu_limte:
        print ("Operação falhou! O valor do saque excede o limite!")
    elif excedeu_saques:
        print ("Operação falhou! Número máximo de saques excedido!")
    elif valor > 0:

        saldo -= valor
        extrato = add_mensagem_extrato(extrato, valor, "Saque: R$ " )
        numero_saques += 1
        print ("Saque realizado com sucesso!")
    else:
        print ("Operação falhou! O valor informado é inválido!")

    return saldo, extrato

def incrementa_saque(numero_saques):
    return numero_saques + 1

def criar_usuario(usuarios):
    cpf = str(input("Digite seu CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print ("Já existe usuario com esse CPF!")
        return
    nome = str(input("Informe o nome completo: "))
    data_nascimento = str(input("Digite sua data de nascimento: (dd-mm-aaaa)"))
    endereco = str(input("Informe o endereço completo (logradouro, numero - bairro - cidade/sigla estado: "))
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuario criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = str(input("Informe o seu CPF: "))
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuário não encontrado! Verifique sua conta.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
                AGENCIA:\t{conta["agencia"]}
                C/C:\t{conta["numero_conta"]}
                TITULAR:\t{conta["usuario"]["nome"]}
            """
        print ("="*30)
        print (textwrap.dedent(linha))
def main ():
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    contas = []
    listaUsuarios = []

    while True:
        opcao = menu()
        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == "e":
            get_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(listaUsuarios)

        elif opcao == "nc":
          numero_conta = len(contas) + 1
          conta = criar_conta(AGENCIA, numero_conta, listaUsuarios)

          if conta:
              contas.append(conta)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
