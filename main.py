from fastapi import FastAPI
import threading
from bot.file_watcher import start_monitoring

app = FastAPI()

# Variable global para almacenar la carpeta monitoreada
monitoring_thread = None

@app.get("/")
def read_root():
    return {"message": "Automatización de archivos en ejecución"}

@app.get("/start-monitoring/")
def start_monitoring_service(folder_path: str):
    global monitoring_thread

    if monitoring_thread and monitoring_thread.is_alive():
        return {"status": "error", "message": "El monitoreo ya está en ejecución"}

    # Iniciar el monitoreo en un hilo separado
    monitoring_thread = threading.Thread(target=start_monitoring, args=(folder_path,), daemon=True)
    monitoring_thread.start()
    return {"status": "Monitoreo iniciado", "folder": folder_path}
