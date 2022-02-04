

class Singleton(object):

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O método __init__ foi chamado')
        else:
            print('A instancia já foi criada: {}'.format(self.get_instance()))

    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton() # classe inicializada, objeto não criado
print('instancia criada agora: {}'.format(s1.get_instance())) # objeto criado agora
s2 = Singleton() 
