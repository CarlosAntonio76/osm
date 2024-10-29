import locale
import datetime
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
dia_semana = datetime.datetime.today().weekday()


DOMINGO = 'Domingo'
SEGUNDA = 'Segund-Feira'
TERCA = 'Terça-Feira'
QUARTA = 'Quarta-Feira'
QUINTA = 'Quinta-Feira'
SEXTA = 'Sexta-Feira'
SABADO = 'Sábado'


class MostrarNomeSemana:
    nome_semana = {0: SEGUNDA, 1: TERCA, 2: QUARTA, 3: QUINTA, 4: SEXTA,
                   5: SABADO, 6: DOMINGO
                   }

    
    def __init__(self):
        self.numero_semana = dia_semana


    def mostrar_nome_semana(self):
        self.numero_semana = self.nome_semana[self.numero_semana]


if __name__=='__main__':
    nsemana = MostrarNomeSemana()
    print(nsemana.nome_semana)
    print(nsemana.numero_semana)
    print(nsemana.nome_semana[nsemana.numero_semana])








    

    