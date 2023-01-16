# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
# ---------------BOT TELEGRAM-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)
# ---------------FUNÇÕES-----------------
def entrar_sala(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('discord')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(30)
    bot.send_message(mensagem.chat.id, "Discord aberto, procurando sala")
    pyautogui.moveTo(-1247, 341)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(-984, 563)
    pyautogui.scroll(-500)
    bot.send_message(mensagem.chat.id, "Estamos dentro ପ૮{˶• ༝ •˶}აଓ")

