from telebot.types import Message
from settings import bot
from services import best_change_request


@bot.message_handler(commands=['start'])
def get_started(message: Message) -> None:
    """
    Функция, отправляющая сообщение при активации команды /start.

    :param message: Сообщение от пользователя
    :return: None
    """
    bot.send_message(message.from_user.id,
                     "Привет✌ \nИщешь лучший курс крипты?💵🏧\n"
                     "Ты по адресу👌\n"
                     "Для получения информации о командах нажми /help")


@bot.message_handler(commands=['help'])
def get_help(message: Message) -> None:
    """
    Функция для получения информации о командах.

    :param message: Сообщение от пользователя
    :return: None
    """
    bot.send_message(message.from_user.id,
                     "Сведения о командах\n\n"
                     "/start - Общая информация\n"
                     "/request — Узнать разницу\n"
                     "/help — Доступные команды\n")


@bot.message_handler(commands=['request'])
def make_a_request(message: Message) -> None:
    """
    Функция для получения ID обменника.

    :param message: Сообщение от пользователя
    :return: None
    """
    msg = bot.send_message(message.from_user.id, "Введите ID обменника")

    bot.register_next_step_handler(msg, get_results)


def get_results(message: Message) -> Message or None:
    """
    Функция для получения разница между лидером и введенным ID обменника.

    :param message: Сообщение от пользователя
    :return: None
    """
    ...

    result = best_change_request(message.text)
    if not result:
        return bot.send_message(message.chat.id, "Данного ID нет на сайте.\nПопробуйте снова.")

    bot.send_message(message.chat.id, result)


@bot.message_handler(func=lambda message: True)
def wrong_command(message: Message) -> None:
    """
    Функция для обработки всех нерелевантных сообщений.

    :param message: Сообщение от пользователя
    :return: None
    """
    bot.send_message(message.chat.id, "Я Вас не понимаю.\nВведите команду: /help")
