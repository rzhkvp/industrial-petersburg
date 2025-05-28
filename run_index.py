import webbrowser
import os
from pathlib import Path

# Определяем путь к index.html относительно местоположения этого скрипта
script_dir = Path(__file__).parent
index_path = script_dir / 'index.html'

# Проверяем, существует ли файл index.html
if not index_path.exists():
    print(f"Файл {index_path} не найден. Убедитесь, что он находится в той же папке, что и скрипт.")
else:
    # Преобразуем путь к URI, чтобы браузер мог его открыть
    index_uri = index_path.resolve().as_uri()

    # Открываем в браузере по умолчанию
    webbrowser.open_new_tab(index_uri)
