from keep_alive import keep_alive
import os
import requests

import requests

def send_startup_message():
    chat_id = "5768567714"
    token = "7863553125:AAFcUIKGAb4NhfbwelZ6HJ7OnTLgxkZa0uQ"
    message = "🚀 PhantomScalerX is now live on Render!"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}
    
    print("Sending Telegram message...")
    print(f"Token starts with: {token[:10]}")
    print(f"Chat ID: {chat_id}")
    print(f"URL: {url}")
    
    try:
        response = requests.post(url, data=data)
        print("Telegram response:", response.status_code, response.text)
    except Exception as e:
        print("Failed to send Telegram message:", e)

def run_bot():
    print("PhantomScalerX is now live on Render!")
    send_startup_message()
    # Sniper logic will go here

if __name__ == "__main__":
    keep_alive()
    run_bot()
