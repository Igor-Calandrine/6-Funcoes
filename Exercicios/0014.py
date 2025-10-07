"""Carros: Escreva uma função que armazene informações sobre um carro em um dicionário. A função sempre deve  receber o nome de um fabricante e um modelo. Um número arbitrário de argumentos nomeados então deverá ser aceito.
Chame a função com as informações necessárias e dois outros pares nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser apropriada para uma chamada como esta:"""

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
 

carros_características("citroen", "c3", cor="cinza", câmbio="manual")
carros_características("pegeout", "208", cor="azul", câmbio="automático")
carros_características("wolks", "gol", cor="preto", câmbio="manual")
apresentar_carros(carros_garagem)