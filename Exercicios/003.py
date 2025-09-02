"""Camiseta: Escreva uma função chamada make_shirt() que aceite um tamanho e o texto de uma mensagem que deverá ser estampada na camiseta. A função deve exibir uma frase que mostre o tamanho da camiseta e a mensagem estampada.
Chame a função uma vez usando argumentos posicionais para criar uma camiseta. Chame a função uma segunda vez usando argumentos nomeados."""

def camisa_feita(tamanho, apelido):
    print(f"A camisa virá do tamanho {tamanho} e com apelido {apelido}")

camisa_feita("P", "Xoba")
camisa_feita(apelido="Perni", tamanho="M")