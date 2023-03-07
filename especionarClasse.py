from classeSimples import Pessoa
from classeHeranca import Programador
from classeComposicao import ChatBOT

def especionar(classe):
    #pegar todos os metodos da classe
    metodos = [m for m in dir(classe) if callable(getattr(classe, m)) and not m.startswith("__")]
    print(f'\n\nMETODOS da classe {str(classe)}:\n{metodos}')

    #pegar todos os atributos da classe
    variaveis = vars(classe)
    print(f'\n\nVARIAVEIS da classe {classe}:\n{variaveis}')

print('------------------------')

pessoa = Pessoa('mateus',24,1.80,60)
pessoa.seApresentar()
pessoa.fazerAniversario()
especionar(pessoa)

print('------------------------')

programador = Programador('mateus',24,1.80,60)
programador.seApresentar()
programador.fazerAniversario()
especionar(programador)

print('------------------------')

chatbot = ChatBOT('mateus',24,1.80,60)
chatbot.seApresentar()
chatbot.fazerAniversario()
especionar(chatbot)


