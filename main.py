from conta import Conta
from cliente import Cliente

conta = Conta(123,"Carol", 55.5,1000.0)
conta2 = Conta(121,"Caroline", 65.5,1000.0)

conta.deposita(15.0)
conta.saca(10.0)

print(conta._Conta__saldo)
conta.extrato()

conta2.tranfere(10.0,conta)
conta.extrato()

conta.get_saldo()
conta.get_titular()
conta.limite=10000.0
print(conta.limite)

cliente = Cliente("carol")
cliente.nome