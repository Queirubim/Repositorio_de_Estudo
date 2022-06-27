class teste:
    def __init__(self):
        print("Endereço do self = ", id(self))

obg = teste()
print("Endereço do objeto da classe teste = ", id(obg))