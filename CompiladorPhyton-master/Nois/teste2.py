from typing import NamedTuple, Union

ERRO = 0
IDENTIFICADOR = 1
NUM_INT = 2
NUM_REAL = 3
EOS = 4

class Atomo(NamedTuple):
  tipo: int
  lexema: str
  valor: Union[int, float]
  linha: int


class Analisador_Lexico:
  def __init__(self, buffer):
    self.buffer = buffer + '\0'
    self.i = 0
    self.nlinha = 1

  def proximo_char(self):
     c = self.buffer[self.i]
     self.i += 1
     return c

  def retrair(self):
    self.i -= 1

  def tratar_identificador(self):
    lexema = self.buffer[self.i - 1]
    c = self.proximo_char()
    while (c.isalpha() or c.isdigit()):
      lexema = lexema + c
      c = self.proximo_char()
    self.retrair()
    return Atomo(IDENTIFICADOR, lexema, 0, self.nlinha)

  def tratar_numeros(self):
    lexema = self.buffer[self.i - 1]
    estado = 1
    c = self.proximo_char()

    while True:
      if estado == 1:
        if c.isdigit():
          lexema = lexema + c
          estado = 1
        elif c == '.':
          lexema = lexema + c
          estado = 3
        else:
          estado = 2
          continue
      elif estado == 2:
        self.retrair()
        return Atomo(NUM_INT, lexema, int(lexema), self.nlinha)
      elif estado == 3:
        if c.isdigit():
          lexema = lexema + c
          estado = 4
        else:
          return Atomo(ERRO, '', 0, self.nlinha)
      elif estado == 4:
        if c.isdigit():
          lexema = lexema + c
          estado = 4
        else:
          estado = 5
          continue
      elif estado == 5:
        self.retrair()
        return Atomo(NUM_REAL, lexema, float(lexema), self.nlinha)
      
      c = self.proximo_char()
  
  def proximo_atomo(self):
    atomo = ERRO

    c = self.proximo_char()
    while c in [' ', '\t', '\n', '\0']:
      if c == '\n':
        self.nlinha = self.nlinha + 1
      if c == '\0':
        return Atomo(EOS, '', 0, self.nlinha)
      c = self.proximo_char()
    if c.isalpha():  
      atomo = self.tratar_identificador()
    elif c.isdigit():  
      atomo = self.tratar_numeros()
    return atomo
    

def leia_arquivo():
  arquivo = open('portugul.ptl', 'r')
  buffer = arquivo.read()
  arquivo.close()
  return buffer


def main():
  buffer = leia_arquivo()
  lexico = Analisador_Lexico(buffer)
  msg_atomo = ['ERRO', 'IDENTIF', 'NUM_INT', 'NUM_REAL', 'EOS']
  atomo = lexico.proximo_atomo()
  while (atomo.tipo != ERRO and atomo.tipo != EOS):
    print('Linha: {}  - atomo: {} \t lexema: {}'.format(atomo.linha, msg_atomo[atomo.tipo], atomo.lexema))
    atomo = lexico.proximo_atomo()


main()

x = 3E5

print(x)