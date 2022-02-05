from abc import ABCMeta, abstractmethod


class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):

    def falar(self):
        print("Au Au")

class Gato(Animal):

    def falar(self):
        print("Miau")

class Factory:

    def criar_animal_falante(self, tipo):
        return eval(tipo)().falar()
        #tipo ['Gato' ou 'Cachorro']
        #eval(tipo) = Gato() || Cachorro()

if __name__ == "__main__":
    fact = Factory()
    animal = input("Cachorro ou gato")
    fact.criar_animal_falante(animal)