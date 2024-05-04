import logging
import os

DIR_LOG = os.path.join(".", "log")

def configurar_logger():
    os.makedirs(DIR_LOG, exist_ok=True)
    log_programa = "ParaulesBoges"
    log_formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_nivel = logging.DEBUG
    log_modo = 'a'
    log_archivo = os.path.join(DIR_LOG, 'boges.log')
    logging.basicConfig(level=log_nivel, format=log_formato, filename=log_archivo, filemode=log_modo)
    return logging.getLogger(log_programa)

def info_log():
    logger = configurar_logger()
    logger.info("Programa iniciado")

def error_log(e, archivo):
    logger = configurar_logger()
    logger.error("Archivo: " + archivo + " - " + str(e))

def final_log(duracion):
    logger = configurar_logger()
    duration_str = "{:.2f}".format(duracion)
    logger.info("Programa finalizado, tardó " + str(duration_str) + " segundos")
