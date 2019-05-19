from db.db_handler import get_all_not_sent_orders


def orders_button_callback(bot, update):
    show_current_orders(bot, update)


def show_current_orders(bot, update):
    orders = get_all_not_sent_orders()

    for order in orders:
        send_order_message(bot, update, order)


def send_order_message(bot, update, order):
    text = ""
    bot.send_location(
        chat_id=update.message.chat_id,
        latitude=order.address.latitude,
        longitude=order.address.longitude
    )
    for order_product in order.order_products:
        text = text + "\n- " + str(order_product.product.name) + ": " + str(order_product.count)
    bot.send_message(
        chat_id=update.message.chat_id,
        text=text
    )
