"""Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7"""

def maior_numero(x,y):
    if x > y:
        print(f'{x} é maior que {y}')
    elif y > x:
        print(f"{y} é maior que {x}")
    elif x == y:
        print(f"Não há um número maior - {x} e {y} são iguais")

maior_numero(5,6)
maior_numero(2,1)
maior_numero(7,7)