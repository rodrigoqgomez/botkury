import requests

url = "https://api.anti-captcha.com/getBalance"
payload = {"clientKey": "bf5a65205366ac960191fd60de67463d"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
data = response.json()

if data.get("errorId") == 0:
    print(f"Saldo disponible: ${data['balance']}")
    if "captchaCredits" in data:
        print(f"Créditos de captcha restantes: {data['captchaCredits']}")
else:
    print(f"Error: {data.get('errorDescription', 'Descripción no disponible')}")
