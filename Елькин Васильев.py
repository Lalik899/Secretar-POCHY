import logging
from telegram import Update, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
    ContextTypes
)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = 'TOKEN'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["Адрес техникума", "Стоимость обучения"],
        ["Специальности"],
        ["Связь с нами"]
    ]
    
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    
    await update.message.reply_text(
        "Добро пожаловать! Выберите информацию:",
        reply_markup=reply_markup
    )

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "Адрес техникума":
        await update.message.reply_text("г. Ижевск, Молодежная 109")
    
    elif text == "Стоимость обучения":
        await update.message.reply_text("~100.000р в год. Для более подробной информации свяжитесь с приёмной комиссией.")
    
    elif text == "Связь с нами":
        await update.message.reply_text("Приемная директора:(3412)370288, \nПриемная комиссия:(3412)370488, \nБухгалтерия: +7(3412) 37-05-00, \nОчное отделение: +7(3412) 37-02-00, \nЗаочное отделение: +7(3412) 37-02-77, \nОбщежитие: +7(3412) 37-04-88")
    elif text == "Специальности":
        await update.message.reply_text("Поварское и кондитерское дело, \nТуризм и гостеприимство, \nЮриспруденция, \nПравоохранительная деятельность, \nКомерция, \nФинансы, \nТорговое дело, \nДизайн, \nИнформационные системы и программирование")
        

async def handle_inline_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    

def main():
    application = Application.builder().token(TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_buttons))
    application.add_handler(CallbackQueryHandler(handle_inline_buttons))
    
    application.run_polling()

if __name__ == '__main__':
    main()
