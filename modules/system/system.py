import datetime
import platform

def get_current_time(): # Current time
    return datetime.datetime.now()
def get_system_info(): # System Information
    return{
        "operating_system" : platform.system(),
        "python_version" : platform.python_version()
    }


time = get_current_time()

if __name__ == "__main__":
    print("Current Time :", get_current_time())
    print("System Info :", get_system_info())

