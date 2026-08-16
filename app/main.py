import json
from modules.brain.brain import think
from modules.system.system import get_current_time, get_system_info
from modules.commands.commands import process_command

def load_config():
    with open("config/config.json", "r") as file:
        return json.load(file)

def display_banner(config):
    config = load_config()

    print("="*40)
    print(f"        {config['assistant_name']}")
    print("="*40)
    print(f"Version   : {config['version']}")
    print(f"Developer : {config['developer']}")
    print(f"Theme     : {config['theme']}")
    print(f"Language  : {config['language']}")
    print("="*40)


def startup_message():
    print("Initializing SONA...")
    print("System Ready.")
    print()


def main():
    config = load_config()

    display_banner(config)

    startup_message()

    think()

    while True:
        command = input("\nYou : ")
        response = process_command(command)
        print(f"SONA : {response}")
        if command.lower() == "exit":
            break



if __name__ == "__main__":
    main()
