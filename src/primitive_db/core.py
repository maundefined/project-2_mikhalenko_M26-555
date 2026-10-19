def create_table(metadata, table_name, columns):
    """
    Создаёт новую таблицу в метаданных.
    При ошибке возвращает metadata без изменений.
    """
    if table_name in metadata:
        print(f'Ошибка: Таблица "{table_name}" уже существует.')
        return metadata

    ALLOWED_TYPES = {"int", "str", "bool"}

    parsed_cols = []
    for col in columns:
        if not isinstance(col, str) or ":" not in col:
            print(f'Ошибка: Некорректный формат столбца "{col}". Ожидается "имя:тип".')
            return metadata

        name, col_type = col.split(":", 1)
        name = name.strip()
        col_type = col_type.strip()

        if not name:
            print(f'Ошибка: Пустое имя столбца в "{col}".')
            return metadata

        if col_type not in ALLOWED_TYPES:
            print(f'Ошибка: Недопустимый тип данных "{col_type}" для столбца "{name}". '
                  f'Разрешены только: int, str, bool.')
            return metadata

        parsed_cols.append({"name": name, "type": col_type})

    id_col = {"name": "ID", "type": "int"}

    if any(col['name'] == 'ID' for col in parsed_cols):
        print('Ошибка: Столбец "ID" добавляется автоматически, не указывайте его вручную.')
        return metadata

    all_cols = [id_col] + parsed_cols
    metadata[table_name] = all_cols

    cols_list = ", ".join(f'{col["name"]}:{col["type"]}' for col in all_cols)
    print(f'Таблица "{table_name}" успешно создана со столбцами: {cols_list}')

    return metadata

def drop_table(metadata, table_name):
    """
    Удаляет таблицу из метаданных.
    """

    if table_name not in metadata:
        print(f'Ошибка: Таблица "{table_name}" не существует.')
        return metadata

    del metadata[table_name]
    print(f'Таблица "{table_name}" успешно удалена.')

    return metadata