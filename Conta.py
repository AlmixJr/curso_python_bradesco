class Conta:
    def __init__(self, numero, titular, saldo):
        self.saldo=0
        self.numero=numero
        self.titular=titular

        @property
        def get_saldo(self):
            return self._saldo
        
        @saldo.setter
        def sey_saldo(sel, saldo):
            if (saldo<0):
                print("0 saldo não pode ser negativo")
            else:
                self._saldo = saldo

    def saque(self, valor):
        if (self.saldo>=valor):
            self.saldo-=valor
            print("Saque foi realizado com sucesso")
        else:
            print("Saldo insuficiente")


    def deposita(self, valor):
        self.saldo+=valor

    def extrato(self):
        print("Cliente: ", self._titular, "Saldo Atual: ", self._saldo)               