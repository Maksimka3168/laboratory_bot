from telegram.ext import CommandHandler, Application

from config import TOKEN
from loader import add_handlers

application = Application.builder().token('5744022716:AAFGQB5o3zUHqn_AapWgVNrgQf2mClJd3ps').build()
add_handlers(application)

if __name__ == "__main__":
    application.run_polling()

