from telegram import ForceReply, Update
from telegram.ext import ContextTypes

# from main import application
from utils.generate_messages import generate_stop_message, generate_start_message, generate_help_message, \
    generate_news_message, generate_joke_message, generate_weather_message
from utils.get_weather import get_weather


async def start_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text, keyboard = await generate_start_message(update.effective_user.first_name)
    await update.message.reply_text(text=text, reply_markup=keyboard)


async def help_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = await generate_help_message()
    await update.message.reply_text(text=text)


async def echo_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_split = update.message.text.split(" ")
    if len(message_split) == 2:
        await update.message.reply_text(message_split[1])
    else:
        await update.message.reply_text("Вы допустили ошибку! Возможно, вы не указали сообщение.\nПример: /echo Привет")


async def weather_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_split = update.message.text.split(" ")
    if len(message_split) == 2:
        text = generate_weather_message(message_split[1])
        await update.message.reply_text(text=text)
    else:
        await update.message.reply_text("Вы допустили ошибку! Возможно, вы не указали сообщение.\nПример: /weather Омск")



async def news_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    news_list = await generate_news_message()
    if len(news_list) != 0:
        for news in news_list:
            if news['photo_link'] is not None:
                await update.message.reply_photo(photo=news['photo_link'], caption=news['text'], parse_mode="Markdown")
            else:
                await update.message.reply_text(text=news['text'], parse_mode="Markdown")
    else:
        await update.message.reply_text("Список новостей пуст. Попробуйте ещё раз!")


async def joke_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    joke_text = await generate_joke_message()
    await update.message.reply_text(text=joke_text)


async def stop_message_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await generate_stop_message(update.effective_user.first_name)
    await update.message.reply_text(text=message)
    await context.application.stop()

