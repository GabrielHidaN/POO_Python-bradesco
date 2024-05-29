from cliente import Cliente
from conta import Conta

class Main:
  pass
print('testando')


c1 = Cliente('joao', '9121922')
conta = Conta(c1.get_nome ,7777 , 0)

conta.deposita(100)
conta.saque(50)
conta.extrato()
