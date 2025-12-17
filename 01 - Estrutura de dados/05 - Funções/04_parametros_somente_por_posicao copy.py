def criar_carro(modelo, ano, placa, /, chassi, marca, * ,  motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel, chassi)


criar_carro("Palio", 1999, "ABC-1234", "123456999", marca = "Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido
