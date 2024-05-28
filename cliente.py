class Cliente:
  def __init__(self , n, fone):
    self.nome  = n
    self.telefone = fone

  def mostrar_nome(self):

    print(f'olá {self.nome}')

