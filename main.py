# --------------------IMPORTS----------------
import pyautogui
import telebot

from funcoes.backup_drive import drive_backup
from funcoes.tokinho import tokin
from funcoes.limpeza import fechar_all
from funcoes.get_email import print_mail
from funcoes.discord_enter import entrar_sala
from funcoes.suspen import suspender_pc, timer_supenser, cancelamento
from funcoes.teamView import connect_viewer
from funcoes.previsao import previsao_tempo
from funcoes.teste import scroll
from funcoes.youtub import carregar_video
from funcoes.minimizar import minimizar_all
from funcoes.escrev import escreva
#from funcoes.boleto import pega_boleto
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

# ------------------------------PRINTS TELA---------------

texto = """
    Olá! Como posso ajudar?
    
/boleto   -  (Para receber o boleto do iesb por aqui)

/drive    -  (Para subir algum arquivo do seu desktop para o drive)

/diario   -  (Comandos para se usar diariamente)

/discord  -  (Conectar ao discord da empresa)

/limpar   -  (Feche todas as abas no servidor)

"""

texto_suspender = """
    Qual opçao deseja?
    
    /tempo  -   Colocar um temporizador para o pc suspender
    
    /agora  -   Suspender imediatamente
"""

texto_diario = """
    /tokinho  -  (Ative o bot tokinho)
    
    /email    -  (Ver os ultimos 5 emails na caixa de email)
    
    /teamViewer - (Conectar um pc ao seu)

    /suspender - (Suspender o pc)
    
    /clima     - (Previsão de hoje)

    /minimiza  - (Minimiza todas as abas)
"""

# ------------------------------------------------------------------------------------------

#------------------------------FUNÇÕES/COMANDOS------------------------------------------------------------

@bot.message_handler(commands=['boleto'])
#def boleto(mensagem):
    #bot.send_message(mensagem.chat.id, "███░░,🔜⌛")
    #pega_boleto(mensagem)


@bot.message_handler(commands=['drive'])
def drive(mensagem):
    bot.send_message(mensagem.chat.id, "⋘ ...𝑃𝑙𝑒𝑎𝑠𝑒 𝑤𝑎𝑖𝑡... ⋙")
    drive_backup(mensagem)


@bot.message_handler(commands=['tokinho'])
def tokinho(mensagem):
    bot.send_message(mensagem.chat.id, "Tokin is comming...")
    tokin(mensagem)


@bot.message_handler(commands=['email'])
def email(mensagem):
    bot.send_message(mensagem.chat.id, "𝐍𝐨𝐰 𝐥𝐨𝐚𝐝𝐢𝐧𝐠...")
    print_mail(mensagem)


@bot.message_handler(commands=['discord'])
def discord(mensagem):
    bot.send_message(mensagem.chat.id, "Abrindo discord..")
    entrar_sala(mensagem)


@bot.message_handler(commands=['limpar'])
def limpar(mensagem):
    bot.send_message(mensagem.chat.id, "Cleaning.. 🧹👩🏻‍🍳💨")
    fechar_all(mensagem)


@bot.message_handler(commands=['teamViewer'])
def teamViewer(mensagem):
    connect_viewer(mensagem)


@bot.message_handler(commands=['suspender'])
def suspender(mensagem):
    bot.send_message(mensagem.chat.id, texto_suspender)


@bot.message_handler(commands=['diario'])
def diario(mensagem):
    bot.send_message(mensagem.chat.id, texto_diario)

@bot.message_handler(commands=['escrever'])
def escrever(mensagem):
    msg = bot.send_message(mensagem.chat.id, "Oq deseja digitar?")
    bot.register_next_step_handler(msg, escreva)

@bot.message_handler(commands=['clima'])
def clima(mensagem):
    bot.send_message(mensagem.chat.id, "Buscando informações")
    previsao_tempo(mensagem)

@bot.message_handler(commands=['agora'])
def agora(mensagem):
    bot.send_message(mensagem.chat.id, "PC SUSPENSO, ATé LOgo,.;~][😴")
    suspender_pc(mensagem)

@bot.message_handler(commands=['tempo'])
def tempo(mensagem):
    msg = bot.send_message(mensagem.chat.id, "Daqui quantos minutos deseja suspender o pc?")
    bot.register_next_step_handler(msg, timer_supenser)

@bot.message_handler(commands=['teste'])
def tempo(teste):
    scroll()

@bot.message_handler(commands=['cancelar'])
def cancelar(mensagem):
    bot.send_message(mensagem.chat.id, "SUSPENSÃO AUTOMÁTICA DESLIGADA!")
    cancelamento()

@bot.message_handler(commands=['minimiza'])
def minimiza(mensagem):
    minimizar_all(mensagem)

#------------------------------MEXER DIRETAMENTE NO PC QUANDO TIVER NO YOUTUB------------------------------
def link(mensagem):
    if mensagem.text.find("youtu") != -1:
        carregar_video(mensagem)
    else:
        return False

def conferir(mensagem):
    http = "https"
    if mensagem.text == 'Q':
        pyautogui.hotkey('ctrl', '+')
        return
    if mensagem.text == 'P':
        pyautogui.hotkey('ctrl', '-')
        return
    if mensagem.text == 'A':
        pyautogui.press('left')
        return
    if mensagem.text == 'L':
        pyautogui.press('right')
        return
    if mensagem.text == 'Qq':
        pyautogui.hotkey('ctrl', '+')
        pyautogui.hotkey('ctrl', '+')
        return
    if mensagem.text == 'Pp':
        pyautogui.hotkey('ctrl', '-')
        pyautogui.hotkey('ctrl', '-')
        return
    if mensagem.text == ',':
        for c in range(5):
            pyautogui.press('volumedown')
        return
    if mensagem.text == '.':
        for c in range(5):
            pyautogui.press('volumeup')
        return
    if mensagem.text == 'G':
        pyautogui.press('space')
        return
    if mensagem.text == 'F':
        pyautogui.press('f')
        return
    if mensagem.text.find(http) == -1:
        bot.send_message(mensagem.chat.id, "No comprendo .-.")
        return


@bot.message_handler(func=conferir)

@bot.message_handler(func=link)

#------------------------------------------------------------------------------------------

@bot.message_handler(commands=['oi'])
def oi(message):
    bot.send_message(message.chat.id, texto)


pyautogui.FAILSAFE = False

bot.polling()
