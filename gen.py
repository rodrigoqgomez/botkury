import random, os
import telebot
import requests
import globals  # Importa globals.py

if globals.current_group_id is None:
    id = globals.current_user_id
    print(globals.current_user_id)
else:
    id = globals.current_group_id
    print(globals.current_group_id)

tokenid = "6942163992:AAHmObNKmBh1nxRlmPVmyRwIqKCQD4o0Wc0"
bot = telebot.TeleBot(tokenid, parse_mode="HTML")
TELEGRAM_API_URL = f"https://api.telegram.org/bot{tokenid}/sendMessage"

# Esta es la función principal que genera los números de tarjeta y los envía al chat de Telegram
def process_message(cleaned_string):
    # Determina si es un usuario o grupo
    if globals.current_group_id is None:
        id = globals.current_user_id
        print(globals.current_user_id)
    else:
        id = globals.current_group_id
        print(globals.current_group_id)
    
    # Extrae los datos de cleaned_string (el mensaje de Telegram)
    file = [cleaned_string.rstrip()]
    quantity = 10
    x = 0
    ccnum = 0
    output = ""

    # Luhn Algorithm para validar números de tarjeta
    def luhn_checksum(card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d * 2))
        return checksum % 10
    
    # Procesamiento de cada línea del archivo simulado (message limpio)
    for lines in file:
        cardss = lines.split('|')
        cc = cardss[0]
        mes = cardss[1]
        ano = cardss[2]
        cvv = cardss[3]
        good = 16 - len(cc)

        # Genera el número de tarjeta y verifica con el algoritmo de Luhn
        while x != quantity:
            r = str(random.randint(pow(10, good - 1), (pow(10, good)) - 1))
            iccnum = cc + r

            if luhn_checksum(int(iccnum)) == 0:
                ccnum = iccnum
                exp_month = mes
                exp_year = str(ano)
                cvv = str(random.randint(100, 999)) if cvv != '000' else '000'
                CC = str(ccnum + "|" + exp_month + "|" + exp_year + "|" + cvv + "\n")
                output += CC
                x += 1
    
    # Enviar el resultado a Telegram
    respuesta = output
    params = {"chat_id": id, "parse_mode": "Markdown", "text": respuesta}
    requests.get(TELEGRAM_API_URL, params=params)
    
    return respuesta  # Devolvemos la respuesta generada para uso posterior

