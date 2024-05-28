from cliente import Cliente
from conta import Conta

class Main:
  pass
print('testando')


c1 = Cliente('joao', '9121922')
conta = Conta(c1.nome ,7777 , 0)

print(f'{conta.titular} numero: {conta.numero} saldo: {conta.saldo}' )
