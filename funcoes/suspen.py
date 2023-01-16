# ---------------IMPORTS-----------------
import pyautogui
import time
import telebot

# ---------------BOT-----------------
CHAVE_API = 'YOUR API KEY BOT HERE'

bot = telebot.TeleBot(CHAVE_API)

# ---------------FUNÇÕES-----------------
def suspender_pc(mensagem):
    pyautogui.PAUSE = 0.5
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.moveTo(1234, 611)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1135, 500)
    time.sleep(2)
    pyautogui.click()
    pyautogui.click()



def timer_supenser(mensagem):
    try:
        tempo = int(mensagem.text) * 60
        bot.send_message(mensagem.chat.id,f'Tudo certo, daqui {tempo} segundos seu pc será suspenso👌')
        time.sleep(tempo)
        pyautogui.press('f')
        pyautogui.PAUSE = 0.5
        pyautogui.press('win')
        time.sleep(1)
        pyautogui.moveTo(1234, 611)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(1135, 500)
        time.sleep(2)
        pyautogui.click()
        pyautogui.click()
    except:
        bot.send_message(mensagem.chat.id,"Irei entender isso como um cancelamento '-'")

def cancelamento():
    pyautogui.press('f')
    pyautogui.moveTo(1888, 291)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(1679, 41)
    time.sleep(1)
    pyautogui.click()
    pyautogui.click()

