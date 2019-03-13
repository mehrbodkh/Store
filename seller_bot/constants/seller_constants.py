class Messages:
    start_conversation = "سلام!\nبه بازوی مدیریت فروشگاه خود خوش آمدید.\nبا استفاده از این بازو می‌توانید اجناس داخل " \
                         "فروشگاه خود به آدرس @BazovanStore_Bot را مدیریت کنید. "
    start_conversation_tour = "برای مدیریت اجناس فروشگاه یکی از گزینه‌های زیر را انتخاب نمایید:"

    add_item_name_tutorial = "لطفا نام محصول خود را وارد کنید:"
    add_item_price_tutorial = "لطفا قیمت محصول خود را وارد کنید:"


class Keyboards:
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"


class ConversationStates:
    NAME, PRICE, PHOTO, DESCRIPTION, INVENTORY, TAG = range(6)
