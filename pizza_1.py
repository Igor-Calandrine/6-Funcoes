def pizza_acrescimos(*acréscimos):
    print(f"Tulpa - {acréscimos}")

def confirmação(*acréscimos):
    print(f"A pizza será feita com os seguintes acréscimos:")
    for acréscimo in acréscimos:
        print(f"\t*{acréscimo}")

def pizza_pedida(tamanho, *acréscimos):
    print(f"Tamanho: {tamanho}")
    print("Acréscimos:")
    for acréscimo in acréscimos:
        print(f"\t*{acréscimo}")