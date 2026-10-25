from progress_analytics import ProgressAnalytics

def run_tests():
    analytics = ProgressAnalytics()
    
    # --- НАБОР ТЕСТОВЫХ ДАННЫХ (Имитация истории тренировок) ---
    mock_history = [
        {'exercise': 'Приседания', 'weight': 100},
        {'exercise': 'Жим лежа', 'weight': 60},
        {'exercise': 'Приседания', 'weight': 110}, # Рекорд здесь
        {'exercise': 'Жим лежа', 'weight': 50},
    ]

    print("--- Тест 1: Обычный поиск рекорда (Happy Path) ---")
    res1 = analytics.find_personal_record(mock_history, 'Приседания')
    print(f"Ожидалось: 110. Получено: {res1}")
    assert res1 == 110

    print("\n--- Тест 2: Упражнения нет в истории (Edge Case) ---")
    res2 = analytics.find_personal_record(mock_history, 'Становая тяга')
    print(f"Ожидалось: 'Упражнение не найдено'. Получено: {res2}")
    # Здесь мы не используем assert, а просто смотрим на вывод

    print("\n--- Тест 3: Пустая история (Negative Test) ---")
    res3 = analytics.find_personal_record([], 'Приседания')
    print(f"Ожидалось: 0.0. Получено: {res3}")
    assert res3 == 0.0

run_tests()
