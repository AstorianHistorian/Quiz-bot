from time import time
from telepot.namedtuple import KeyboardButton,ReplyKeyboardMarkup
import telepot as t
from csv import reader
import random

def test(update,responce):
     msg = f"Проверка"


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("Привет", 'Эй', "Здравствуйте"):
       return "Привет!"

    if user_message in ("1", '2', '3', '4'):
        return user_message

    return "Я не знаю такой команды"