<<<<<<< HEAD
from telethon import Button
=======
>>>>>>> 95d0066d7837ac45ed759d780fa857de0b624958


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

<<<<<<< HEAD
🗣 Postato da: {name}
=======
🗣 Postato da: {first_name}
>>>>>>> 95d0066d7837ac45ed759d780fa857de0b624958
"""
    buttons = [[Button.url('🛒AMAZON🛒', product.return_url())]]

    return {"message":message, "buttons":buttons}
