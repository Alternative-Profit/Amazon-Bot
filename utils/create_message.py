from telethon import Button


def amazon_message(product, name):

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

🗣 Postato da: {name}
"""
    buttons = [[Button.url('🛒AMAZON🛒', product.return_url())]]

    return {"message":message, "buttons":buttons}
