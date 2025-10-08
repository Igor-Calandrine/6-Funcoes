def pizza_pedida(tamanho, *acréscimos):
    print(f"Tamanho: {tamanho}")
    print("Acréscimos:")
    for acréscimo in acréscimos:
        print(f"\t*{acréscimo}")
    print()    