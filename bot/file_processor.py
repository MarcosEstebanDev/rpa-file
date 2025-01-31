import os
import shutil
from datetime import datetime

# Carpeta donde se moverán los archivos procesados
PROCESSED_FOLDER = "processed"

def process_file(file_path):
    """Procesa el archivo moviéndolo a la carpeta correspondiente"""
    if not os.path.exists(PROCESSED_FOLDER):
        os.makedirs(PROCESSED_FOLDER)

    file_name, file_extension = os.path.splitext(os.path.basename(file_path))
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    new_name = f"{file_name}_{timestamp}{file_extension}"

    destination_folder = os.path.join(PROCESSED_FOLDER, file_extension[1:].upper())

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    new_path = os.path.join(destination_folder, new_name)
    shutil.move(file_path, new_path)
    print(f"Archivo movido a: {new_path}")

    return new_path
