from keep_alive import keep_alive
import os
import requests

def send_startup_message():
    chat_id = os.getenv("5768567714")
    token = os.getenv("7863553125:AAFcUIKGAb4NhfbwelZ6HJ7OnTLgxkZa0uQ")
    message = "🚀 PhantomScalerX is now live on Render!"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Failed to send Telegram message:", e)

def run_bot():
    print("PhantomScalerX is now live on Render!")
    send_startup_message()
    # Sniper logic will go here

if __name__ == "__main__":
    keep_alive()
    run_bot()
