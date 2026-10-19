import copy
import os
import shlex

import prompt

from primitive_db.core import create_table, drop_table
from primitive_db.utils import load_metadata, save_metadata

METADATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 
                                                       'db_meta.json')

HELP_TEXT = """***Процесс работы с таблицей***
Функции:
<command> create_table <имя_таблицы> <столбец1:тип> <столбец2:тип> .. - создать таблицу
<command> list_tables - показать список всех таблиц
<command> drop_table <имя_таблицы> - удалить таблицу
<command> exit - выход из программы
<command> help - справочная информация"""


def run():
    print(HELP_TEXT)

    while True:
        metadata = load_metadata(METADATA_FILE)

        user_input = prompt.string('\n>>>Введите команду: ').strip()

        if not user_input:
            continue

        try:
            args = shlex.split(user_input)
        except ValueError:
            print(f'Некорректное значение: {user_input}. Попробуйте снова.')
            continue

        if not args:
            continue

        command = args[0].lower()
        command_args = args[1:]

        if command == 'create_table':
            if len(command_args) < 2:
                print(f'Некорректное значение: {user_input}. Попробуйте снова.')
                continue

            table_name = command_args[0]
            cols = command_args[1:]

            old_v = copy.deepcopy(metadata)
            new_v = create_table(metadata, table_name, cols)

            if new_v != old_v:
                save_metadata(METADATA_FILE, new_v)

        elif command == 'list_tables':
            if metadata:
                for table in metadata:
                    print(f'- {table}')
            else:
                print('Список таблиц пуст.')

        elif command == 'drop_table':
            if len(command_args) != 1:
                print(f'Некорректное значение: {user_input}. Попробуйте снова.')
                continue

            table_name = command_args[0]

            old_v = copy.deepcopy(metadata)
            new_v = drop_table(metadata, table_name)

            if new_v != old_v:
                save_metadata(METADATA_FILE, new_v)

        elif command == 'help':
            print(HELP_TEXT)

        elif command == 'exit':
            print('Выход из программы.')
            break

        else:
            print(f'Функции {args[0]} нет. Попробуйте снова.')