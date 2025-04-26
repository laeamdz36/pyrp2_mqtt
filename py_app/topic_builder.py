"""Builder to construc custom topics for MQTT"""
import json
import os
from typing import Any


class Topics:
    """Class to storage and handle configured topics"""

    def __init__(self, config):
        self.config = config


def get_path(file_name):
    """Load config topics"""

    file_name = "topics.json"
    parent_dir = os.path.dirname(__file__)
    result_pth = None
    try:
        file_pth = os.path.join(parent_dir, file_name)
        if os.path.exists(file_pth):
            result_pth = file_pth
        else:
            print(f"Path does not exists for -> {file_name}")
    except TypeError:
        print(
            f"Incorrect type for -> '{file_name}' {type(file_name)} must be str")

    return result_pth


def read_config(file_name: str = "topics.json") -> dict[str, Any]:
    """read config information from jason file"""

    file_pth = get_path(file_name)
    with open(file_pth, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
