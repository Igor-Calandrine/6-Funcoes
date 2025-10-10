"""
Variáveis locais e globais
    Uma variável local a uma função existe apenas dentro dela, sendo normalmente inicializada a cada chamada. Assim, não podemos acessar o valor de uma variável local fora da função que a criou e, por  isso, passamos parâmetros e retornamos valores nas funções, de forma a possibilitar a troca de dados no programa.
    Uma variável global é definida fora de uma função, pode ser vist por todas as funções do módulo e por todos os módulos que importam o módulo que a definiu. Observe que utilizamos a variável EMPRESA definida fora da função. Nesse caso, #empresa é uma variável global, podendo ser acessada em qualquer função."""

print("Exemplo 1")
empresa = "Unidos venceremos "

def print_cabeçalho():
    print(empresa, end="-"*8)
    print()

print_cabeçalho()

"""
    Variáveis globais devem ser utilizadas o mínimo possível em seus programas, pois dificultam a leitura e violam o encapsulamento da função. A dificuldade da leitura é em procurar pela definição e conteúdos fora da função em si, que popdem mudar entre diferentes chamadas. Além disso, uma variável global pode ser alterada por qualquer função, tornando a tarefa de saber qua, altera seu valor realmente mais trabalhosa.
    Embora devamos utilizar variáveis globais vcom cuidado, isso significa que elas não tenham uso ou que possam simplesmente ser classificadas como máprática. Um bom uso de variáveis globais é guardar valores constantes e que devem ser acessíveis a todas as funções do programada, como o nome da empresa
    
Variáveis globais e locais
    Devido à capacidade da linguagem Python de declarar variáveis 
    á medida que precisamos, devemos tomar cuidado quando altermos uma variável global dentro de uma função.
    No exemplo abaixo temos uma variável global e uma local de mesmo nome, mas para o computador essas variáveis são completamente diferentes, embora tenho o mesmo nome. a variável #nome = yuri, deixa de existir no final da funçãoe explica porque não alteramos a variável global #nome = igor"""

print("\nExemplo 2")

nome = "igor"

def alterar_nome():
    nome = "yuri"

print(nome.title())
alterar_nome()
print(nome.title())

"""
    Se quisermos modificar uma variávelglobal dentro de uma função, devemos informar que estamos usando uma variável global antes de inicializá-la, na primeira linha de nossa função através da instrução #global."""

print("\nExemplo 3")
def alterar_nome_global():
    global nome
    nome = "yuri"

print(nome.title())
alterar_nome_global()
print(nome.title())

"""
    A utilização da instrução #global pode sinalizar um problema de construção no programa. Lembre-se de utilizar variáveis globais apenas para configuração, e de preferância para constantes. A instrução #global facilita a escolha de nomes de veriáveis preexistentes e não criando uma nova.
    Ao utilizar variáveis globais, tente facilitar a leitura de seu programa, como usar apenas letras maiúsculas sem seus nomes ou um prefixo, por exemplo #EMPRESA OU #G_EMPRESA"""

print("\nExemplo 4")
EMPRESA = "Jamais cederemos"
G_NOME = "bianca"

print(EMPRESA)
print(G_NOME.title())
