def all_variants(text):
    n = len(text)
    # Генерируем все возможные подпоследовательности
    for start in range(n):
        for end in range(start + 1, n + 1):
            yield text[start:end]  # Возвращаем подпоследовательность

# Пример использования функции
a = all_variants("abc")
for i in a:
    print(i)