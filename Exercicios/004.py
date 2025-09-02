"""Modifique a função make_shirt()  de  modo  que  as camisetas sejam grandes por default, com uma mensagem Eu amo  Python. Crie uma camiseta grande e outra média com a mensagem default, e uma camiseta de qualquer tamanho com uma mensagem diferente."""

def camisa_feita(frase, tamanho="G"):
    print(f"A camisa virá do tamanho {tamanho} e com frase '{frase}'")

camisa_feita("Eu amo Phyton")

def camisa_feita(tamanho, frase="Eu amo Phyton"):
    print(f"A camisa virá do tamanho {tamanho} e com frase '{frase}'")

camisa_feita("M")

def camisa_feita(tamanho, frase="Eu sou muito gordo mesmo!"):
    print(f"A camisa virá do tamanho {tamanho} e com frase '{frase}'")

camisa_feita("GG")
