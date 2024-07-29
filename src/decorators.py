def log(filename=None):
    """Декоратор, который логирует вызовы и результаты функции.
    Если указан параметр filename, логи записываются в файл.
    Если параметр filename не указан, логи выводятся в консоль."""

    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                logg_message = (
                    f"{func.__name__} ошибка: {e}. Входные данные: {args}, {kwargs}"
                )
                raise
            else:
                logg_message = f"{func.__name__} ok"
            if filename:
                with open(filename, "a") as file:
                    file.write(logg_message + "\n")
            else:
                print(logg_message)
            return result

        return wrapper

    return my_decorator
