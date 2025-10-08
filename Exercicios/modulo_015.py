carros_garagem = []

def carros_características(fabricante, modelo, **infos):
    carro_infos = {}

    carro_infos["fabricante"] = fabricante
    carro_infos["modelo"] = modelo

    for chave, valor in infos.items():
        carro_infos[chave] = valor

    carros_garagem.append(carro_infos)

    print(carro_infos)
    print()

def apresentar_carros(lista):
    for x, item in enumerate(lista, 1):
        print(f"\n{x}º Automóvel:")
        for chave, valor in item.items():
            if chave == "fabricante":
               print(f"\t{chave}: {valor.upper()}")
            else:
               print(f"\t{chave}: {valor}")