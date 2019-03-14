class BotMessages:
    enter_or_choose_product_count = "تعداد مورد نیاز را انتخاب یا وارد نمایید."
    title = "پیام پرداخت"
    total_price = "\n" \
                  "جمع کل :‌{} ریال"
    send_location = "موقعیت خود را از روی نقشه ارسال نمایید."
    product_list = "*لیست محصولات* :\n"
    products_in_order = "*{index}-* {name} قیمت واحد *{price}* تعداد {count}\n"
    success_add_product_to_order = "محصول با موفقیت به سبد خرید شما اضافه شد."
    product_info = "نام محصول: *{name}*\n" \
                   "دسته: *{category}*\n" \
                   "قیمت: *{price}*\n" \
                   "تعداد موجود: *{inventory}*\n" \
                   "توضیحات: *{description}*\n" \
                   "تعداد مورد نیاز برای افزودن به سبد خرید را انتخاب یا وارد نمایید."
    cat_count = " ({})"
    choose_product = "محصول مورد نظر خود را انتخاب نمایید:"
    choose_category = "به فروشگاه من خوش‌ آمدید.\nبرای شروع خرید یکی از دسته‌بندی‌های زیر را انتخاب کنید:"
    stores = "فروشگاه مورد نظر را انتخاب نمایید:"
    help = "راهنما"
    line = "\n"
    choose_from_buttons = "لطفا از بین گزینه ها انتخاب کنید:"
    start = "سلام به بات فروشگاه خوش آمدید😊😊\nلطفا از بین گزینه ها انتخاب کنید: 👇👇"


class Cons:
    dash = "-"


class ReplyKeyboards:
    one = "1"
    two = "2"
    three = "3"
    next = "مرحله بعد"
    pay = "پرداخت"
    finish_order_and_pay = "تکمیل خرید و پرداخت"
    add_product_to_order = "اضافه کردن به سبد خرید"
    back = "بازگشت"
    products = "محصولات"
    stores = "فروشگاه ها"


class UserData:
    total_price = "total_price"
    count = "count"
    last_product = "last_product"
    categories_list = "categories_list"
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
