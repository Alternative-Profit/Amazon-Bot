from json import load # for config
import requests
# Amazon Stuff
from utils.create_message import amazon_message # Create HTML template for amazon
from utils.product_amazon import Product
from utils.tools import *
from telethon import TelegramClient, events


with open('config/credentials.json') as config_file:
    config = load(config_file)
api_id = config["api_id"]
api_hash = config["api_hash"]
token = config["BOT-TOKEN"]

bot = TelegramClient("bot", api_id, api_hash).start(bot_token=token)
@bot.on(events.NewMessage())
async def start(message):
    await message.respond('Send me links from Amazon! I will give you back a nice post.')
    amazon_valid_urls = ('www.amzn.to', 'amzn.to',
                         'www.amazon.', 'amazon.',
                         'https://www.amazon.', 'https://www.amzn.to')
    url = message.text
    domain = check_domain(message.text)

    if domain.startswith(amazon_valid_urls):

        if 'amzn.to/' in domain:
            url = requests.get(url).url

        product = Product(get_asin(url))
        message = amazon_message(product, message.sender.first_name)
        await bot.send_message(message.chat_id, message["message"], buttons=message["buttons"], parse_mode='HTML')
        await message.delete(message.chat_id, message.message_id)


if __name__ == '__main__':
    print("Bot status[online]")
    bot.run_until_disconnected()
