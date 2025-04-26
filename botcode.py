import logging
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from telegram.ext import Application, MessageHandler, CommandHandler, ContextTypes, filters

logging.basicConfig( 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

data = pd.read_json('../dataset.json.gz')  
inputs = data['input']
outputs = data['output']

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(inputs)

def get_best_response(user_message: str) -> str:
    user_vec = vectorizer.transform([user_message])
    similarities = cosine_similarity(user_vec, X)
    idx = similarities.argmax()
    return outputs.iloc[idx]

async def start(update, context):
    """Обработчик команды /start"""
    welcome_text = (
        "Привет! Я умный бот на основе датасета.\n"
        "Напиши что-нибудь, и я постараюсь ответить."
    )
    await update.message.reply_text(welcome_text)

async def handle_message(update, context):
    """Обрабатываем любое текстовое сообщение"""
    user_text = update.message.text
    reply = get_best_response(user_text)
    await update.message.reply_text(reply)g

async def error_handler(update, context):
    """Логируем ошибки"""
    logger.error(msg="Исключение при обработке сообщения:", exc_info=context.error)

async def main():
    TOKEN = 'telegram API'

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error_handler)

    await application.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
