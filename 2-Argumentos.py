"""
Argumentos posicionais
    Quando chamamos uma função, Python precisa fazer a correspondência entre cada argumento da chamada da função e um parâmetro da definição. A maneira mais simples de fazer isso é contar com a ordem dos argumentos fornecidos. Valores cuja correspondência seja feita dessa maneira são chamados de argumentos posicionais.
    Podemos usar tantos argumentos posicionais quantos forem necessários nas funções. Python trabalha com os argumentos fornecidos na chamada da função e faz a correspondência de cada um com o parâmetro associado na definição da função."""

print("Exemplo 1")

def descricao_pet (tipo_pet, nome_pet):
    print(f"Eu tenho um pet do tipo {tipo_pet}")
    print(f"O nome do meu pet do tipo {tipo_pet} é {nome_pet.title()}")

descricao_pet("cachorro", "pudge")
descricao_pet("gato", "Femb")

"""
A ordem é importante em argumentos posicionais
    Podemos obter resultados inesperados se confundirmos a ordem dos argumentos em uma chamada de função quando argumentos posicionais forem usados. Se obtiver resultados inesperados como esse, verifique se a ordem dos argumentos  em  sua  chamada  de  função  corresponde  à  ordem  dos parâmetros na definição da função."""

print("\nExemplo 1.2")

descricao_pet ("pudge", "cachorro")

"""
Argumentos nomeados
    Um argumento nomeado é um par nome-valor passado para uma função. Associamos diretamente o nome e o valor no próprio argumento para que não haja confusão quando ele for passado para a função. Argumentos nomeados fazem com que você não precise se preocupar com a ordem correta de seus argumentos na chamada da função e deixam claro o papel de cada valor na chamada.
    A função não mudou, entretanto a ordem dos argumentos foi invertida quando chamamos a função. Porém dizemos  explicitamente a Python a qual parâmetro cada argumento deve corresponder. Quando Python lê a chamada da função, ele sabe onde deve armazenar o argumento."""

print("\nExemplo 2")

descricao_pet (nome_pet = "pudge", tipo_pet = "cahorro")
descricao_pet (tipo_pet = "cahorro", nome_pet = "pudge")

"""
Valores default
    Ao escrever uma função, podemos definir um valor default para cada parâmetro. Se um valor default for definido para um parâmetro, você poderá excluir o argumento correspondente, que normalmente seria especificado na chamada  da função. Usar valores default pode simplificar suas chamadas de função e deixar mais claro o modo como suas funções normalmente são utilizadas.
    Como o uso do valor default faz com que não seja necessário especificar um tipo de animal como argumento, o único argumento restante na chamada da função é o nome do animal de estimação. Python continua interpretando  esse valor como um argumento  posicional, portanto, se a função for chamada somente com o nome de um animal de estimação, esse argumento corresponderá ao primeiro parâmetro listado na definição da função."""

print("\nExemplo 3")
def descricao_pet (nome_pet, tipo_pet = "cahorro"):
    print(f"Eu tenho um pet do tipo {tipo_pet}")
    print(f"O nome do meu pet do tipo {tipo_pet} é {nome_pet.title()}")

descricao_pet ("Pudge")

"""
Deixando um argumento opcional
    Às vezes, faz sentido criar um argumento opcional para que as pessoas que usarem a função possam optar por fornecer informações extras somente se quiserem. Valores default podem ser usados para deixar um argumento opcional. Nesse exemplo, o nome é criado a partir de três partes possíveis. Como o primeiro nome e o sobrenome sempre existem, esses parâmetros são listados antes na definição da função. O nome do meio é opcional, portanto é listado por último na definição, e seu valor default é uma string vazia"""

print("\nExemplo 4")
def nome_completo(primiro_nome, ultimo_nome, meio_nome=""):
    if meio_nome:
        nome_completo = f"{primiro_nome} {meio_nome} {ultimo_nome}"
    else:
        nome_completo = f"{primiro_nome} {ultimo_nome}"
    
    print(nome_completo.title())

nome_completo("igor", "araujo")
nome_completo("igor", "araujo", "guimarães")