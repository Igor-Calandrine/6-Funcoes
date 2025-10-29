"""
Passando um número arbitrário de argumentos
    Às vezes você não saberá com antedecedência quantos argumentos uma função deve aceitar. Felizmente, Python permite que uma função receba um número arbitrário de argumentos da instrução de chamada.
    No exemplo abaixo o *(asteriscos) no nome do parâmetro diz para criar uma tupla vazia chamada acréscimos e reunir os valores recebidos nessa tupla.
    Como um TUPLA foi criado, podemos realizar uma chamada para que cada acréscimo a essa pizza seja impressa com um laço for. Essa sintaxe irá funcionar não importante quantos argumentos a função receba."""

print("Exemplo 1")

def pizza(*acréscimos):
    print(f"Tulpa - {acréscimos}")

def confirmação(*acréscimos):
    print(f"A pizza será feita com os seguintes acréscimos:")
    for acréscimo in acréscimos:
        print(f"\t*{acréscimo}")

pizza("queijo", "pepperoni", "frango")
confirmação("queijo", "pepperoni", "frango")

"""
Misturando argumentos posicionais e arbitrários
    Se quiser que uma função aceite vários tipos de argumentos, o parâmetro que aceita um número arbitrário de argumentos deve ser colocado por último da definição da função. Python faz a correspondência de argumentos posicionais e nomeados antes, e depois agrupa qualquer argumento remanescente no último parâmetro."""

print("\nExemplo 2")

def pizza_pedida(tamanho, *acréscimos):
    print(f"Tamanho: {tamanho}")
    print("Acréscimos:")
    for acréscimo in acréscimos:
        print(f"\t*{acréscimo}")

pizza_pedida("grande", "queijo", "pepperoni", "frango")

"""
Usando argumentso nomeados arbitrários
    Às vezes você vai querer aceitar um número arbitrário de argumentos, mas não saberá com antecedência qual tipo de informação será passado para a função. Nesse caso podemos escrever funções que aceitem tantos pares chave-valor quantos forem fornecidos pela instrução que faz a chamada. 
    Os ** (asteriscos duplos) antes do parâmetro fazem Python criar um par chave-valor que irão se comportar como itens de um DICIONÁRIO, assim iremos criar esse par em um e acessá-los como faríamos em qualquer dicionário.
    No próximo exemplo temos uma função que cria um dicionário para construir o perfil de um usuário que sempre aceita um primeiro nome e sobrenome, mas aceita também um número arbitrário de argumentos nomeados."""

print("\nExemplo 3")

def perfil_usuário(nome, sobrenome, **infos):
    perfil_usuário = {}
    perfil_usuário["nome"] = nome
    perfil_usuário["sobrenome"] = sobrenome
    
    for chave, valor in infos.items():
        perfil_usuário[chave] = valor

    print(f"Dicionário - {perfil_usuário}")
    print("Usuário:")
    for chave, valor in perfil_usuário.items():
        print(f"\t{chave}: {valor}")

perfil_usuário("Igor", "Araújo", Altura=1.65, Ensino="Superior")
