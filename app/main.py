import json

def load_config():
    with open("config/config.json", "r") as file:
        return json.load(file)

def main():
    config = load_config()

    print("================================")
    print(f"Welcome to {config['assistant_name']}")
    print("================================")
    print(f"Version   : {config['version']}")
    print(f"Developer : {config['developer']}")
    print(f"Theme     : {config['theme']}")
    print(f"Language  : {config['language']}")
    print("SONA is starting...")

if __name__ == "__main__":
    main()