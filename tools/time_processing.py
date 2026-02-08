import datetime


def date_utc_now() -> str:
    """

    :return: '%Y-%m-%d'
    """
    now = datetime.datetime.now(datetime.timezone.utc)
    date_utc = (now.strftime('%Y-%m-%d'))  # год-месяц-день
    return date_utc


def time_now() -> str:
    now = datetime.datetime.now()
    # '%Y-%m-%d_%H:%M:%S' '%Y-%m-%d %H°%M\'\'%S\''
    time_now_ = (now.strftime('%H:%M:%S'))
    return time_now_


def date_now() -> str:
    """
    Возвращает дату в формате 'Год-месяц-день'
    :return: str
    """
    now = datetime.datetime.now()
    date = (now.strftime('%Y-%m-%d'))
    return date


def date_now_lst() -> list[str]:
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


def dif_days(*, date_old, date_today):
    """
    Вычисляет разницу между двумя датами в днях.
    :param date_old: Прошедшая дата в формате "2025-11-29"
    :param date_today: Сегодняшняя дата в формате "2025-11-29"
    :return: Количество в днях
    """
    # Если дата в формате "29-11-2025" нужно привести в правильный формат
    lst_date_old = date_old.split(sep='-')
    if len(lst_date_old[0]) == 4:
        list_date_old = lst_date_old
    else:
        list_date_old = lst_date_old[::-1]
    list_date_today = date_today.split(sep='-')
    par_year = 0
    par_month = 1
    par_day = 2
    d_old = datetime.date(int(list_date_old[par_year]),
                          int(list_date_old[par_month]),
                          int(list_date_old[par_day]))
    d_today = datetime.date(int(list_date_today[par_year]),
                            int(list_date_today[par_month]),
                            int(list_date_today[par_day]))
    dif = d_today - d_old
    return dif.days


def get_rest_tim(*, h_max):
    t_now = time_now()
    h, m, s = t_now.split(':')
    t_work = 8
    rest_t = h_max - int(h)
    if rest_t > 8:
        t_work = 8
    elif 8 >= rest_t > 5:
        t_work = 5
    elif 5 >= rest_t > 2:
        t_work = 2
    elif 2 >= rest_t > 1:
        t_work = 1
    return t_work
