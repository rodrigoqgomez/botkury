import requests
import time

api_key = "15a7d37c2e38321b89c6f9ac050f5b1c"  # Tu clave de CapMonster

# Paso 1: Crear tarea
create_task_url = "https://api.capmonster.cloud/createTask"
payload = {
    "clientKey": api_key,
    "task": {
        "type": "NoCaptchaTaskProxyless",
        "websiteURL": "https://www.google.com/recaptcha/api2/demo",
        "websiteKey": "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
    }
}

print("📤 Enviando tarea de captcha a CapMonster...")
response = requests.post(create_task_url, json=payload)
result = response.json()

if result.get("errorId") != 0:
    print(f"❌ Error al crear tarea: {result.get('errorCode')}")
    exit()

task_id = result["taskId"]
print("🆔 Tarea creada con ID:", task_id)

# Paso 2: Esperar a que CapMonster resuelva
get_result_url = "https://api.capmonster.cloud/getTaskResult"
for i in range(20):
    time.sleep(5)
    res = requests.post(get_result_url, json={
        "clientKey": api_key,
        "taskId": task_id
    })
    res_json = res.json()

    if res_json.get("status") == "ready":
        token = res_json["solution"]["gRecaptchaResponse"]
        print("✅ CAPTCHA resuelto. Token:", token)
        break
    else:
        print(f"⏳ Esperando solución ({i+1}/20)...")

else:
    print("❌ Tiempo de espera agotado.")
