import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from bot.file_processor import process_file

class FileHandler(FileSystemEventHandler):
    """Clase que maneja eventos en la carpeta"""

    def __init__(self, folder_path):
        self.folder_path = folder_path

    def on_created(self, event):
        """Ejecuta cuando se detecta un archivo nuevo"""
        if not event.is_directory:
            print(f"Nuevo archivo detectado: {event.src_path}")
            process_file(event.src_path)  # Procesar archivo

def start_monitoring(folder_path):
    """Inicia el monitoreo de la carpeta especificada"""
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    event_handler = FileHandler(folder_path)
    observer = Observer()
    observer.schedule(event_handler, folder_path, recursive=False)
    observer.start()

    print(f"Monitoreando la carpeta: {folder_path}")

    try:
        while True:
            time.sleep(1)  # Mantener la ejecución activa
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
