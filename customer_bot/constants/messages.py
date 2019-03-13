class BotMessages:
    choose_product = "محصول خود را انتخاب نمایید:"
    choose_category = "دسته محصول خود را انتخاب نمایید:"
    stores = "فروشگاه مورد نظر را انتخاب نمایید:"
    help = "راهنما"
    line = "\n"
    choose_from_buttons = "لطفا از بین گزینه ها انتخاب کنید:"
    start = "سلام به بات فروشگاه خوش آمدید😊😊\nلطفا از بین گزینه ها انتخاب کنید: 👇👇"


class ReplyKeyboards:
    products = "محصولات"
    stores = "فروشگاه ها"


class UserDate:
    store = "store"
    store_list = "store_list"


class LogMessages:
    pass


class Store:
    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address


def get_store_list():
    store_list = [Store(1, "ممد آقا", "خیابان شریعتی جنب پارک"),
                  Store(2, "حسن دست کج", "خیابان آزادی جنب میوه فروشی")]
    return store_list


def get_name_list_from_store(store_list):
    name_list = []
    for i in store_list:
        name_list.append(i.name)
    return name_list


def get_categories_list_from_store(store):
    name_list = []
    for i in store:
        name_list.append(i.category)
    return name_list
