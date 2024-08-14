import json
import logging

logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("../logs/utils.log", "w")
file_formatter = logging.Formatter(
    "%(asctime)s %(levelname)s: %(filename)s %(funcName)s: %(message)s"
)
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)


def json_data():
    try:
        with open(
            r"C:\Users\User\My_Projects\project_2_git\data\operations.json",
            encoding="utf-8",
        ) as f:
            data = json.load(f)
        logger.debug("File opened successfully")
        return data
    except Exception:
        logger.debug("Something went wrong")
        return []


json_data()
