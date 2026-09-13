def filter_by_state(list_of_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список банковских операций и фильтрует их по статусу"""
    final_operations_list = []

    for operation in list_of_operations:
        if operation["state"] == state:
            final_operations_list.append(operation)

    return final_operations_list


def sort_by_date(list_of_operations: list[dict], reverse: bool = True) -> list[dict]:
    """Функция, которая сортирует список операций по дате операции"""
    final_sorted_list = sorted(list_of_operations, key=lambda operation: operation["date"], reverse=reverse)

    return final_sorted_list
