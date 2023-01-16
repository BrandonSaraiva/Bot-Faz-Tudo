#------------------------------IMPORTS------------------------------
import pyautogui
import time
import telebot
from PIL import Image
# ---------------BOT TELEGRAM-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

#########################     NÃO TERMINEI O BOLETO AINDA PQ PRECISO ESPERAR ELE FICAR DISPONIVEL NO SITE PARA TERMINAR

# ---------------FUNÇÃO----------------------------
#def pega_boleto(mensagem):
    #image = Image.open('download.png')
#
    #pyautogui.PAUSE = 0.5
    #pyautogui.press('win')
    #time.sleep(1)
    #pyautogui.write('opera')
    #pyautogui.press('enter')
    #time.sleep(4)
    #pyautogui.moveTo(465, 80)
    #pyautogui.click()
    #time.sleep(2)
    #pyautogui.write('YOUR LOGIN HERE')
    #pyautogui.press('enter')
    #pyautogui.write('YOUR PASSWORD HERE')
    #pyautogui.press('enter')
    #time.sleep(1)
    #pyautogui.press('enter')
    #pyautogui.moveTo(800,181)
    #time.sleep(1)
    #pyautogui.moveTo(821, 213)
    #pyautogui.click()
    #bot.send_message(mensagem.chat.id, f'testeee')
    #time.sleep(1)
    #location = pyautogui.locateOnScreen(image)
    #time.sleep(2)
    #bot.send_message(mensagem.chat.id,f'Localização === {location}')