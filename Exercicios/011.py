"""Mágicos inalterados: Comece com o trabalho feito no anterior. Chame a função make_great() com uma cópia da lista de nomes de mágicos. Como a lista original não será alterada, devolva a nova lista e armazene-a em uma
lista separada. Chame show_magicians() com cada lista para mostrar que você tem  uma  lista  de  nomes  originais  e  uma  lista  com  a  expressão  o  Grande adicionada ao nome de cada mágico."""

magicos = ["harry houdini","david copperfield", "criss angel", "dynamo", "penn & teller"]

def exibir_nomes(nomes):
    print("Lista de famosos mágicos:")
    for nome in nomes:
        print(f"\t* {nome.title()}")

def grande_magico(nomes):
    i=0
    while i < len(nomes):
        nome_atual = nomes.pop(0)
        frase = f"\tO grande {nome_atual.title()}"
        nomes.append(frase)
        i = i + 1
    
    print("Os grande mágicos:")
    for nome in nomes:
        print(nome)
    
exibir_nomes(magicos)
grande_magico(magicos[:])
exibir_nomes(magicos)