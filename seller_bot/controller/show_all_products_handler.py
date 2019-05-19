from db.db_handler import select_store_products
from seller_bot.constants.keyboards import Keyboard
from seller_bot.constants.seller_constants import Message


def show_all_products_callback(bot, update):
    products = select_store_products(store_id=1)
    if products:
        for product in products:
            send_product(bot, update, product)
    else:
        update.message.reply_text(Message.no_products)
        update.message.reply_text(Message.choose_menu, reply_markup=Keyboard.main_menu)


def send_product(bot, update, product):
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=product.photo,
        caption=Message.product_caption.format(name=product.name,
                                               description=product.description,
                                               price=product.price)
    )
