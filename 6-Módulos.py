"""
Armazenando sua funções em módulos
    Um vantagem das funções é a maneira como elas separam blocos de código de seu programa principal. Ao usar nomes descritivos para suas funções, será bem mais fácil entender o seu programa principal. Você pode dar um passo além, armazenando suas funções em um arquivo separado chamado módulo e então importar esse módulo em seu programa princiapal.
    Uma instrução #import diz a Python para deixar o código de um módulo disponível no arquivo de programa em execução.
    Quando armazenamos funções em arquivos separados, podemos compartilhar esses arquivos com outros programadores sem a necessidade de compartilhar o programa todo. Saber como importar funções também possibilita usar bibliotecas de funções que outros programadores escreveram.
    
Importando um módulo completo
    Para começar a importar funções, inicialmente precisammos criar um módulo. Um #módulo é um arquivo terminado em #.py que contém o código que queremos importar para o nosso programa. Como exemplo vamos criar um módulo de uma função do capítulo anterior, assim removeremos tudo que está no arquivo, exeto a função desejada e a colocaremos no arquivo pizza.py.
    Agora iremos importar para cá, quando Python lê esse arquivo, a linha import pizza lhe diz para abrir o arquivo pizza.py e copiar todas as funções dele para esse programa e agora qualquer função de pizza.py estará disponível aqui.
    Para chamar a função que está em um módulo importado, forneça o nome do módulo e em seguida o nome da função separados por um ponto.

        nome_do_modulo.nome_da_função()"""

print("Exemplo 1")
import pizza_0

pizza_0.pizza_pedida("G", "pepperoni", "queijo", "frango")
pizza_0.pizza_pedida("M", "batata", "queijo", "salame")

"""Importando funções específicas
    Podemos importar uma função específica de um módulo como demonstrado no exemplo abaixo.
    
        from nome_do_modulo import nome_da_função
    
    Assim como podemos também quantas funções quisermos de um módulo separando o nome de cada função com uma vírgula.
    
        from nome_do_modulo import função_1, função_2, função_3
        
    Observe no exemplo abaixo que quando usamos #from e depois #import, especificamos qual a função será importada, assim não precisamos usar o ponto que separa o módulo da função an sintaxe da chamada, podendo realizar através apenas da função."""

print("\nExemplo 2")
from pizza_1 import pizza_acrescimos, confirmação

pizza_acrescimos("queijo", "pepperoni", "frango")
confirmação("queijo", "pepperoni", "frango")

"""
Usando a palavra reservada #as para atribuir um alias a uma função
    Se o nome de um função que você importar poder entrar em conflito com um nome já existente em seu programa, ou se o nome da função for longo, podemos usar um #as único, que é um nome alternativo, semelhante a um apelido para a função. Observe o exemplo abaixo que foi dado um apelido para a função e em seguida a chamada foi realizada através dele mesmo.
    
        from nome_do_modulo import nome_da_função as apelido"""

print("\nExemplo 3")
from pizza_1 import pizza_pedida as pedido

pedido("M", "batata", "queijo", "salame")

"""
Usando a palavra reservada #as para atribuir a um módulo
    Também podemos fornecer um #as para um nome de módulo, isso permite chamar mais rapidamente as funções do módulo. Observe o exemplo abaixo, e suponha que tivéssemos a chamada através de #p, seria muito mais compacto. Utilizar essa sintaxe também  permite dar enfoque aos nomes descritivos de suas funções, nomes esses que devem claramente informar o que cada função faz, algo mais importante para a legibilidade de seu código que usar o nome completo do módulo.
    
        import nome_do_modulo as apelido"""

print("\nExemplo 4")

import pizza_0 as p
p.pizza_pedida("G", "pepperoni", "queijo", "frango")

"""
Importando todas as funções de um módulo
    O asterisco na instrução import diz a Python para copiar todas as funções do módulo para esse aquivo de programa. Como todas as funções são importadas, podemos chamar qualquer função pelo nome, sem usar a notação de ponto. No entento, é melhor não usar essa abordagem quando trabalhamos com módulos maiores, que não foram escritos por você, porque casa o módulo tiver um nome de função que seja igual a um nome existente em seu projeto, você terá resultados inesperados.
    Python poderá ver várias funções ou variáveis com o mesmo nome, e em de importar todas as funções separadamente, ele as sobrescreverá.
    A melhor abordadgem é importar a função que você quiser ou importar o módulo todo e usar a notação do ponto. Isso resulta em um código claro, mais fácil de ler e de entender.

        from nome_do_módulo import *
    
Estilizando funções
    Como já vimos, é importante se atentar a alguns detalhes sobre os nomes descritivos das funções, esse nomes também devem ser escritos com letra minúsculas e underscores. Nomes descritivos ajudam você e outras pessoas a entederem o que seu código está tentando fazer. Os nomes de módulos devem usar essas conveções também.
    Toda função deve ter um comentário que explique o que ela faz, esse comentário deve estar imediatamente após a definição da função e deve utilizar o formato de docstring. Os programadores poderão usá-las em seus programas e funcionará conforme descrito.
    Um módulo não deve começar seu nome com um número, isso irá gerar um erro de sintaxe.
    Se você especificar um valor default ou um argumento nomeado para um parâmetro, não deve haver espaços em nenhum dos lados do sinal de igualdade.
    Se seu programa ou módulo tiver mais de uma função, você poderá separá-las usando duas linhas em branco para facilitar ver em que ligar uma função termina e a próxima começa.
    Todas as instruções #import devem estar no início de um arquivo. A única exceção ocorre quando você usa comentários no início de eu arquivo para descrever o programa como um todo."""


    


