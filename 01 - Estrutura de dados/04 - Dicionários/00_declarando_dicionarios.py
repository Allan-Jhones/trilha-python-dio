#Um dicionário é um conjunto não-ordenado de pares
#chave:valor, onde as chaves são únicas em uma dada instância
#do dicionário. Dicionários são delimitados por chaves: {}, e
#contém uma lista de pares chave:valor separadas por vírgulas.
pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)
