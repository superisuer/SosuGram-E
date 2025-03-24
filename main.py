from pyrogram import Client, filters
from ollama import chat
import cfg
import random 
import base64
from os import system
import emoji
from cryptography.fernet import Fernet
import os
import requests

key = b'rseBSHbX506ZyOLs9qJVCZvTdQqlmkrVnBT0PKXszyo='
cipher = Fernet(key)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_console()

print("""
  ██████  ▒█████    ██████  █    ██   ▄████  ██▀███   ▄▄▄       ███▄ ▄███▓
▒██    ▒ ▒██▒  ██▒▒██    ▒  ██  ▓██▒ ██▒ ▀█▒▓██ ▒ ██▒▒████▄    ▓██▒▀█▀ ██▒
░ ▓██▄   ▒██░  ██▒░ ▓██▄   ▓██  ▒██░▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██    ▓██░
  ▒   ██▒▒██   ██░  ▒   ██▒▓▓█  ░██░░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▒██    ▒██ 
▒██████▒▒░ ████▓▒░▒██████▒▒▒▒█████▓ ░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██▒   ░██▒
▒ ▒▓▒ ▒ ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒  ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ░  ░
░ ░▒  ░ ░  ░ ▒ ▒░ ░ ░▒  ░ ░░░▒░ ░ ░   ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░  ░      ░
░  ░  ░  ░ ░ ░ ▒  ░  ░  ░   ░░░ ░ ░ ░ ░   ░   ░░   ░   ░   ▒   ░      ░   
      ░      ░ ░        ░     ░           ░    ░           ░  ░       ░   
    """)

def is_emoji(s):
    return any(char in emoji.EMOJI_DATA for char in s)
    
def am(text):
    text = text.replace("а", "α") \
                             .replace("б", "δl") \
                             .replace("в", "ϐ") \
                             .replace("г", "г") \
                             .replace("д", "д") \
                             .replace("е", "e") \
                             .replace("ё", "ё̴") \
                             .replace("ж", "җ") \
                             .replace("з", "ӡ") \
                             .replace("и", "μ") \
                             .replace("й", "ύ") \
                             .replace("к", "қ") \
                             .replace("л", "λ") \
                             .replace("м", "ӎ") \
                             .replace("н", "н") \
                             .replace("о", "σ") \
                             .replace("п", "п") \
                             .replace("р", "ρ") \
                             .replace("с", "ϲ") \
                             .replace("т", "τ") \
                             .replace("у", "γ") \
                             .replace("ф", "ቁ") \
                             .replace("х", "χ") \
                             .replace("ц", "ų") \
                             .replace("ч", "ч") \
                             .replace("ш", "ш") \
                             .replace("щ", "щ") \
                             .replace("ъ", "ъ") \
                             .replace("ы", "ы") \
                             .replace("ь", "Ƅ") \
                             .replace("э", "э") \
                             .replace("ю", "ю") \
                             .replace("я", "я́")
    return text

# DOWNLOADING SOSUGRAM STARS
stars = requests.get("https://raw.githubusercontent.com/superisuer/SosuGram/refs/heads/main/stars.txt").text.split(" ")
for i in range(len(stars)): 
    stars[i] = int(stars[i])

user_id = 0
auto_ai = 0
auto_react = [0, ""]

# LOAD VARS FROM CONFIG
system_prompt = cfg.system_prompt
thinking_message = cfg.thinking_message
command_prefix = cfg.command_prefix
ollama_model = cfg.ollama_model
prefix = cfg.prefix
api_hash = cfg.api_hash
api_id = cfg.api_id
device_model = cfg.device_model
database_name = cfg.database_name

# START APP
if len(api_id) < 4 and len(api_hash) < 12:
    api_id = "21865971"
    api_hash = "ad1a33e350675c34d954b9104745df97"

app = Client(database_name, api_id=api_id, api_hash=api_hash, device_model=device_model)

