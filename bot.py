import asyncio
from telegram import Bot

TOKEN = "8900154827:AAH5ksvET66keQiBXOz5UUq_Y5Itwci6uWA"
CHAT_ID = "6162072304"

bot = Bot(token=TOKEN)

async def main():
    print("Bot isleyir...")

    while True:
        await bot.send_message(chat_id=CHAT_ID, text="heyat gozeldir")
        print("gonderildi")
        await asyncio.sleep(10)

asyncio.run(main())