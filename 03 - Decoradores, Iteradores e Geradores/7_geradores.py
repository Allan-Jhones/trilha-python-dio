def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2


for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)


def meu_gerador():
    texto = "python"
    yield texto

for i in meu_gerador():
    print(i)