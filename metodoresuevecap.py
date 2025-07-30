# pip install anticaptchaofficial

from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless

# Clave de API de AntiCaptcha
api_key = "bf5a65205366ac960191fd60de67463d"

# URL del sitio donde se encuentra el reCAPTCHA
website_url = "https://redphone.api.koonolmexico.com/payment_cards"

# Sitekey del reCAPTCHA (obtenido del HTML del sitio)
sitekey = "6LeRoVMUAAAAAGvv93qaFm8mOppFzZsq_FKIgHll"

# Crear y configurar el solver
solver = recaptchaV2Proxyless()
solver.set_verbose(1)
solver.set_key(api_key)
solver.set_website_url(website_url)
solver.set_website_key(sitekey)

print("⏳ Enviando tarea a AntiCaptcha...")

# Intentar resolver el CAPTCHA
g_response = solver.solve_and_return_solution()

if g_response != 0:
    print("✅ CAPTCHA resuelto correctamente.")
    print("Token:", g_response)

    # Puedes usar este token para enviarlo al formulario del sitio
else:
    print(f"❌ Error al resolver CAPTCHA: {solver.error_code}")
