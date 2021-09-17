import sys
import os.path

# Bliblioteca padrao de string
import string


class AnalisadorLexico():

    

  def __init__(self):
    self.arquivo_e = "\portugul.ptl"
    self.arquivo_r = "retorno.txt"

  def ifDelimitador(self, caracter):
    delimitadores = [' ', '\t', '\n', '\0']
    if caracter in delimitadores:
      return True
    return False

  def ifReservada(self, caracter):
    reservadas = ['ALGORITMO','ATE','CADEIA', 'CARACTER','ENQUANTO','ENTAO','FACA','FIM','FUNCAO','INICIO','INTEIRO','PARA','PASSO','PROCEDIMENTO','REAL','REF','RETORNE','SE','SENAO','VARIAVEIS',]
    if caracter in reservadas:
      return True
    return False

  def AtomoDefineReservada(self, entrada):
    reservadas = ['ALGORITMO','ATE','CADEIA', 'CARACTER','ENQUANTO','ENTAO','FACA','FIM','FUNCAO','INICIO','INTEIRO','PARA','PASSO','PROCEDIMENTO','REAL','REF','RETORNE','SE','SENAO','VARIAVEIS',]
    posicao = delimitadores.find(entrada)
    return ""

  def ifRelacional(self, caracter):
    reservadas = ['ALGORITMO','ATE','CADEIA', 'CARACTER','ENQUANTO','ENTAO','FACA','FIM','FUNCAO','INICIO','INTEIRO','PARA','PASSO','PROCEDIMENTO','REAL','REF','RETORNE','SE','SENAO','VARIAVEIS',]
    if caracter in reservadas:
      return True
    return False


  def proximo_atomo(self):
    arquivo_saida = open(self.arquivo_r, 'w')
    arquivo_entrada = open(self.arquivo_e, 'r')

    linha_programa = arquivo_entrada.readline()
    numero_linha = 1
    while linha_programa:
        i = 0
        tamanho_linha = len(linha_programa)
        a = linha_programa.split()
        print(a)
    #   while i < tamanho_linha:  
    #     caracter_atual = linha_programa[i] 
    #     caractere_seguinte = None

    #     if ((i+1) < tamanho_linha):
    #       caractere_seguinte = linha_programa[i+1] 


    #     if (~self.ifDelimitador(caracter_atual)):
    #         if (self.ifReservada(caracter_atual)):
    #             arquivo_saida.write()
    #     i += 1
        #   arquivo_saida.write(self.qualTokenDelimitador(caracter_atual)+'_'+caracter_atual+'->'+str(numero_linha)+'\n')







    # if not os.path.exists(self.arquivo_entrada):
    #   arquivo_saida.write("Arquivo de entrada inexistente")
    #   return







