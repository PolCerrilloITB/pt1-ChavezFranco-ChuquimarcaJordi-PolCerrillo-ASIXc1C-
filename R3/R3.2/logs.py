import os
import logging

def crear_logger(programa_log):
    path_nombre_log = os.path.join(".", "registro")
    os.makedirs(path_nombre_log, exist_ok=True)
    archivo_log = os.path.join(path_nombre_log, 'boges.log')
    formato_log = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    nivel_log = logging.DEBUG
    modo_log = 'a'
    logging.basicConfig(level=nivel_log, format=formato_log, filename=archivo_log, filemode=modo_log)
    logger = logging.getLogger(programa_log)
    return logger
def info_log(logger):
    logger.info("Programa iniciado")
def error_log(logger, e, archivo):
    logger.error("Archivo: " + archivo + " - " + str(e))
def log_final(logger, duracion):
    duracion_str = "{:.2f}".format(duracion)
    logger.info("Programa finalizado, tardó " + str(duracion_str) + " segundos")
    logger = crear_logger("ParaulesBoges")
    info_log(logger)
    try:
        pass
    except Exception as e:
        error_log(logger, e, "principal")
    finally:
        log_final(logger, 1.23)
