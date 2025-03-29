import copy
import functools
from datetime import datetime, timedelta

from flask import request


class Tables:
    PRODUCT_CATEGORY = 0
    PRODUCT = 1
    SALE = 2


def api_decorator(tables: list[int]):
    """Декоратор для кэширования запросов к API

    :param tables: Таблицы используемые эндпоинтом
    Для GET запросов - таблицы из которых берутся данные
    Для POST/PUT/DELETE - таблицы в которых изменяются данные
    """

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            full_url = f'{request.method} {request.url}'

            if cached_data := cache.get(full_url):
                return cached_data, 200

            data, code = func(*args, **kwargs)

            if code == 200:
                if request.method == 'GET':
                    cache.set(full_url, tables, data)
                else:
                    # данные в бд были изменены, инвалидировать кэш связанный с таблицами tables
                    for t in tables:
                        cache.invalidate(t)

            return data, code
        return wrapper
    return decorator


class Cache():
    def __init__(self):
        self.cache = {}

    def get(self, url: str) -> dict:
        """Отдаёт здачение из кэша если оно не устарело"""
        ch = self.cache.get(url)
        if ch and ch['time'] + timedelta(minutes=5) > datetime.now():
            data = copy.deepcopy(ch['data'])
            data.update({'cached': ch['time'].ctime()})  # отметка о том что ответ был получени из кэша
            return data

    def set(self, url: str, tables: list[int], data: dict):
        """Записывает в кэш значение и из каких таблиц оно было получено"""
        self.cache.update({url: {'tables': tables, 'time': datetime.now(), 'data': data}})

    def invalidate(self, table: int):
        """Удаляет все записи в кэше связанные с таблицей table"""
        to_delete = [url for url, val in self.cache.items() if table in val['tables']]
        for url in to_delete:
            self.cache.pop(url)


cache = Cache()
