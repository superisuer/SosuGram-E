# SosuGram-E
A modification for your Telegram account that is able to manage your messages through commands. It is similar to a userbot. AI features, censorship-filter bypass, flooding, AI auto-reply, message encryption are available. \
*This modification violates ToS, so be careful!*
## Commands
- `ai <prompt>` - Write a message via AI to Ollama.
- `auto_ai <chat_id>` - Automatically reply to messages via AI to users in <chat_id> chat.
- `am <text>` - Bypass censorship of swear words.
- `ssg <text>` - Encrypt the message via Fernet.
- `b64 <text>` - Base64 encoding and decoding.
- `p <text>` - Set a prefix to be automatically added to the end of your every post.
- `cmd_p <prefix>` - Set the prefix for handling the command.
- `s <n> <text>` - Duplicate the <n> string once in 1 post.
- `rnd` - Select yes or no at random.
- `about` - About the SosuGram.
## Setup
### Windows
Download and unarchive the latest release and configure config.json (entering api_hash, api_id and other parameters is optional). Run the SosuGram executable and enter your phone number, code and cloud password (if present). After entering the data, go to any Telegram client from the same account and try to write any command. For example, write `about` command (with the prefix that was in config.json, the default is “.”). If your message has changed, you've done the right thing. If it still hasn't changed and you are sure it is correct, send the error (or a screenshot of the SosuGram window) to Issues.
### Python (Windows and other systems)
Download the source and code from the latest release and extract it to any folder. Open terminal in this directory and install requirements.txt via pip. After installation, configure config.json (same as with Windows) and run main.py. Everything else is the same as in the Windows instructions.
