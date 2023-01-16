# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot
from minimizar import minimizar_all

#-----------------------BOT----------------------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

#---------------------FUNÇÕES---------------------------------

def connect_viewer(mensagem):
    acesso = "CODIGO DO SEU TEAM VIEWR"
    bot.send_message(mensagem.chat.id,f'Código de acesso: {acesso}')
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.write('TeamViewer')
    pyautogui.press('enter')
    time.sleep(10)
    bot.send_message(mensagem.chat.id, "--Abrindo aplicativo--")
    pyautogui.moveTo(311, 324)
    pyautogui.mouseDown()
    pyautogui.moveTo(443, 326)
    pyautogui.mouseUp()
    pyautogui.moveTo(366, 324)
    pyautogui.rightClick()
    pyautogui.moveTo(382, 334)
    pyautogui.click()
    bot.send_message(mensagem.chat.id, f'Pegando a senha...')
    pyautogui.press('win')
    pyautogui.write('opera')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(399, 49)
    pyautogui.click()
    pyautogui.write('HTTP DO SEU CHAT DO TELEGRAM OU WTS AQUI')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(5)
    bot.send_message(mensagem.chat.id, f'Enviando a senha:')
    pyautogui.moveTo(911, 1037)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    minimizar_all(mensagem)