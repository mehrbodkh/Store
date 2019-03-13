from DB.db_handler import get_products_by_store_id


def show_all_products_callback(bot, update):
    products = get_products_by_store_id(1)

    for product in products:
        send_product(bot, update, product)


def send_product(bot, update, product):
    bot.send_photo(
        chat_id=update.message.chat_id,
        photo=product.photo,
        caption=str(
            "نام محصول: " + product.name +
            "\n" +
            "توضیحات:‌ " + product.description +
            "\n" + "قیمت: " + str(product.price) + " ریال")
    )