@app.on_message()
def reply_to_messages(client, message):
    global user_id
    if not hasattr(message, "text"):
        return
    if user_id == 0:
        user_id = client.get_me().id
    if auto_react[0] == message.chat.id and message.from_user.id != user_id:
        try:
            message.react(auto_react[1])
        except Exception as e:
            print(f"[ REACT ] {e} - @{message.from_user.username}, ID: {message.from_user.id}")
        else:
            print(f"[ REACT ] @{message.from_user.username}, ID: {message.from_user.id}")
    if auto_ai == message.chat.id and not message.text.startswith(command_prefix):
        print(f"[ AUTO-AI ] {message.text} - @{message.from_user.username}, ID: {message.from_user.id}, GROUP_ID: {auto_ai}")
        if message.from_user.id != user_id:
            prompt = message.text
            msg = message.reply(text=thinking_message) 
            try:
                response = chat(model=ollama_model, messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': prompt}])['message']['content']
            except Exception as e:
                msg.edit(text="**Ошибка: **" + str(e))
            else:
                msg.edit(text=response)
    try:
        if message.from_user.id != user_id:
            return
    except:
        return
    if not message.text.startswith(command_prefix):
        return
    print(f"[ COMMAND ] {message.text} - @{message.from_user.username}, ID: {message.from_user.id}")
    parts = message.text.split()
    command = parts[0].replace(command_prefix, "")
    command_switch = {
        "ai": lambda: handle_ai_command(message, parts),
        "auto_ai": lambda: handle_auto_ai_command(message, parts),
        "am": lambda: handle_am_command(message, parts),
        "ssg": lambda: handle_ssg_command(message, parts),
        "b64": lambda: handle_b64_command(message, parts),
        "p": lambda: handle_prefix_command(message, parts),
        "cmd_p": lambda: handle_command_prefix_command(message, parts),
        "s": lambda: handle_s_command(message, parts),
        "rnd": lambda: handle_rnd_command(message, parts),
        "about": lambda: handle_about_command(message, parts),
        "auto_react": lambda: handle_autoreact_command(message, parts),
        "me": lambda: handle_me_command(message, client),
    }

    command_action = command_switch.get(command)
    if command_action:
        command_action()
    else:
        if not prefix == "":
            try:
                message.edit(text=message.text + prefix)
            except:
                pass

def handle_me_command(message, client):
    me = client.get_me()
    second_additional_text = ""
    if me.id in stars:
        additional_text = "🌟"
        second_additional_text = "Этот пользователь помог в разработке SosuGram."
    elif me.is_premium:
        additional_text = "⭐️"
    elif me.is_fake or me.is_scam:
        additional_text = "🚫"
    elif me.is_bot:
        additional_text = "🤖"
    else:
        additional_text = "👤"

    me_str = f"""
**{additional_text} {me.first_name} {me.last_name}**
**Тег:** @{me.username}
**ID:** {me.id}
**{second_additional_text}**
"""
    message.edit(text=me_str)

def handle_ai_command(message, parts):
    print(message.text)
    prompt = ' '.join(parts[1:])
    message.edit(text=thinking_message) 
    try:
        response = chat(model=ollama_model, messages=[{'role': 'system', 'content': system_prompt}, {'role': 'user', 'content': prompt}])['message']['content']
    except Exception as e:
        message.edit(text="**Ошибка: **" + str(e))
    else:
        message.edit(text=response)

def handle_auto_ai_command(message, parts):
    print(message.text)
    global auto_ai
    if auto_ai == message.chat.id:
        auto_ai = 0
        message.edit(text="**Auto-AI выключен.**")
    else:
        auto_ai = message.chat.id
        message.edit(text=f"**Auto-AI включен для группы: **{auto_ai}")

def handle_am_command(message, parts):
    message.edit(text=am(' '.join(parts[1:])))

def handle_ssg_command(message, parts):
    text = ' '.join(parts[1:])
    try:
        encoded_text = cipher.encrypt(text.encode()).decode()
    except Exception as e:
        pass
    else:
        message.edit(text=encoded_text)
    try:
        decoded_text = cipher.decrypt(text).decode('utf-8')
    except Exception as e:
        pass
    else:
        message.edit(text=decoded_text)

def handle_b64_command(message, parts):
    text = ' '.join(parts[1:])
    try:
        encoded_text = base64.b64encode(text.encode()).decode()
    except Exception as e:
        pass
    else:
        message.edit(text=encoded_text)
    try:
        decoded_text = base64.b64decode(text).decode()
    except Exception as e:
        pass
    else:
        message.edit(text=decoded_text)

def handle_prefix_command(message, parts):
    text = ' '.join(parts[1:])
    cfg.save_cfg('prefix', text.encode('utf-8').decode('unicode_escape'))
    global prefix
    prefix = text.encode('utf-8').decode('unicode_escape')
    message.edit(text="**PREFIX: **" + text + ".")

def handle_command_prefix_command(message, parts):
    global command_prefix
    text = ' '.join(parts[1:])
    cfg.save_cfg('command_prefix', text.encode('utf-8').decode('unicode_escape'))
    command_prefix = text.encode('utf-8').decode('unicode_escape')
    message.edit(text="**COMMAND_PREFIX: **" + text + ".")

def handle_autoreact_command(message, parts):
    global auto_react
    if len(parts) < 2:
        message.edit(f'Реакция удалена для авто-реакции.')
        return
    try:
        chat_id = message.chat.id
    except:
        message.edit(f'**Ошибка: **не удалось получить chat_id.')
        return
    reaction = parts[1]
    if is_emoji(reaction):
        auto_react = [chat_id, reaction]
    else:
        message.edit(f'**Ошибка: **"{reaction}" не является эмодзи.')
        return
    message.edit(f'"{reaction}" установлен для авто-реакции для чата **{chat_id}**.')

def handle_s_command(message, parts):
    message_output = ''
    num_lines = int(parts[1])
    text = ' '.join(parts[2:])
    for _ in range(num_lines):
        message_output += text + '\n'
    message.edit(text=message_output + prefix)

def handle_rnd_command(message, parts):
    if random.randint(0, 1) == 1:
        message.edit(text="да")
    else:
        message.edit(text="нет")

def handle_about_command(message, parts):
    message.edit(text="**Вы используете SosuGram E.**\n**- Разработчик: **@mikeapplee\n**- Канал: **@sosugram")

app.run()
