"""Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso em caso contrário"""

palavras = ["tomate", "cebola", "alface", "carne"]

def procurar_palavra(palavra, lista=palavras):
    encontrada = False
    
    if palavra in lista:
        print("Palavra encontrada")
        encontrada = True
        print(encontrada)
    else:
        print("Palavra não encontrada")
        encontrada = False
        print(encontrada)

def inserir_lista(nome):
    palavras.append(nome)
    print(palavras)

procurar_palavra("tomate")
procurar_palavra("alho")
print(palavras)
inserir_lista("AZEITONA")
print(palavras)