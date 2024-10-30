import time

hora = time.strftime("%H:%M")

MENSAGEM  = ""

BOM_DIA = 'Bom dia!'
BOA_TARDE = 'Boa Tarde!'
BOA_NOITE = 'Boa Noite!'
BOA_MADRUGADA = 'Boa Madrugada!'



class Saudacao:
    saudacao = {
        0: BOM_DIA, 1: BOA_TARDE, 2: BOA_NOITE, 3: BOA_MADRUGADA
    }

    def __init__(self):
        self.saudar = self.saudacao[hora]


    def saudar(self):
        self.saudar = self.saudacao[self.saudar]


    if hora >= "1" and hora < "12":
        msg = 'Bom dia!'
    elif hora>= "12" and hora < "18":
        msg = 'Boa tarde!'
    elif (hora>"18" and hora<="24") or hora=="0":
        msg = 'Boa noite!'


if __name__=="__main__":
    hh = Saudacao()
    print(hh)
    print(hh.saudar)
