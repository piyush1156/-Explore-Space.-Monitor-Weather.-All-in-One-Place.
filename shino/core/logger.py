import logging
import sys
from shino.config.config import Config

def setup_logger(name="SHINO"):
    logger = logging.getLogger(name)
    level = logging.DEBUG if Config.DEBUG else logging.INFO
    logger.setLevel(level)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler
    ch = logging.StreamHandler(sys.stdout)
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # File handler
    fh = logging.FileHandler("shino.log")
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger

logger = setup_logger()
