import datetime


def date_utc_now():
    now = datetime.datetime.now(datetime.timezone.utc)
    date_utc = (now.strftime('%Y-%m-%d'))  # год-месяц-день
    return date_utc


def time_now():
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    time_now_ = (now.strftime('%H:%M:%S'))
    return time_now_


def date_time_now():
    """

    :return:
    """
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    date_time_now_ = (now.strftime('%Y-%m-%d %H:%M:%S'))
    date = (now.strftime('%Y-%m-%d'))
    return date_time_now_, date


def date_now():
    """
    Возвращает дату в формате 'Год-месяц-день'
    :return: str
    """
    now = datetime.datetime.now()
    date = (now.strftime('%Y-%m-%d'))
    return date


def date_now_lst():
    """
    Возвращает дату в формате ['Год', 'месяц', 'день']
    :return: list
    """
    now = datetime.datetime.now()
    date = (now.strftime('%Y-%m-%d'))
    date_lst = date.split('-')
    return date_lst


def minutes_now():
    now = datetime.datetime.now()
    minutes_now_ = (now.strftime('%M'))
    return minutes_now_


def date_and_time_in_name_file():
    """
    '%Y-%m-%d %H-%M-%S'
    :return: str
    """
    now = datetime.datetime.now()
    date_time_now_f = (now.strftime('%Y-%m-%d %H-%M-%S'))
    return date_time_now_f
