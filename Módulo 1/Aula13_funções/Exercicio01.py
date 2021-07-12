def operacao(largura, comprimento):
    
    area = largura * comprimento
    print(f"A área do seu terreno é: {area} m²")


largura = int(input("Informe a largura do terreno: "))
comprimento = int(input("Informe o comprimento do terreno: "))
operacao(largura,comprimento)
