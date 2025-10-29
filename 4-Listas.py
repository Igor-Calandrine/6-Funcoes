"""
Passando uma lista para uma função
    Com frequência, você acahrá útil passa uma lista para uma função, seja uma lista de nome, de números ou de objetos mais complexos, como dicionários. Se passarmos uma lista como argumentos a uma função, ela terá acesso direto ao conteúdo dessa lista. Observe o exemplo abaixo em que #u é uma lista e foi passado como argumento para a função."""

print("Exemplo 1")
usernames = ["hannah", "ty", "margot"] #u

def greet_users(names):
    for name in names:
        msg = f"Hello {name.title()}!"
        print(msg)

greet_users(usernames)

"""
Modificando uma lista em uma função
    Quando passamos uma lista a uma função, ela pode ser modificada, qualquer alteração na lista no corpo da função é PERMANENTE, permitindo trabalhar de modo eficiente, mesmo quando lidamos com grandes quantidades de dados.
    Escreveremos um código em que cada função executa uma tarefa específica, deixando-o mais eficiente. A primeira função tratará a impressão dos designs e a segunda gerará um resumo da impressão feita.
    Em #a definomos a função com dois parâmetros, uma lista a serem impressos e outra a serem concluídas. Dada as duas listas, a função simula os esvaziamento de uma lista e em seguida preenchendo outra.
    Em #b definimos a função com um parãmetro para apresentar a lista de modelos finalizados com o nome de cada modelo.
    O código produz a mesma saída que poderia produzir com apenas uma função, mas observe no corpo de #c como o código fica muito mais fácil de entender."""
     

print("\nExemplo 2")

unprited_models = ["batman", "capitão américa", "thor"]
printed_models = []

def print_model(unprited_models, printed_models): #a
    while unprited_models:
        current_model = unprited_models.pop(0)
        print(f"Printing model: {current_model.title()}")
        printed_models.append(current_model)

def show_printed_model(printed_models): #b
    print("\nOs seguintes modelos foram finalizados")
    for printed_model in printed_models:
        print(f"\t{printed_model.title()}")

print_model(unprited_models, printed_models) #c
show_printed_model(printed_models) #c

"""
    Esse programa é mais fácil de ser estendido e mantido que a versão sem funções. Se precisarmos imprimir mais designs depois, poderemos simplesmente chamar a função novamente. Se percebermos que o código de impressão precisa ser modificado, podemos alterar o código uma vez, e nossas alterações estarão presentes em todos os lugares em que a função for chamada. Essa técnia é mais eficiente que ter de atualizar um código separdamente em vários pontos do programa.
    Esse exemplo também mostra a ideia de que toda dunção deve ter uma tarefa específica, isso é mais vatajoso que usar uma única função para executar as duas tarefas. Se você estiver escrevendo uma função e perceber que ela está fazendo muitas tarefas diferentes, experimente dividir o código em duas funções. 

Evitando que uma função modifique uma lista
    Ás vezes você vai querer evitar que uma função modifique uma lista. Por exemplo, suponha que você queira manter a lista de itens não impressos para ter ser registro. Nesse caso, podemos tratar esse problema passando uma cópia da lista para a função, e não a original. Qualquer alteração que a função fizer, afaterá apenas a cópia.
    Em #y utilizamos como argumento unprited_models[:], assim criamos uma cópia da lista (ver propriedade em 2-Listas), e no final foi pedido a lista original para garantir que não foi modificada.
    Apesar de poder preservar o conteúdo de uma lista passando uma cópia dela para suas funções, você deve passar a lista original para as funções, a menos que tenha um motivo para passar uma cópia. É mais eficiente trabalhar com uma lista existente a fim de evitar o uso de tempo e memória necessários para criar uma cópia separada, em especial quando trabalhamos com listas grandes. """

print("\nExemplo 3")
unprited_models = ["batman", "capitão américa", "thor"]
printed_models = []

def print_model(unprited_models, printed_models):
    while unprited_models:
        current_model = unprited_models.pop(0)
        print(f"Printing model: {current_model.title()}")
        printed_models.append(current_model)

def show_printed_model(printed_models):
    print("\nOs seguintes modelos foram finalizados")
    for printed_model in printed_models:
        print(f"\t{printed_model.title()}")

print_model(unprited_models[:], printed_models) #y 
show_printed_model(printed_models)
print(unprited_models)

