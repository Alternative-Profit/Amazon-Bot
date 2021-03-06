<!---------------------------
README.MD
AmazonBot-1.1.0
---------------------------->

# AmazonBot

🤖Fast and simple bot to transform links from Amazon into a nice post with your referral link in Telegram 🛒

### Prerequisites

- You need Python 3.0 or higher

```
pip3 install requirements.txt
```

### Setup

In order to setup the bot you need to copy `example_credentials.json` to `credentials.json` in `config/example_credentials.json`.
Then add Bot Token (get it from [@BotFather](https://t.me/Botfather)) and Amazon configuration to the file `credentials.json`

### Running

```
#If you want just run the bot
python3 main.py

# Or maybe run forever in to a VPS in linux
screen -r  python3 main.py
```

### Customizing the message 😉

Now customizing is more easy, you can go to `utils/create_message.py` and edit the variable `message` to put in whatever you want

### Changelog

```
Version 1.0.3
  -Definitive Edition
Version 1.0.2
  -Rewrite the code in Telethon
Version 1.0.1
  - Initial Release
```

## Built With

- [python-amazon-paapi](https://github.com/sergioteula/python-amazon-paapi)
- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Telethon](https://github.com/LonamiWebs/Telethon)
## License

This project is licensed under the Apache 2.0 License - see the [LICENSE.md](LICENSE.md) file for details
