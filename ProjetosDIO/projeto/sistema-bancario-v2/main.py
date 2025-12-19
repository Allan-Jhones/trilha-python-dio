import textwrap
from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod
from datetime import datetime


class Historico:
    def __init__(self):
        self.transacoes = []
    def transacoes(self):
        return self.transacoes
    def adicionar_transacao(self, transacao):
        self.transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        })
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    @classmethod
    def registrar(self, conta):
        pass


class Conta:

    def __init__(self, saldo, numero, cliente):
        self._saldo = saldo
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def __str__(self):
        pass

    def __del__(self):
        print("Removendo instância de conta")

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print ("Deposito realizado com sucesso!")
        else:
            print ("O valor informado é inválido!")
            return False
        return True 

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo
        if excedeu_saldo:
            print("Saldo insuficiente")
        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        else:
            print("O valor informado é inválido.")
        return False


    def criar_conta(self, saldo, numero, agencia, cliente, historico):
        conta = Conta(self.saldo, self.numero, self.agencia, self.cliente, self)
        self.lista_de_contas.append(conta)

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque=3):
        super.__init__(numero, cliente)
        self.limite = limite
        self.limite_saque = limite_saque

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saque
        if excedeu_limite:
            print("O valor do saque excede o limite!")
        elif excedeu_saques:
            print("Número máximo de saques excedido!")
        else:
            return super().sacar(valor)

        def __str__(self):
            return f"""\
            Agência:\t{self.agencia}
            C/C:\t{self.numero}
            Titular:\t{self.cliente.nome}
            """

class Transacao(ABC):
    pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

class Deposito(Transacao):
    pass

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def __str__(self):
        pass

    def __del__(self):
        print("Removendo instância de Cliente")

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf



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
        print ("Saque realizado com sucesso!")
    else:
        print ("Operação falhou! O valor informado é inválido!")
    return saldo, extrato


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
            aux_saldo = saldo
            saldo, extrato = sacar(
                saldo=saldo,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques = LIMITE_SAQUES
            )
            if aux_saldo != saldo:
                numero_saques += 1

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