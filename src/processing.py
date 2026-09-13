def filter_by_state(list_of_operations: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция, которая принимает список банковских операций и фильтрует их по статусу"""
    final_operations_list = []

    for operation in list_of_operations:
        if operation["state"] == state:
            final_operations_list.append(operation)

    return final_operations_list
