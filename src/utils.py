import json


def get_operations_from_json(file_path):
    """
    Функция, которая принимает путь к файлу, читает его
    и возвращает список словарей с данными о финансовых операциях.
    """
    try:
        with open(file_path, encoding='utf-8') as f: #Открываем файл
            operations = json.load(f) #Читаем файл
    except (json.JSONDecodeError, FileNotFoundError): #Обрабатываем ошибки - пустой файл или файл не найден
        return []
    #Если файл не пуст и найден, проверяем два условия - operations это список, а внутри него словари
    if isinstance(operations, list) and all(isinstance(operation, dict) for operation in operations):
        return operations #Возвращаем, если оба условия соблюдены
    else:
        return [] #Возвращаем пустой список, если хотя бы одно условие не истина
