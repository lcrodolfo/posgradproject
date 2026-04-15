import logging
import os
from datetime import datetime

RUN_TIMESTAMP = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
LOG_DIR = f"logs/run_{RUN_TIMESTAMP}"
os.makedirs(LOG_DIR, exist_ok=True)

def get_detailed_logger(name):
    logger = logging.getLogger(f"{name}")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
        )
        file_handler = logging.FileHandler(f"{LOG_DIR}/detailed.log")
        file_handler.setFormatter(formatter)
        
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
               

    return logger

def get_results_logger():
    logger = logging.getLogger("results_logger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        formatter = logging.Formatter(
            "%(asctime)s - %(message)s"
        )

        file_handler = logging.FileHandler(f"{LOG_DIR}/results.log")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger