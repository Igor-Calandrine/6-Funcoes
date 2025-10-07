"""Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma função chamada show_magicians() que exiba o nome de cada mágico da lista."""

magicos = ["harry houdini","david copperfield", "criss angel", "dynamo", "penn & teller"]

def exibir_nomes(nomes):
    print("Lista de famosos mágicos:")
    for nome in nomes:
        print(f"\t* {nome.title()}")

exibir_nomes(magicos)