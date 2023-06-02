class Main:
    pass


print ("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("Junior", "442255-6688")

conta=Conta(c1.nome,6565,0)

conta.deposita(100)
conta.saque(50)
conta.extrato()



#print(conta.titular, " Numero:", conta.numero, "Seu Saldo: ", conta.saldo)

#print(c1)
#print(c1.nome, "e", c1.telefone)

