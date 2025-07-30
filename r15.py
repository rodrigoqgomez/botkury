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
                'Accept': '*/*',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'text/plain',
                # 'Cookie': 'JSESSIONID=CF2B2C044E120C44D943B2B67766742B; TS01dfd7f9=01a32597e8c9b5d3c20233f0fb299ea446bce256e64d535f575d6e62110c90a92cb7678baeb7eea058a499e4c64df9298d6490be9ce371545e1af91ce8e906f959e83dacc9; _evga_7ecb={%22uuid%22:%220f2b00bcfb7e3a4d%22}; _gcl_au=1.1.1260860188.1741910923; _fbp=fb.1.1741910926276.448138762261136339; _tt_enable_cookie=1; _ttp=01JP8ZPVCS82600NN4G8AYEMQX_.tt.1; _hjSessionUser_671473=eyJpZCI6IjhjZjdiM2ZmLTQxODUtNTIxMy05YmZmLTgxY2Y2YTczNzFhOSIsImNyZWF0ZWQiOjE3NDE5MTA5MzA3NTcsImV4aXN0aW5nIjp0cnVlfQ==; _evga_af86={%22uuid%22:%220f2b00bcfb7e3a4d%22}; _hjSessionUser_5319347=eyJpZCI6IjgzZmMzOWQ2LWQwZGItNTlmNC1iZjEzLWIxYmNlMmRlMWU5YyIsImNyZWF0ZWQiOjE3NDQyMjMxMjgxNTksImV4aXN0aW5nIjpmYWxzZX0=; _sfid_919f={%22anonymousId%22:%220f2b00bcfb7e3a4d%22%2C%22consents%22:[{%22consent%22:{%22purpose%22:%22Personalization%22%2C%22provider%22:%22UAT%20Telcel%22%2C%22status%22:%22Opt%20In%22}%2C%22lastUpdateTime%22:%222025-04-09T18:25:51.982Z%22%2C%22lastSentTime%22:%222025-04-09T18:25:51.985Z%22}]}; _ga_GSFLT13ERL=GS1.1.1744233386.3.1.1744233388.58.0.0; _ga=GA1.1.692562675.1741910924; ttcsid=1744233390301.2.1744233390302; ttcsid_CE8OQMRC77UA21H9M1EG=1744233390301.2.1744233390559; ttcsid_CD6PQDBC77U80187A5V0=1744233390302.2.1744233390559; _ga_7DN9V2VK17=GS1.1.1745982396.1.1.1745982399.0.0.0; TS011a274e=01a32597e8ad150cebedad6e450660b88837e1d27c4d535f575d6e62110c90a92cb7678bae9b717ce9e60891abb6fc305a6af3d015; AMCVS_E5DF7DBC577F6F517F000101%40AdobeOrg=1; AMCV_E5DF7DBC577F6F517F000101%40AdobeOrg=-1303530583%7CMCIDTS%7C20209%7CMCMID%7C42494744016018064960718319195828355797%7CMCAAMLH-1746587204%7C7%7CMCAAMB-1746587204%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1745989604s%7CNONE%7CvVersion%7C3.3.0; s_lv_s=First%20Visit; s_cc=true; _hjSession_671473=eyJpZCI6ImI2OGI3ZGQ5LTY4MDUtNGQzYi1hMjM4LTAxYWVmYmJjOGI5MCIsImMiOjE3NDU5ODI0MDQ3ODUsInMiOjAsInIiOjAsInNiIjowLCJzciI6MCwic2UiOjAsImZzIjowLCJzcCI6MH0=; s_lv=1745982420807; s_sq=telamitelcel%3D%2526c.%2526a.%2526activitymap.%2526page%253Dhttps%25253A%25252F%25252Fmitelcel1.recarga.telcel.com%25252FMiTelcelMXExternalWebAnonymous%25252Fenter.do%25253FAction%25253D1%252526Amount%25253D15%252526ProductCode%25253DILIM30%252526ProductDescription%25253DInternet%25252520por%25252520tiempo%2525252030%252526TelcelChannelID%25253D11%252526TelcelChannelName%25253DTCL%252526UserPlan%25253Dundefined%252526Region%25253Dundefined%252526Profile%25253Dundefin%2526link%253DSiguiente%2526region%253Dpago-factura-paso-2%2526.activitymap%2526.a%2526.c%2526pid%253Dhttps%25253A%25252F%25252Fmitelcel1.recarga.telcel.com%25252FMiTelcelMXExternalWebAnonymous%25252Fenter.do%25253FAction%25253D1%252526Amount%25253D15%252526ProductCode%25253DILIM30%252526ProductDescription%25253DInternet%25252520por%25252520tiempo%2525252030%252526TelcelChannelID%25253D11%252526TelcelChannelName%25253DTCL%252526UserPlan%25253Dundefined%252526Region%25253Dundefined%252526Profile%25253Dundefin%2526oid%253DSiguiente%2526oidt%253D3%2526ot%253DSUBMIT',
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
            }

            data = 'callCount=1\npage=/MiTelcelMXExternalWebAnonymous/enter.do?Action=1&Amount=15&ProductCode=ILIM30&ProductDescription=Internet%20por%20tiempo%2030&TelcelChannelID=11&TelcelChannelName=TCL&UserPlan=undefined&Region=undefined&Profile=undefined&Recomendado=no\nhttpSessionId=\nscriptSessionId=190550306A982BE6D05A52C656DF570D444\nc0-scriptName=Services\nc0-methodName=anonymousRechargeMdnQuery\nc0-id=0\nc0-param0=string:9831172324\nbatchId=0\n'

            response = c.post(
                'https://mitelcel1.recarga.telcel.com/MiTelcelMXExternalWebAnonymous/dwr/call/plaincall/Services.anonymousRechargeMdnQuery.dwr',
                headers=headers,
                data=data,
            )

            
                                                

          

                    
            print("Status Code:", response.status_code)
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4812830883245011|02|2030|000"))