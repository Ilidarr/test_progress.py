# Lab3
| ID | Модуль и метод | Входные данные | Ожидаемый результат | Фактический результат |
|----|----------------|----------------|---------------------|-----------------------|
| BUG-01 | ProgressAnalytics.find_personal_record | workout_history = None (вместо списка)|Сообщение об ошибке или возврат 0.0 | Программа падает с TypeError: 'NoneType' object is not iterable| 
| BUG-02 | ProgressAnalytics.find_personal_record| Вес упражнения указан строкой: {'exercise': 'Жим', 'weight': '60'}| Игнорирование или конвертация | Программа падает с TypeError при сравнении строки и числа |  

 [Ссылка на Канбан](https://github.com/users/Ilidarr/projects/1/views/1?template_dialog_tab=featured&layout_template=board)
