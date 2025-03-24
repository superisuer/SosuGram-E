import json

def load_config(filename="config.json"):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return {}
    except json.JSONDecodeError:
        print(f"Ошибка при чтении {filename}. Проверьте формат JSON.")
        return {}

config = load_config()
system_prompt = config.get("system_prompt")
thinking_message = config.get("thinking_message")
prefix = config.get("prefix")
ollama_model = config.get("ollama_model")
command_prefix = config.get("command_prefix")
api_hash = config.get("api_hash")
api_id = config.get("api_hash")
device_model = config.get("device_model")

def save_config(data, filename="config.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def save_cfg(setting, value):
    config[setting] = value
    save_config(config)