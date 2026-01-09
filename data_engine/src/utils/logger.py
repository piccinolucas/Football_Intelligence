import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file="pipeline.log"):
    #Logger que escribe tanto en archivo como en consola

    # 1. Definición de la ruta del archivo de log
    log_dir = "/app/logs"
    os.makedirs(log_dir, exist_ok=True)
    log_path = os.path.join(log_dir, log_file)

    # 2. Configuracion de Timestamp y formato
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # 3. Handler de Archivo
    # Backup de 3 archivos de 5MB cada uno
    file_handler = RotatingFileHandler(log_path, maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(formatter)

    # 4. Handler de Consola
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 5. Creación del objeto Logger en nivel INFO (Puede ser DEBUG, WARNING, ERROR en caso de producción)
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    
    # Evitar duplicación de logs
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger