from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.helpers import escape_markdown


from utils.get_joke import get_joke
from utils.get_news import get_news
from utils.get_weather import get_weather


async def generate_start_message(first_name: str) -> tuple[str, InlineKeyboardMarkup]:
    """
    Generating the start message
    :param first_name: first name user
    :return: message text | str
    """
    text = f"""
🖐 Здравствуйте, {first_name}!

📋 Выберите нужный вам пункт из меню.
"""
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="👁 Посмотреть доступные команды", callback_data="see_list_commands")
        ],
        [
            InlineKeyboardButton(text="🤖 Эхо-ответ", callback_data="echo_answer"),
            InlineKeyboardButton(text="☁ Текущая погода", callback_data="see_weather")
        ],
        [
            InlineKeyboardButton(text="📰 Последние новости", callback_data="last_news")
        ],
        [
            InlineKeyboardButton(text="🗣 Случайная шутка", callback_data="random_joke")
        ],
        [
            InlineKeyboardButton(text="⚠ Остановка работы бота", callback_data="stop_bot")
        ]
    ])
    return text, keyboard


async def generate_help_message():
    """
    Generating a message with commands
    :return: message text | str
    """
    text = """
📋 Список доступных команд:
🔸 /start - вывод меню
🔸 /echo <текст> - эхо-ответ с переданным текстом
🔸 /weather <город> - вывод текущей погоды в указанном городе
🔸 /news - вывод последних новостей
🔸 /joke - вывод случайной шутки
🔸 /stop - остановка работы бота    
"""
    return text


async def generate_news_message() -> list:
    """
    Generating a message about the latest news
    :return: list
    """
    message_list = []
    news_list = get_news()
    for news in news_list:
        message_list.append(
            {
                "text": f"""
*{escape_markdown(news['title']) if news.get('title') is not None else " "}*

{escape_markdown(news['description']) if news.get('description') is not None else " "}

*Автор:* {escape_markdown(news['author']) if news.get('author') is not None else " "}
*Дата публикации:* {escape_markdown(news['pubDate']) if news.get('pubDate') is not None else " "}

[Ссылка на публикацию]({news['link'] if news.get('link') is not None else " "})         
""",
                "photo_link": news['photo_url']})
    return message_list


async def generate_joke_message() -> str:
    """
    Generating a message with a random joke for the user
    :return: str
    """
    text_json = get_joke()
    if text_json is not None:
        if len(text_json) != 0:
            if text_json[0].get('content') is not None:
                return text_json[0].get('content')
            else:
                return "Произошла ошибка. Попробуйте ещё раз через некоторое время."
        else:
            return "Произошла ошибка. Попробуйте ещё раз через некоторое время."
    else:
        return "Произошла ошибка. Попробуйте ещё раз через некоторое время."


async def generate_stop_message(first_name: str) -> str:
    """
    Generating a message saying goodbye to the user
    :param first_name: first name user
    :return:
    """
    text = f"Приятно было с вами пообщаться, {first_name}! До свидания! 👋"
    return text


def generate_weather_message(place: str) -> str:
    """
    Generating a message with the current weather for the user
    :param place:
    :return:
    """
    temp = get_weather(place)
    if temp is not None:
        if temp.get("temp") is not None:
            return f"В городе {place} сейчас {temp.get('temp')}°C"
        elif temp.get("error") is not None:
            return temp.get("error")
        else:
            return "Произошла ошибка. Попробуйте ещё раз через некоторое время."
    else:
        return "Произошла ошибка. Попробуйте ещё раз через некоторое время."
