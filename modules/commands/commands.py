from modules.system.system import get_current_time, get_system_info

def process_command(command):
    command = command.lower()
    if command == "time":
        return f"Current Time : {get_current_time()}"
    elif command == "system":
        info = get_system_info()
        return(
            f"Operating System : {info['operating_system']}\n"
            f"Python Version : {info['python_version']}"
        )
    elif command == "help":
        return (
            "Available Commands:\n"
            "- time\n"
            "- system\n"
            "- help\n"
            "- exit"
        )
    elif command == "love you buddy" or command == "love you":
        return "love you too buddy!!"
    elif command == "who build you":
        return "Shankar"
    elif command == "exit":
        return "Goodbye!"
    
    else:
        return "Sorry, I don't understand that command."
