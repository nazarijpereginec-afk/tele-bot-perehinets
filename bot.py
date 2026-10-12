import telebot
from telebot import types

from pr1 import Catalog

TOKEN = "8414724586:AAFcIsl5b6BUozQk8fld7Z7FO_6tUzIiMsk"

bot = telebot.TeleBot(TOKEN)

# дані 
tours = Catalog()
tours.read_from_file("dataTours.txt")

# кнопки 
def main_keyboard():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add("🌍 Усі тури", "🟢 Вільні тури")
    kb.add("📝 Забронювати тур")
    kb.add("ℹ Про агенство", "🌐 Наш сайт")
    return kb


# старт 
@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(
        msg.chat.id,
        "👋 <b>Вітаємо!</b>\n"
        "Я бот туристичного агентства ✈️\n\n"
        "👇 Оберіть дію з меню нижче:",
        reply_markup=main_keyboard(),
        parse_mode="HTML"
    )


# усі тури 
@bot.message_handler(func=lambda m: m.text == "🌍 Усі тури")
def all_tours(msg):
    text = "📋 <b>Список турів:</b>\n\n"

    for t in tours._Catalog__tours:
        text += (
            f"🌎 <b>{t.get('country')}</b>\n"
            f"💰 Ціна: {t.get('price')} грн\n"
            f"👥 Місця: {t.get('booked')}/{t.get('slots')}\n"
            f"📝 {t.get('description')}\n\n"
        )

    bot.send_message(msg.chat.id, text, parse_mode="HTML")


# вільні тури
@bot.message_handler(func=lambda m: m.text == "🟢 Вільні тури")
def free_tours(msg):
    text = "✅ <b>Доступні тури:</b>\n\n"

    for t in tours._Catalog__tours:
        if t.get("booked") < t.get("slots"):
            text += (
                f"🌍 <b>{t.get('country')}</b>\n"
                f"💵 {t.get('price')} грн\n"
                f"🟢 Вільно місць: {t.get('slots') - t.get('booked')}\n\n"
            )

    bot.send_message(msg.chat.id, text, parse_mode="HTML")


# забронювати тур
@bot.message_handler(func=lambda m: m.text == "📝 Забронювати тур")
def book_info(msg):
    bot.send_message(
        msg.chat.id,
        "📝 <b>Бронювання туру</b>\n\n"
        "📌 Для оформлення бронювання:\n"
        "• оберіть тур у списку\n"
        "• зверніться до менеджера\n\n"
        "📞 Телефон: <b>+380 96 744 01 35</b>\n"
        "📱 Або скористайтесь нашим додатком",
        parse_mode="HTML"
    )


# про агенство
@bot.message_handler(func=lambda m: m.text == "ℹ Про агенство")
def about(msg):
    bot.send_message(
        msg.chat.id,
        "🏢 <b>Туристичне агентство</b>\n\n"
        "✈️ Кращі тури по всьому світу\n"
        "🌍 Найпопулярніше агентство в Україні\n\n"
        "👤 Власник: Перегінець Назарій Володимирович\n"
        "📞 Телефон: <b>+380 96 744 01 35</b>",
        parse_mode="HTML"
    )


# наш сайт
@bot.message_handler(func=lambda m: m.text == "🌐 Наш сайт")
def site(msg):
    kb = types.InlineKeyboardMarkup()
    kb.add(
        types.InlineKeyboardButton(
            text="🌐 Перейти на сайт",
            url="https://www.poehalisnami.ua/ua"
        )
    )

    bot.send_message(
        msg.chat.id,
        "🌐 <b>Наш офіційний сайт</b>",
        reply_markup=kb,
        parse_mode="HTML"
    )


# запуск бота
bot.polling(none_stop=True)
