from src.widget import get_data, mask_account_card

def log(filename=None):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                logg_message = f"{func.__name__} ошибка: {e}. Входные данные: {args}, {kwargs}"
            else:
                logg_message = f"{func.__name__} ok"
            if filename:
                with open(filename) as file:
                    file.write(logg_message)
            else:
                print(logg_message)
        return wrapper
    return my_decorator
