"""Perfil do usuário: Crie um perfil seu chamando perfil_usuário(), usando seu primeiro nome e o sobrenome, além de três outros pares chave-valor que o descrevam."""

lista_usuários = []

def perfil_usuário(nome, sobrenome, **infos):
    perfil_construindo = {}

    perfil_construindo["nome"] = nome
    perfil_construindo["sobrenome"] = sobrenome

    for chave, valor in infos.items():
        perfil_construindo[chave] = valor

    lista_usuários.append(perfil_construindo)

def todos_usuários(lista):
    for x, usuário in enumerate(lista, 1):
        print(f"{x}º Usuário:")
        
        for chave, valor in usuário.items():
            if chave == "nome" or chave == "sobrenome":
               print(f"\t{chave}: {valor.title()}")
            else: 
                print(f"\t{chave}: {valor}")

perfil_usuário("igor", "araújo", idade=20, altura=1.65, cor="branco")
perfil_usuário("bianca", "rosshard", idade=19, altura=1.60, cor="branco")
perfil_usuário("yuri", "guimarães", idade=18, altura=1.70, cor="branco")
todos_usuários(lista_usuários)
