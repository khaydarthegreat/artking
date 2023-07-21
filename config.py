import database

PAYMENT_MANAGERS = [236030478]
SALES_MANAGERS = [6138005564,56424449]
ANALYTICS = [56424449]  # Add your analytics group's user IDs here

BOT_TOKEN = "5806879239:AAHmFrPnB5k28HtyLgGD3D9ERQh2euymnt8"
MANAGER_URL = "https://t.me/Artbet_k1ng"
BOT_URL = "https://t.me/artkingsbot"




def get_card_number():
    return database.get_current_card()  # Fetches the current card number from the database


def set_card_number(new_number):
    global _CARD_NUMBER
    _CARD_NUMBER = new_number
