import requests
import time

TOKEN = "8625077430:AAEtRNuiTe87O2tzty_q6uF9elV6gYs-hf0"
CHAT_ID = "6162072304"

while True:

    message = "heyat gozeldir"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }

    requests.post(url, data=payload)

    print("Mesaj gonderildi")

    time.sleep(15)