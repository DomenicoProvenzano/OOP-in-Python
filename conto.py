class Conto:
    def __init__(self, nome, conto):
        self.nome = nome
        self.conto = conto

class ContoCorrente(Conto):
    def __init__(self, nome, conto, importo):
        super().__init__(nome, conto)
        self.__saldo = importo

    def preleva(self, importo):
        self.__saldo -= importo
    
    def deposita(self, importo):
        self.__saldo += importo
    
    def descrizione(self):
        print(self.nome, self.conto, self.__saldo)

    @property 
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, importo):
        self.preleva(self.__saldo)
        self.deposita(importo)

class GestoreContiCorrenti:
    @staticmethod
    def bonifico(sorgente, destinazione, importo):
        sorgente.preleva(importo)
        destinazione.deposita(importo)
        

c1 = ContoCorrente("Mario", 10, 3000)
c2 = ContoCorrente("Andrea", 20, 9000)

c1.descrizione()
c2.descrizione()

GestoreContiCorrenti.bonifico(c1, c2, 350)

c1.descrizione()
c2.descrizione()