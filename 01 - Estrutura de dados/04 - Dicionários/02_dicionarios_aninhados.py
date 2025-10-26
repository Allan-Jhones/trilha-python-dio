#Dicionários podem armazenar qualquer tipo de objeto Python
#como valor, desde que a chave para esse valor seja um objeto
#imutável como (strings e numeros)
contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766", "extra":{"a": 1}},
}

telefone = contatos["melaine@gmail.com"]["extra"]["a"]
nome = contatos["melaine@gmail.com"]["nome"]
print (nome)
print(telefone)
