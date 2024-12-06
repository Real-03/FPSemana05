class ContaBancaria:
    Titular = ""
    Saldo = 0
    credit = 0
    def __init__(self, titular, saldo, limite):
        self.titular = titular
        self.saldo = saldo
        self.credit = limite

    def depositar(self,saldo):
        
        if(saldo>=0):
            self.saldo+=saldo
            print(1)
        else:
            print(0)
    
    def levantar(self,saldo):

        if((self.saldo+self.credit)-saldo>=0):
            self.saldo -= saldo
            print(1)
        else:
            print(0)
    
    def exibir_saldo(self):
        print(f"{self.saldo:.2f}")
        
    
    def exibir_info(self):
        print(f"{self.titular} {self.saldo:.2f} {self.credit:.2f}") 


conta = ContaBancaria("João", 1000.00, 500.00)
conta.depositar(-500.00)
conta.depositar(500.00)
conta.levantar(1200.00)
conta.levantar(1200.00)
conta.exibir_info()
