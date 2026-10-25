class ProgressAnalytics:
    def __init__(self):
        # Заглушка (Stub) для связи с базой данных, если понадобится
        self.storage_service = "Active"

    def find_personal_record(self, workout_history, exercise_name):
        # 1. Проверка на пустую историю
        if not workout_history:
            return 0.0

        max_weight = 0.0
        found = False

        # 2. Проход по всем тренировкам и поиск нужного упражнения
        for workout in workout_history:
            # Предполагаем, что workout - это словарь: {'exercise': 'Жим', 'weight': 50}
            if workout.get('exercise') == exercise_name:
                found = True
                current_weight = workout.get('weight', 0)
                if current_weight > max_weight:
                    max_weight = current_weight
        
        # 3. Обработка случая, если упражнение не найдено
        if not found:
            return "Упражнение не найдено"
            
        return max_weight
