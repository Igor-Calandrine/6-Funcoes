lista_usuários = []

def perfil_usuário(nome, sobrenome, **infos):
    perfil_construindo = {}

    perfil_construindo["nome"] = nome
    perfil_construindo["sobrenome"] = sobrenome

    for chave, valor in infos.items():
        perfil_construindo[chave] = valor

    lista_usuários.append(perfil_construindo)