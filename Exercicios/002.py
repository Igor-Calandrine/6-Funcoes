"""Livro favorito: Escreva uma função chamada favorite_book() que aceite um parâmetro title. A função deve exibir uma mensagem como Um  dos  meus livros favoritos é Alice no país das maravilhas. Chame a função e não se esqueça de incluir o título do livro como argumento na chamada da função."""

def favorite_book(nome, titulo):
    print(f"Sr.(a) {nome.title()}, seu livro preferido é o '{titulo}'")

favorite_book("igor", "Harry Potter")
