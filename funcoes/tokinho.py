# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
from minimizar import minimizar_all
# ---------------BOT TELEGRAM-----------------
CHAVE_API_BOT_LOTOFACIL = 'YOUR API KEY BOT HERE'

CHAVE_API = 'YOUR API KEY BOT HERE'

cleiton = telebot.TeleBot(CHAVE_API)

tokinho = telebot.TeleBot(CHAVE_API_BOT_LOTOFACIL)
# ---------------FUNÇÃO-----------------

def tokin(mensagem):
    url_drive = 'URL DE ONDE O BOT DA LOTOFACIL ESTA NO SEU DRIVE'
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('opera')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.write(url_drive)
    time.sleep(3)
    pyautogui.press('enter')
    pyautogui.moveTo(414, 367)
    time.sleep(3)
    cleiton.send_message(mensagem.chat.id, "Calma, ele está se arrumando.")
    pyautogui.click()
    pyautogui.press('enter')
    time.sleep(16)
    cleiton.send_message(mensagem.chat.id, "Só mais um pouquinho...")
    pyautogui.moveTo(406, 152)
    pyautogui.click()
    time.sleep(2)
    pyautogui.moveTo(421, 185)
    pyautogui.click()
    time.sleep(4)
    cleiton.send_message(mensagem.chat.id, "Sdds pontualidade...")
    time.sleep(7)
    tokinho.send_message(mensagem.chat.id, "To quase chegando calmi calmi")
    time.sleep(10)
    tokinho.send_message(mensagem.chat.id, "CHEGAAAY ε(´｡•᎑•`)っ 💕")
    minimizar_all(mensagem)