"""Álbum: Escreva uma função chamada make_album() que construa um dicionário descrevendo um álbum musical. A função deve aceitar o nome de um artista e o título de um álbum e deve devolver um dicionário contendo essas duas informações. Use a função para criar três dicionários que representem álbuns diferentes. Apresente cada valor devolvido para mostrar que os dicionários estão armazenando as informações do álbum corretamente. Acrescente um parâmetro opcional em make_album() que permita armazenar o número de faixas em um álbum. Se a linha que fizer a chamada incluir um valor para o número de faixas, acrescente esse valor ao dicionário do álbum. Faça pelo
menos uma nova chamada da função incluindo o número de faixas em um álbum."""

artistas_album = []

def album_feito(artista, album, faixas=""):
    artistas = {}

    artistas["artista"] = artista
    artistas["album"] = album
    
    if faixas:
        artistas["faixas"] = faixas
    
    artistas_album.append(artistas)

album_feito("Red Hot", "Red")
album_feito("Pitty", "Quebrado", 15)
album_feito("Foo", "Cele", 13)
album_feito("Cell", "Dragon")



for artista in artistas_album:
    if "faixas" in artista:
        print(f"Artista: {artista["artista"]} - Album: {artista["album"]} - {artista["faixas"]} faixas")
    else:
        print(f"Artista: {artista["artista"]} - Album: {artista["album"]}")


