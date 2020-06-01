import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Считываем настройки путей для мониторинга и перемещения файлов
settings = {}
with open('path_settings.txt', 'r') as file:
    for line in file.readlines():
        line = str(line.replace('\n', '')).split('|')
        settings[line[0]] = line[1]
    print(settings)

# Считываем настройки типов и пути сохранения файлов
target = {}
with open('known_file_types.txt', 'r') as file:
    for line in file.readlines():
        line = str(line.replace('\n', '')).split(':')
        target[line[0]] = line[1]
    print(target)


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(settings.get('source')):
            # Проверяем расширенеи файла
            extension = filename.split(".")[-1]
            # Если этот тип известен то
            if len(extension) > 1 and (extension.lower() in target):
                file = str(settings.get('source')) + filename
                new_path = settings.get(target.get(extension.lower())) + filename
                try:
                    os.rename(file, new_path)
                except Exception:
                    pass


# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, settings.get('source'), recursive=True)
observer.start()

# Программа будет срабатывать каждую секунду
try:
    while True:
        time.sleep(1000)
except KeyboardInterrupt:
    observer.stop()
except:
    print("WTF are you doing?? Check whether everything is correct and then re-run!!!")

observer.join()
