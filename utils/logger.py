import logging

def get_logger():
    logger = logging.getLogger("flight-automation")
    logger.setLevel(logging.INFO)

    console = logging.StreamHandler()
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

    console.setFormatter(formatter)
    logger.addHandler(console)

    return logger