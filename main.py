from settings import bot
from tg_commands import get_started, get_help, make_a_request, wrong_command


def register_handlers() -> None:
    """
    Функция-обработчик всех команд.

    :return: None
    """
    bot.register_message_handler(get_started)
    bot.register_message_handler(get_help)
    bot.register_message_handler(make_a_request)
    bot.register_message_handler(wrong_command)


if __name__ == '__main__':
    bot.polling(none_stop=True)
    register_handlers()
