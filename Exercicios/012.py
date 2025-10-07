"""Sanduíches: Escreva uma função que aceite uma lista de itens que uma pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe tantos itens quantos forem fornecidos pela chamada da função e deve apresentar um resumo do sanduíche pedido. Chame a função três vezes usando um número diferente de argumentos a cada vez."""

sanduíches = []

def pedidos_sanduíches(*itens):
    pedidos = []
    print("Lista de itens pedidos:")
    
    for item in itens:
        pedidos.append(item)
        print(f"\t*{item}")
    
    sanduíches.append(pedidos)

def lista_sanduíches(lista):
    for x, item in enumerate(lista, 1):
        print(f"\nSanduíche {x} -")
        print(f"\t{item}")

pedidos_sanduíches("batata", "tomate", "carne")
pedidos_sanduíches("batata", "tomate", "carne", "mostarda", "maionese")
pedidos_sanduíches("alface", "tomate", "carne", "ketchup", "maionese")
lista_sanduíches(sanduíches)
