import datetime
from datetime import date
import locale

data_atual = date.today()
agora = data_atual.strftime("%d/%m/%Y")


class Pessoa:
    def __init__(self, nome, idade, dtcadastro, dtvencimento, ativo):
        self.nome = nome
        self.idade = idade
        self.dtcadastro = dtcadastro
        self.dtvencimento = dtvencimento
        self.ativo = ativo

    def desativar(self):
        self.ativo = False
        print(f'A pessoa: {self.nome} desativado com sucesso...')
        print(f'Vencimento: {self.dtcadastro}')

        if self.dtcadastro <= self.dtvencimento:
            print('A vencer')
        else:
            print('Vencida')

    

if __name__=="__main__":
    p = Pessoa('Carlos', 48, "31/12/2024", "31/12/2025", True)
    print(p.nome,p.idade, p.dtcadastro, p.dtvencimento, p.ativo)
    p.desativar()