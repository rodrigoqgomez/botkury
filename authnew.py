import ast
import email
from email import message
from encodings.idna import nameprep
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
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; lastPageId=%22943219634083647489%22; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; sakDepth=16; _clsk=1avmkwx%7C1747336758878%7C5%7C1%7Ce.clarity.ms%2Fcollect; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336759$j0$l0$h576195047; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/landingpage--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'handle': 'checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'funnel_step_page_id': '',
                'last_page_id': '943219634083647489',
                'overview': 'false',
                'currencyCode': 'MXN',
            }

            response = c.get(
                'https://www.suerteya.mx/api/multicurrency/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                params=params,

                headers=headers,
            )
            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; sakDepth=19; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336774$j0$l0$h576195047',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'shippingInfo': {
                    'country': 'Mexico',
                },
                'productCheckoutFunnelDtoList': [
                    {
                        'productId': '939122107566731265',
                        'productName': ' Paño de limpieza multifuncional sin rayones',
                        'imageId': '939144983988613122',
                        'productOptionCombineIds': '939122107591897090',
                        'quantity': 1,
                    },
                    {
                        'productId': '939122107566731265',
                        'productName': ' Paño de limpieza multifuncional sin rayones',
                        'imageId': '939145053840551938',
                        'productOptionCombineIds': '939122107596091394',
                        'quantity': 1,
                    },
                ],
                'checkoutToken': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
                'currencyCode': 'MXN',
            }

            response = c.post(
                'https://www.suerteya.mx/api/multicurrency/shippingTemplate',
                
                headers=headers,
                json=json_data,
            )

            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; sakDepth=19; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336774$j0$l0$h576195047',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'shippingTemplateId': '943326905958584321',
                'productCheckoutFunnelDtoList': [
                    {
                        'productId': '939122107566731265',
                        'productName': ' Paño de limpieza multifuncional sin rayones',
                        'imageId': '939144983988613122',
                        'productOptionCombineIds': '939122107591897090',
                        'quantity': 1,
                    },
                    {
                        'productId': '939122107566731265',
                        'productName': ' Paño de limpieza multifuncional sin rayones',
                        'imageId': '939145053840551938',
                        'productOptionCombineIds': '939122107596091394',
                        'quantity': 1,
                    },
                ],
                'discountCodes': '',
                'checkoutToken': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
                'calPromotionFlag': True,
                'tipPrice': 0,
                'calInsuranceFlag': False,
                'shippingInsuranceChecked': False,
                'currencyCode': 'MXN',
            }

            response = c.post(
                'https://www.suerteya.mx/api/multicurrency/calculatePrice',
               
                headers=headers,
                json=json_data,
            )

            headers = {
                'authority': 'tracking.myshopage.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'trace_id': '921458970726211585',
                'uuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'browse_url': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'event_type': 'funnel_checkoutBtn_click',
                'timestamp': 1747336881774,
                'order_id': '',
                'order_name': '',
                'order_token': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
                'currency': 'MXN',
                'value': 398.99,
                'items': [
                    {
                        'id': 'CP59692-X46752',
                        'name': ' Paño de limpieza multifuncional sin rayones',
                        'quantity': 1,
                        'price': 299.99,
                    },
                ],
                'funnel_id': '943216860117782540',
                'funnel_handle': 'checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'on': True,
                'off': False,
            }

            response = c.post('https://tracking.myshopage.com/api/tracking', headers=headers, json=json_data)
            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336774$j0$l0$h576195047; sakDepth=29',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'countryCode': 'MX',
                'state': 'Yucatán',
                'zip': '97910',
            }

            response = c.get('https://www.suerteya.mx/api/base-districts/check/zip', params=params,  headers=headers)

            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336774$j0$l0$h576195047; sakDepth=29',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'token': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
            }

            response = c.post(
                'https://www.suerteya.mx/api/paymentStrategy/getOceanOrderHandle',
                headers=headers,
                json=json_data,
            )

            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747336774$j0$l0$h576195047; sakDepth=29',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'productCheckoutFunnelDtoList': [
                    {
                        'productId': '939122107566731265',
                        'productName': ' Paño de limpieza multifuncional sin rayones',
                        'quantity': 1,
                        'imageId': '939144983988613122',
                        'productOptionCombineIds': '939122107591897090',
                    },
                ],
                'shippingTemplateId': '943326905958584321',
                'currencyCode': 'MXN',
                'nextHandle': 'upsell--pa-o-de-limpieza-multifuncional-sin-rayones',
                'asShippingAddress': 1,
                'funnelId': '943216860117782540',
                'shippingInfo': {
                    'email': email,
                    'firstName': name,
                    'lastName': last,
                    'country': 'Mexico',
                    'address1': 'Calle Uuguay 410',
                    'address2': 'calle Uruguay 410',
                    'city': 'Chetumal',
                    'province': 'Quintana Roo',
                    'provinceCode': '',
                    'zip': '97910',
                    'phone': '9971556986',
                },
                'email': email,
                'checkoutToken': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
                'funnelHandle': 'checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'paymentMethodCode': 'oceanpayment_onepage_checkout',
                'discountCodes': '',
                'calPromotionFlag': True,
                'tipPrice': 0,
                'shippingInsurancePrice': 0,
            }

            response = c.post('https://www.suerteya.mx/api/multicurrency/funnel-buy',  headers=headers, json=json_data)

            headers = {
                'authority': 'www.suerteya.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic 6JGj6L-c5bOwOmExMjM0NTY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'sakUUID=ba73c1e6-c757-4f3d-9390-468b5dac4d5c; soundestID=20250515191845-g3rkMPlqoTmCmfQj3aKuujRuS5msPOIXvurYsNQVntB6PGrWJ; omnisendSessionID=8B4gqEJDCJGV2X-20250515191845; sak-locale=es; _fbp=fb.1.1747336726721.878281480461112766; _gcl_au=1.1.2110293340.1747336727; _ga=GA1.1.1291803887.1747336727; _clck=bxp1w4%7C2%7Cfvx%7C0%7C1961; _cbp=fb.1.1747336727514.1780273869; STOREPATH=%2F; landingpage--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943219634083647489; FUNNELPATH=%2Ffunnel%2Fcheckout--pa-o-de-limpieza-multifuncional-sin-rayones; lastPageId=%22943216860142948354%22; checkout--pa-o-de-limpieza-multifuncional-sin-rayones=funnel-943216860142948354; funnelToken=abdfbbfc61bb42cd9b85a9c57221b6e4; _clsk=1avmkwx%7C1747336774005%7C6%7C1%7Ce.clarity.ms%2Fcollect; sakDepth=29; _ga_S8KVZ34G1C=GS2.1.s1747336727$o1$g1$t1747337076$j0$l0$h576195047',
                'customeruuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
                'origin': 'https://www.suerteya.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.suerteya.mx/funnel/checkout--pa-o-de-limpieza-multifuncional-sin-rayones',
                'saklang': 'es',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sign': '',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'token': 'abdfbbfc61bb42cd9b85a9c57221b6e4',
                'nextHandle': 'upsell--pa-o-de-limpieza-multifuncional-sin-rayones',
                'code': 'oceanpayment_onepage_checkout',
                's': '411b1752b6f6d78d0cfe4ebd2387dbdbf1b8dbf8f89305afd574525cba8a341a',
                't': 1747337076518,
                '_atr': 1747090767385,
                '_step': '2efyjm70',
                '_pay': '89f934ebb3032c09ac963a66d7207b06',
                'uuid': 'ba73c1e6-c757-4f3d-9390-468b5dac4d5c',
            }

            response = c.post('https://www.suerteya.mx/api/paymentStrategy',  headers=headers, json=json_data)


            #responsePm = json.loads(response.text)
           # print(responsePm)



                                    
            
            print("Status Code:", response.status_code)
           
        


            
            
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4812830882403017|02|2030|159"))