class Conta:
  def __init__(self ,  titular , numero , saldo):
    self.titular = titular
    self.numero = numero
    self._saldo = 0

  @property
  def get_saldo(self):
    return self._saldo


  def set_saldo(self,saldo):
    if (saldo<0):
      print("@@@ O saldo não pode ser negativo! @@@")

    else:
      self._saldo = saldo

  def saque(self , valor):
    if (self._saldo >= valor):
      self._saldo -= valor
      print('Saque Realizado com sucesso!')

    else:
      print('saldo insuficiente!')

  def deposita (self , valor):
    self._saldo += valor

  def extrato (self):
   print( f"Cliente: {self.titular} , Saldo atual: {self._saldo}")
