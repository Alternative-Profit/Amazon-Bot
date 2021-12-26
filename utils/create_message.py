
def amazon_message(product, update):

    first_name = update.message.from_user['first_name']

    if product.get_price().pvp.value != None:
        price = f"❌{product.get_price().pvp.value} ✅{product.get_price().price.value}"

    elif product.get_price().price.value != None:
        price = f"{product.get_price().price.value}"

    else:
        price = "Non "

    message = f"""<a href='{product.get_image()}'>​​​​​​​​​​</a>
📌{product.get_title()}

💰Prezzo: {price}

🔗Link: <a href=\"{product.return_url()}\">Click Here</a>

🗣 Postato da: {first_name}
"""

    buttons = InlineKeyboardMarkup([[InlineKeyboardButton(text='🛒AMAZON🛒', url=product.return_url())]])

    return [message, buttons]
