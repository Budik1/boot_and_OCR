import inspect

def get_function_details():
    # Получение информации о текущем фрейме
    current_frame = inspect.currentframe()

    # Информация о текущей функции
    current_func_name = current_frame.f_code.co_name

    # Получение стека вызовов
    call_stack = inspect.stack()

    # Имя вызывающей функции (если есть)
    caller_name = call_stack[1].function if len(call_stack) > 1 else "None"

    # Имя модуля текущей функции
    module_name = inspect.getmodule(current_frame).__name__

    return {
    "function_name": current_func_name,
    "caller_name": caller_name,
    "module_name": module_name,
    "file_name": call_stack[0].filename,
    "line_number": call_stack[0].lineno
    }

def caller_function():
    details = get_function_details()
    print(f"Функция: {details['function_name']}")
    print(f"Вызвана из: {details['caller_name']}")
    print(f"Модуль: {details['module_name']}")
    print(f"Файл: {details['file_name']}")
    print(f"Строка: {details['line_number']}")

# caller_function()

