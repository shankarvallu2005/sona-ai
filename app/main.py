import json

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
    config = load_config

    display_banner(config)

    startup_message()



if __name__ == "__main__":
    main()