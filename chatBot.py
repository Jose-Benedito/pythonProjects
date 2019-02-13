import json
import sys
import os
class Chatbot():
    def __init__(self):
        print("=================ChatBot=============")
        print(" Digite: oi para começar\n"
              "Digite: 'aprende' para aprender\n"
              "Digite em letras minusculas e sem acentos.")
        print("======================================")
        try:
            memoria = open('Jarvis.json','r')
        except FileNotFoundError :
            memoria = open('Jarvis.json','w')
            memoria.write('["Bene","Roberto","Jose"]')
            memoria.close()
            memoria = open('Jarvis.json','r')
        self.conhecidos = json.load(memoria)
        memoria.close()

#===============memoria2===========================
        try:
            memoria2 = open('novasFrases.json','r')
        except FileNotFoundError :
            memoria2 = open('novasFrases.json','w')
            memoria2.write('{"oi":"Qual é seu nome?","tchau":"Até breve"}')
            memoria2.close()
            memoria2 = open('novasFrases.json','r')
        self.frases = json.load(memoria2)
        memoria2.close()

        self.historico = []
      #  self.frases = {'oi': 'Olá, qual é o seu nome?', 'tchau': 'tchau,tchau'}
#=================================Responde ao usuário====================
    def fala(self, frase):
        if 'executa' in frase:
            plataforma = sys.platform
            comando = frase.replace('executa','')
            if 'win' in plataforma :
                os.startfile(comando)

        print(frase)
        self.historico.append(frase)
#=========================lê a frase do usuário==========================
    def escuta(self):
        frase = input(' ')
        frase = frase.lower() #converte a frase em letras minúsculas
        frase = frase.replace('é', 'eh') # verficar variantes
        return frase
#=========================processa a frase==================================
    def pensa(self, frase):
        if frase in self.conhecidos:
            return self.conhecidos[frase]
        if frase in self.frases : # verifica se a frase está na lista de frases
            return self.frases[frase]

        if frase == 'aprende':      # inicia o aprendizado de novas frases, caso o comando seja 'aprende'
            chave = input('Digite a frase: ')
            resp = input('Digite a resposta: ')
            self.frases[chave] = resp         # associa a chave(pergunta) com o valor(resposta) para o Dicionário


    #===========================teste de inclusão na memória=================

            memoria2 = open('novasFrases.json', 'w')
            json.dump(self.frases, memoria2)
            memoria2.close()
            return 'Aprendido'
        # verificação de nomes no cumprimento
        if self.historico[-1] == 'Ola, qual e o seu nome?':
            nome = self.pegaNome(frase)
            resp = self.respondeNome(nome)
            return resp
        #try:
           # resp = str(eval(frase))
           # return resp
        #except:
            #pass
        return 'Não entendi'


#===========================Tratamento de nome=============================
    def pegaNome(self, nome):
        if 'o meu nome eh 'in nome:
            nome = nome[14:]
            nome = nome.title()
            return nome
        else :
            nome = nome.title()
        return nome
#================================Resposta de cumprimento====================
    def respondeNome(self, nome):
        if nome in self.conhecidos:
            frase = 'Bom revê-lo, '
        else:
            frase = 'Muito prazer, '
            self.conhecidos.append(nome)
            memoria = open('Jarvis.json','w')
            json.dump(self.conhecidos,memoria)
            memoria.close()
        return frase + nome

