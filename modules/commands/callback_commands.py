from telegram import Update
from telegram.ext import ContextTypes

from utils.generate_messages import generate_help_message, generate_news_message, generate_stop_message, \
    generate_joke_message


async def start_callback_command_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.callback_query.answer()
    query = update.callback_query
    if query.data == "see_list_commands":
        text = await generate_help_message()
        await update.callback_query.message.reply_text(text=text)
    elif query.data == "echo_answer":
        await update.callback_query.message.reply_text(text="Используйте /echo <text>\n\n<text> - переданный текст")
    elif query.data == "see_weather":
        await update.callback_query.message.reply_text(text="Используйте /weather <город>\n\n<город> - город, погоду "
                                                            "которого вы хотели бы узнать")
    elif query.data == "last_news":
        news_list = await generate_news_message()
        if len(news_list) != 0:
            for news in news_list:
                if news['photo_link'] is not None:
                    await update.callback_query.message.reply_photo(photo=news['photo_link'], caption=news['text'],
                                                                    parse_mode="Markdown")
                else:
                    await update.callback_query.message.reply_text(text=news['text'], parse_mode="Markdown")
        else:
            await update.callback_query.message.reply_text("Список новостей пуст. Попробуйте ещё раз!")
    elif query.data == "random_joke":
        joke_text = await generate_joke_message()
        await update.callback_query.message.reply_text(text=joke_text)
    elif query.data == "stop_bot":
        message = await generate_stop_message(update.effective_user.first_name)
        await update.callback_query.message.reply_text(text=message)
        await context.application.stop()
