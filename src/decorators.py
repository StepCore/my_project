def log(filename=None):
    """Декоратор, который проверяет правильность работы функции"""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logg_message = (
                    f"{func.__name__} ошибка: {e}. Входные данные: {args}, {kwargs}"
                )
            else:
                logg_message = f"{func.__name__} ok"
            if filename:
                with open(filename, "w") as file:
                    file.write(logg_message)
            else:
                print(logg_message)

        return wrapper

    return my_decorator
