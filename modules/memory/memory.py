import json


MEMORY_FILE = "data/memory.json"


def load_memory():

    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {}


def save_memory(memory):

    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)