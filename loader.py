from telegram.ext import CommandHandler, Application, CallbackQueryHandler

from modules.commands.callback_commands import start_callback_command_handler
from modules.commands.message_commands import start_message_command_handler, help_message_command_handler, \
    echo_message_command_handler, weather_message_command_handler, news_message_command_handler, \
    joke_message_command_handler, stop_message_command_handler


def add_handlers(application: Application):
    application.add_handler(CommandHandler("start", start_message_command_handler))
    application.add_handler(CommandHandler("help", help_message_command_handler))
    application.add_handler(CommandHandler("echo", echo_message_command_handler))
    application.add_handler(CommandHandler("weather", weather_message_command_handler))
    application.add_handler(CommandHandler("news", news_message_command_handler))
    application.add_handler(CommandHandler("joke", joke_message_command_handler))
    application.add_handler(CommandHandler("stop", stop_message_command_handler))
    application.add_handler(CallbackQueryHandler(start_callback_command_handler))

# application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
