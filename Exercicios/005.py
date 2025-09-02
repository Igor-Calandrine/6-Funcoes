"""Cidades:  Escreva  uma  função  chamada  describe_city() que aceite o nome de uma cidade e seu país. A função deve exibir uma frase simples, como Reykjavik está localizada na Islândia. Forneça um valor default ao parâmetro que representa o país. Chame sua função para três cidades diferentes em que pelo menos uma delas não esteja no país default."""

def cidade_descrita(cidade, paiz="islândia"):
    print(f"A cidade {cidade.title()} esta localizada no paíz {paiz.title()}")

cidade_descrita("Reykjavík")
cidade_descrita("Akureyri")
cidade_descrita("Keflavík")
cidade_descrita(cidade="Belém", paiz="Brasil")