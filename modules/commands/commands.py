from modules.commands.handlers import (
    handle_time,
    handle_system,
    handle_help,
    handle_exit,
)


def process_command(command):

    command = command.lower().strip()

    if command == "time":
        return handle_time()

    elif command == "system":
        return handle_system()

    elif command == "help":
        return handle_help()

    elif command == "exit":
        return handle_exit()

    else:
        return "Sorry, I don't understand that command."