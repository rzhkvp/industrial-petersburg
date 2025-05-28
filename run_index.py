import webbrowser
import os
from pathlib import Path


script_dir = Path(__file__).parent
index_path = script_dir / 'index.html'


if not index_path.exists():
    print(f"Файл {index_path} не найден.")
else:
    
    index_uri = index_path.resolve().as_uri()

    
    webbrowser.open_new_tab(index_uri)
