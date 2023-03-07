class Pessoa:
    def __init__(self,nome,idade,altura,peso):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso

    def seApresentar(self):
        print(f'olá, meu nome é {self.nome} e eu tenho {self.idade} anos')

    def fazerAniversario(self):
        self.idade += 1



