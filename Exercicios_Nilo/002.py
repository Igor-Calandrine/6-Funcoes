"""Escreva uma função que receba dois números e retorne True se o  
primeiro número for múltiplo do segundo.
Valores esperados:
múltiplo(8,4) == True
múltiplo(7,3) == False
múltiplo(5,5) == True"""

def multiplo(x,y):
    boll_var = False
    
    if x % y == 0:
        boll_var = True
    else:
        boll_var = False
    
    print(boll_var)

multiplo(8,4)
multiplo(7,3)
multiplo(5,5)