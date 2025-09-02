"""Introdução - Funções
    Neste capítulo aprenderemos a escrever funções, que são blocos de código nomeados, concebidos para realizar uma tarefa específica. Quando queremos executar uma tarefa em particular, definida em uma função, chamamos o nome da  função responsável por ela. Se precisar executar essa tarefa várias vezes durante seu programa, não será necessário digitar todo o código para a mesma tarefa repetidamente: basta chamar a função dedicada ao tratamento dessa tarefa e a chamada dirá a Python para executar o código da função. Você perceberá que usar funções permite escrever, ler,  testar e corrigir seus programas de modo mais fácil.

Definindo uma função
    Esse exemplo mostra a estrutura mais simples possível para uma função. A linha em u utiliza a palavra reservada def para informar Python que estamos definindo uma função, em seguida informamos o nome da função a Python e, se for aplicável, quais são os tipos de informação necessários à função para que ela faça sua tarefa nos parênteses.
    A linha print("Hello!") w é a única linha com código propriamente dito no corpo dessa função, portanto apenas a realizará.
    Quando quiser usar essa função, você deve chamá-la em x. Escreva o nome dela, seguido de qualquer informação necessária entre  parênteses, como nenhuma informação é necessária nesse caso, chamar nossa função é simples."""

print("Exemplo 1")
def saudacao (): #u
    print("Hellow Word") #w

saudacao () #x

"""Argumento ou parâmetros
Um argumento é uma informação passada para uma função em sua chamada. Quando chamamos a função, colocamos entre parênteses o valor com que queremos que a função trabalhe. Nesse caso, o argumento 'igor' foi passado para a função e o valor foi armazenado no parâmetro username."""

print("\nExemplo 2")
def saudacao (usuario):
    print(f"Hellow Word, {usuario}")

saudacao ("Igor")
    
