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

# ------------------------------------------------------------

class Animal():
    def __init__(self, nome, cor):
        self.nome=nome
        self.cor=cor

    def comer(self):
        print(f"O {self.nome} foi comer...")

#---------
class Gato(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def miar(self):
        print(f"O {self.nome} foi miando...")

class Cachorro(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def latir(self):
        print(f"{self.nome} está latindo")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def comer(self):
        print(f"{self.nome} está comendo cenoura")

    def botarOvo(self):
        print(f"{self.nome} está colocando ovos de chocolate belga")

class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{super.nome} está mugindo")

#-------------- Exercício 01 -------------------
class Ingresso():
    def __init__(self, valor):
        self.valor=valor

    def imprimeValor(self):
        print(f"O valor do ingresso é {self.valor}")

class Vip(Ingresso):
    def __init__(self, valor):
        super().__init__(valor* 1.5)

# --------------Exercício 02----------------

class Forma():
    def __init__(self):
        self.area = 0
        self.perimetro = 0

class Retangulo(Forma):
    def __init__(self):
        super().__init__()

    def calcularArea(self):

    def calcularPerimetro(self):

class Triangulo(Forma):
    def __init__(self):
        super().__init__()
        self.altura = 0

    def calcularArea(self):
        area = (self.base * self.altura) / 2
        print(f"A área do triângulo é {area}")

    def calcularPerimetro(self):
        
