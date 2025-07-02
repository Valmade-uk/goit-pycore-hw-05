def caching_fibonacci():
    # Створити порожній словник cache
    cache = {}

    # Внутрішня функція для обчислення чисел Фібоначчі
    def fibonacci(n):
        # Якщо n <= 0, повернути 0
        if n <= 0:
            return 0

        # Якщо n == 1, повернути 1
        if n == 1:
            return 1

        # Якщо n у cache, повернути cache[n]
        if n in cache:
            return cache[n]

        # Обчислення з рекурсією і кешуванням
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)

        # Повернути результат з кешу
        return cache[n]

    # Повернути функцію fibonacci
    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610