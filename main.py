import telebot
from telebot import types

# توكن البوت الخاص بك
TOKEN = "8718432157:AAHKg5rcp3g9c7RSggDLyuVUS7unyJGt6wc"
bot = telebot.TeleBot(TOKEN)

# رابط أدسيرا الربحي الخاص بك
AD_LINK = "https://www.profitablecpmratenetwork.com/xqc8sixu?key=b69268fa0361aeda53eeb3cb5212c316"

@bot.message_handler(commands=['start'])
def start(message):
    # إنشاء أزرار احترافية بالإنجليزية
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("🎨 AI Image Generator")
    btn2 = types.KeyboardButton("🌐 Web Search")
    btn3 = types.KeyboardButton("✍️ Text Translation")
    btn4 = types.KeyboardButton("💎 Premium Features")
    markup.add(btn1, btn2, btn3, btn4)
    
    welcome_text = (
        "👋 **Welcome to ChatGPT 5 | DeepSeek Pro**\n\n"
        "To start using our AI features, you must **verify your access** for today.\n\n"
        f"🔗 **Click here to Unlock:** {AD_LINK}\n\n"
        "After clicking, come back and use the buttons below!"
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode="Markdown", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    # رسالة تظهر عند محاولة استخدام البوت بدون ضغط الرابط
    response = (
        "⚠️ **Access Denied!**\n\n"
        "Please verify your free access first to use this feature.\n"
        f"👉 **Unlock here:** {AD_LINK}\n\n"
        "Once done, you can ask me anything!"
    )
    bot.reply_to(message, response, parse_mode="Markdown")

bot.polling()
