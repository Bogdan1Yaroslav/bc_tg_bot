import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def find_exchanger_name(some_tag: Tag) -> str:
    """
    Функция нахождения наименование обменника на сайте.

    :param some_tag: Тэг HTML разметки
    :return: Наименование обменника (str)
    """
    return some_tag.find("td", class_="bj").find("div", class_="ca").text.strip()


def find_exchange_rate(some_tag: Tag) -> float:
    """
    Функция нахождения курса обмена криптовалюты.

    :param some_tag: Тэг HTML разметки
    :return: Курс обменника (float)
    """
    data = some_tag.find_all("td", class_="bi")[1]
    data.small.decompose()

    exchange_rate = data.text.replace(" ", "")

    return float(exchange_rate)


def best_change_request(exchanger_id: str) -> str or None:
    """
    Функция выполняет GET запрос на сайт BC,
    парсит данные, находит запрашиваемый ID обменника,
    вычисляет разницу между лучшим курсом и курсом запрашиваемого обменника.

    :param exchanger_id: ID обменника
    :return: Результат в виде строки либо None в случае, если ID запрашиваемого обменника отсутствует на сайте.
    """
    url = "https://www.bestchange.ru/bitcoin-to-tether-trc20.html"
    my_request = requests.get(url).text

    soup = BeautifulSoup(my_request, "html.parser")
    main_table = soup.find("table", id="content_table").find("tbody").find_all("tr")

    exchangers_dict = dict()

    for elem in main_table:
        try:
            name, rate = find_exchanger_name(elem), find_exchange_rate(elem)
            exchangers_dict[name] = rate
        except AttributeError as err:
            ...

    if exchanger_id in exchangers_dict:
        requested_value = exchangers_dict[exchanger_id]

        max_value_exchanger = max(exchangers_dict, key=exchangers_dict.get)
        max_value = exchangers_dict[max_value_exchanger]

        result = round(max_value - requested_value, 4)

        return f"Курс {exchanger_id}: {requested_value}\n" \
               f"Курс лидера {max_value_exchanger}: {max_value}\n" \
               f"Разница между курсами: {result}"

    return None
