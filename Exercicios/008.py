"""Álbuns dos usuários: Comece com o seu programa anterior. Escreva um laço while que permita aos usuários fornecer o nome de um artista e o título de um álbum. Depois que tiver essas informações, chame make_album() com as entradas do usuário e apresente o dicionário criado. Lembre-se de incluir um valor de saída no laço while."""

artistas_album = []

def album_feito():

    while True:
        artistas = {}
        
        artista = input("Digite o nome do artista ou (0)zero para sair.\n\t")
        if artista == "0":
            break
        album = input("Digite o nome do album ou (0)zero para sair.\n\t")
        if album == "0":
            break
        faixas = input("Digite a quantiade de faixas do album se souber ou (0)zero para sair.\n\t")
        if faixas == "0":
            break

        artistas["artista"] = artista
        artistas["album"] = album
        if faixas:
            artistas["faixas"] = faixas
    
        artistas_album.append(artistas)

album_feito()

for musico in artistas_album:
    if "faixas" not in musico:
        print(f"Artista: {musico["artista"]} - Album: {musico["album"]}")
    else:
        print(f"Artista: {musico["artista"]} - Album: {musico["album"]} - {musico["faixas"]} faixas")