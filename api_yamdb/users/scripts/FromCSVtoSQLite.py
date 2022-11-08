import csv
from pathlib import Path

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError
from reviews.models import Category, Genre, Title

DIR_PATH = Path.cwd()

MODELS_DICT = {'category': Category,
               'genre': Genre,
               'titles': Title,
               }


class Command(BaseCommand):
    help = u'Импорт из csv файла в базу данных'

    def add_arguments(self, parser):
        parser.add_argument(
            'filename',
            type=str,
            help=u'Имя csv файла')

    def handle(self, *args, **kwargs):
        file_key = kwargs['filename']
        file = file_key + '.csv'  # Генерация имени файла
        full_path = Path(DIR_PATH, 'static', 'data', file)  # получение пути к файлу
        model_name = MODELS_DICT.get(file_key)  # извлечение имени модели
        if model_name is None:  # проверка на случай отсутствия ключа
            raise KeyError('Проверьте корректность имени файла!')

        with open(full_path, encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")  # читаем csv
            count = 0
            for row in file_reader:  # построчно
                if count == 0:
                    first_row = row  # первая строка - название полей, пригодится, храним
                else:
                    keyargs = dict(zip(first_row, row))  # создаем словарь аргументы модели - значения
                    try:
                        model_name.objects.create(**keyargs)  # создаем объект в бд
                    except TypeError:
                        raise TypeError(
                            'Поля файла не соответствуют полям таблицы!'
                        )
                    except IntegrityError:
                        raise IntegrityError(
                            'Поля файла не соответствуют полям таблицы!'
                        )
                count += 1
