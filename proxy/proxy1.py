class Ator:

    def __init__(self):
        self.ocupado = True
    
    def indisponivel(self):
        self.ocupado = True
        print(f'{type(self).__name__} está ocupado em uma atuação.')
    
    def disponivel(self):
        self.ocupado = False
        print(f'{type(self).__name__} está disponível para atuação.')
    
    def ver_disponibilidade(self):
        return self.ocupado


class Agente:

    def trabalhar(self):
        ator = Ator()
        ator_ocupado = ator.ver_disponibilidade()
        if ator_ocupado:
            ator.indisponivel()
        else:
            ator.disponivel()


if __name__ == '__main__':
    agente = Agente()
    agente.trabalhar()