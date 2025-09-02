"""Nomes de cidade: Escreva uma função chamada city_country() que aceite o nome de uma cidade e seu país. A  função deve devolver uma string formatada assim: "Santiago, Chile". Chame sua função com pelo menos três pares cidade-país e apresente o valor devolvido."""

def city_country():
    locais = []

    while True:
        local = {}
        
        cidade = input("Digite o nome da cidade, ou 'q' para sair: ")
        if cidade == "q":
            break
        estado = input("Digite o nome do estado, ou 'q' para sair: ")
        if estado == "q":
            break

        local["cidade"] = cidade.title()
        local["estado"] = estado.upper()
        locais.append(local)
        print(f"\nCidade: {cidade.title()} - {estado.upper()}")
    
    for lugar in locais:
        print(f"Cidade: {lugar["cidade"]} - {lugar["estado"]}")
    
city_country()


    
