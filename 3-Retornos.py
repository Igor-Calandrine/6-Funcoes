"""
Retornos
    Uma função nem sempre precisa exibir sua saída diretamente. Em vez disso, ela pode processar alguns dados e então devolver um valor ou um conjunto de valores. O valor devolvido pela função é chamado de valor de retorno. A instrução return toma um valor que está em uma função e o envia de volta à linha que a chamou. Valores de retorno permitem passar boa parte do trabalho pesado de um programa para funções, o que pode simplificar o corpo de seu programa.
    Quando  chamamos uma função que devolve um valor, precisamos fornecer uma variável em que o valor de retorno possa ser armazenado. Nesse caso, o valor devolvido é armazenado na variável musician. A saída mostra um nome formatado de modo elegante, composto das partes do nome de uma pessoa"""

print("Exemplo 1")

def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
 
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

"""
Devolvendo um dicionário
    Uma função pode devolver qualquer tipo de valor necessário, incluindo estruturas de dados mais complexas  como listas e dicionários. Por exemplo, a função a seguir aceita partes de um nome e devolve um dicionário que representa uma pessoa"""

print("\nExemplo 2")
def definicao_pessoa(nome, genero, idade=""):
    pessoa = {"nome":nome.title(), "genero":genero}
    if idade:
        pessoa["idade"] = idade 
    return pessoa

musico_1 = definicao_pessoa("igor", "masculino")
musico_2 = definicao_pessoa("bianca", "feminino", 16)

print(musico_1)
print(musico_2)




