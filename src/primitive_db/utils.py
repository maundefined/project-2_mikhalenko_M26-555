import json

def load_metadata(filepath):
    """
    Загружает метаданные из JSON-файла.
    Возвращает словарь с метаданными или пустой словарь {},
             если файл не существует или повреждён.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        return {}

def save_metadata(filepath, data):
    """
    Сохраняет метаданные в JSON-файл.
    """
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)