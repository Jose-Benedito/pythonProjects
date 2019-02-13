from chatBot import Chatbot

bot = Chatbot()
while True:
    frase = bot.escuta()
    resp = bot.pensa(frase)
    bot.fala(resp)
    if resp == 'tchau':
        break
