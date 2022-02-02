

class Singleton(object):

    def __new__(cls):
        # se nao estiver criado, cria o objeto
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print('criando o objeto {}'.format(cls.instance))
        return cls.instance

s1 = Singleton()
print('instancia {}'.format(id(s1)))
s2 = Singleton()
print('instancia {}'.format(id(s2)))