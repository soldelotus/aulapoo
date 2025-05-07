class Pessoa():

    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.statusFalando = False
        self.statusDormindo = False
        self.statusComendo = False

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome}"
              f" eu tenho {self.idade} anos"
              f" e peso {self.peso} quilos")

    def comer(self):
        self.statusComendo == True
        print(f"{self.nome} está comendo")

        if self.statusDormindo == True:
            self.statusComendo == False
            print("Você está dormindo e não pode comer")

        if self.statusDormindo == True:
            self.statusComendo == False
            print("Você está dormindo e não pode comer")


    def dormir(self):
        print(f"{self.nome} está dormindo")
        self.statusDormindo = True

        if self.statusComendo == True:
            self.statusDormindo == False
            print("Você já está comendo e não pode dormir")

        if self.statusFalando == True:
            self.statusDormindo == False
            print("Você está falando e não pode dormir")



    def falar(self):
        print(f"{self.nome} está falando")
        self.statusFalando = True

        if self.statusDormindo == True:
            self.statusFalando == False
            print("Você está dormindo e não pode falar")

        if self.statusComendo == True:
            self.statusFalando == False
            print("Você está comendo e não pode falar")



