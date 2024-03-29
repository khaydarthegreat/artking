import database

PAYMENT_MANAGERS = [236030478]
SALES_MANAGERS = [6138005564,56424449]
ANALYTICS = [56424449]  # Add your analytics group's user IDs here

BOT_TOKEN = "5806879239:AAHmFrPnB5k28HtyLgGD3D9ERQh2euymnt8"
MANAGER_URL = "https://t.me/Artbet_k1ng"
BOT_URL = "https://t.me/artkingsbot"
GROUP_ID = "-1001820599351"

def get_card_number():
    return database.get_current_card()  # Fetches the current card number from the database


def set_card_number(new_number):
    global _CARD_NUMBER
    _CARD_NUMBER = new_number

INVOICE_TEXT = """🧾 Заказ на сумму: {amount} рублей.

Для оплаты, нажмите кнопку Оплатить 👇🏻"""

INVOICE_TEXT_VIP = """🧾 Новй заказ.

Подписка на ВИП:{days} дней.

К оплате: {amount} рублей.

Для оплаты, нажмите кнопку Оплатить 👇🏻"""

INVOICE_PAY_BUTTON = "💳 Оплатить"
 

PAYMENT_MESSAGE = """
 👉🏻 Вам необходимо оплатить заказ на сумму {amount} рублей.  

Что оплатить ваш заказ, переведите средства на карту банка РФ

💳 Номер карты для перевода:
{bank} {card_number}

После того, как сделаете перевод, нажмите на кнопку ✅ Я оплатил.

Если возникли трудности с оплатой, нажмите кнопку ❓ Поддержка. """

VIP_PAYMENT_MESSAGE = """
👉🏻 Вам необходимо оплатить Вип подписку на сумму {amount} рублей.  

🕰️ Срок подписки: {subscription_length} дней 

Что оплатить ваш заказ, переведите средства на карту банка РФ

💳 Номер карты для перевода:
{bank} {card_number}

После того, как сделаете перевод, нажмите на кнопку ✅ Я оплатил.

Если возникли трудности с оплатой, нажмите кнопку ❓ Поддержка.  """


I_PAID_TEXT = "✅ Я оплатил"
CONTACT_MANAGER_TEXT = "❓ Поддержка"

ASK_SCREEN_TEXT = """🖼️ Пожалуйста, отправьте боту скриншот вашего перевода для проверки."""

CHECK_SCREEN_TEXT = """🔎 Ваш перевод был отправлен на проверку. 
            
Ожидайте. """


GO_BACK_TEXT = "🔙 Назад "

DEAL_DONE_TEXT = """ ⚽️ Ваш заказ на сумму: {amount} рублей подтвержден!

👇🏻 Нажмите кнопку внизу, чтобы вернуться в диалог и забрать свой прогноз. """

VIP_INVITE_TEXT = """⚽️ Ваша Вип-подписка на сумму {amount }была оплачена! 


⌛️ Дата окончания подписки: {kick_date}
Вы можете всегда запросить бота информацию о вашей подписке отправив ему комманду /myvip

Чтобы вступить в группу, нажмите кнопку внизу. 👇🏻 (❗️Ссылка действует один раз)
"""

GET_SERVICE_TEXT = "👉🏻 Забрать прогноз"

SCREEN_DECLINED_TEXT = """🚫 Бро, что-то пошло не так. 

Скриншот не прошел проверку. Если ты думаешь, что произошла ошибка, напиши менеджеру."""

BOT_CANCEL_TEXT = """❌ Действие было отменено. 

Для продолжения работы с ботом, отправьте комманду /start"""

MY_VIP_TEXT = """⌛️ Ваша подписка на Вип-Чат действительно до {}.

👉🏻 Количество дней до кноца подписки: {}.

↪️ Вы продлили свою подписку {} раз. """
