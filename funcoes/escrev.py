# ---------------IMPORTS-----------------
import pyautogui
import telebot
#----------------------------------------------------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)
#----------------------FUNÇÃO------------------------------------

def escreva(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('backspace')
    pyautogui.write(mensagem.text)
    pyautogui.press('enter')