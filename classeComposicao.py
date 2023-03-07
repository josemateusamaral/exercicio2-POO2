from classeSimples import Pessoa

class ChatBOT():
    def __init__(self,nome,idade,altura,peso):
        self.simulacaoDeUmaPessoa = Pessoa(nome,idade,altura,peso)

    def seApresentar(self):
        self.simulacaoDeUmaPessoa.seApresentar()

    def fazerAniversario(self):
        self.simulacaoDeUmaPessoa.fazerAniversario()
