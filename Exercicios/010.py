"""Grandes mágicos: Comece com uma cópia de seu programa anterior. Escreva uma função chamada make_great() que modifique a lista de mágicos acrescentando a expressão o Grande ao nome de cada mágico. Chame show_magicians() para ver se a lista foi realmente modificada."""

magicos = ["harry houdini","david copperfield", "criss angel", "dynamo", "penn & teller"]

def exibir_nomes(nomes):
    print("Lista de famosos mágicos:")
    for nome in nomes:
        print(f"\t* {nome.title()}")

def grande_magico(nomes):
    i=0
    while i < len(nomes):
        nome_atual = nomes.pop(0)
        frase = f"O grande {nome_atual}"
        nomes.append(frase)
        i = i + 1
    
exibir_nomes(magicos)
grande_magico(magicos)
exibir_nomes(magicos)
