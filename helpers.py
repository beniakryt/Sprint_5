import random
import string

def generate_unique_email():
    # Генерируем случайный номер для уникальности
    random_number = random.randint(1000, 9999)
    # Формируем email
    email = f"yurii14{random_number}@yandex.ru"
    return email
