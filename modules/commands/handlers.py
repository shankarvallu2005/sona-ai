from modules.system.system import get_current_time, get_system_info


def handle_time():
    return f"Current Time : {get_current_time()}"


def handle_system():
    system = get_system_info()

    return (
        f"Operating System : {system['operating_system']}\n"
        f"Python Version : {system['python_version']}"
    )


def handle_help():
    return (
        "Available Commands:\n"
        "- time\n"
        "- system\n"
        "- help\n"
        "- exit"
    )


def handle_exit():
    return "Goodbye!"