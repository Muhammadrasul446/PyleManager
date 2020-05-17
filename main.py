import os
import time
from pathlib import Path
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Handler(FileSystemEventHandler):
    def on_any_event(self, event):
        for filename in os.listdir(source):
            # Проверяем расширенеи файла
            extension = filename.split(".")[-1]
            # Если этот тип известен то
            if len(extension) > 1 and (extension.lower() in target):
                file = source + r"\\" + filename
                new_path = str(target.get(extension.lower())) + filename
                print(new_path)
                try:
                    os.rename(file, new_path)
                except Exception:
                    pass


home = str(Path.home())
# Источник файлов
source = home + r'\Downloads'

# Папка куда перемещать будем
pictures = home + r'\Pictures\\'
video = home + r'\Video\\'
docs = home + r'\Documents\\'
audio = home + r'\Music\\'

target = {
    # Изображения
    'jpg': pictures,
    'jpeg': pictures,
    'png': pictures,
    'tif': pictures,
    'tiff': pictures,
    'gif': pictures,
    'svg': pictures,
    'bmp': pictures,
    'dib': pictures,

    # Видео
    'avi': video,
    'flv': video,
    'm4v': video,
    'mkv': video,
    'mov': video,
    'mp4': video,
    'mpeg': video,
    'mpg': video,
    'swf': video,
    'vcd': video,
    'vob': video,
    'webm': video,
    'wmv': video,

    # Документы
    'txt': docs,
    'doc': docs,
    'docx': docs,
    'epub': docs,
    'ibooks': docs,
    'indd': docs,
    'key': docs,
    'mobi': docs,
    'pages': docs,
    'pdf': docs,
    'pps': docs,
    'ppt': docs,
    'pptx': docs,
    'rtf': docs,
    'xlr': docs,
    'xls': docs,
    'xlsx': docs,
    'docm': docs,
    'dotm': docs,
    'fb2': docs,
    'kml': docs,
    'mdb': docs,
    'mso': docs,
    'ods': docs,
    'oxps': docs,
    'pot': docs,
    'potm': docs,
    'potx': docs,
    'pptm': docs,
    'ps': docs,
    'sldm': docs,
    'snb': docs,
    'xlsm': docs,
    'xlt': docs,
    'dot': docs,
    'dotx': docs,
    'odt': docs,
    'ppsm': docs,
    'ppsx': docs,
    'pub': docs,
    'wpd': docs,
    'wps': docs,
    'xlsb': docs,
    'xltm': docs,
    'xltx': docs,
    'xps': docs,

    # Архивы
    '7z': docs,
    'ace': docs,
    'arj': docs,
    'bin': docs,
    'cab': docs,
    'cbr': docs,
    'deb': docs,
    # 'exe': docs,
    'gz': docs,
    'gzip': docs,
    'jar': docs,
    'pak': docs,
    'pkg': docs,
    'rar': docs,
    'rpm': docs,
    'sh': docs,
    'sis': docs,
    'sisx': docs,
    'sit': docs,
    'sitx': docs,
    'tar': docs,
    'tar-gz': docs,
    'tgz': docs,
    'xar': docs,
    'zip': docs,
    'zipx': docs,

    # Аудио
    'ac3': audio,
    'aif': audio,
    'aiff': audio,
    'amr': audio,
    'aob': audio,
    'ape': audio,
    'asf': audio,
    'aud': audio,
    'cdr': audio,
    'flac': audio,
    'gpx': audio,
    'ics': audio,
    'iff': audio,
    'm3u': audio,
    'm3u8': audio,
    'm4a': audio,
    'm4b': audio,
    'm4p': audio,
    'm4r': audio,
    'mid': audio,
    'midi': audio,
    'mod': audio,
    'mp3': audio,
    'mpa': audio,
    'mts': audio,
    'nkc': audio,
    'ogg': audio,
    'ra': audio,
    'ram': audio,
    'sib': audio,
    'wav': audio,
    'wave': audio,
    'wma': audio,
    'xsb': audio,
    'xwb': audio,
}

# Запуск всего на отслеживание
handle = Handler()
observer = Observer()
observer.schedule(handle, source, recursive=True)
observer.start()

# Программа будет срабатывать каждые 240 милисекунд
try:
    while True:
        time.sleep(1000)
except KeyboardInterrupt:
    observer.stop()

observer.join()
