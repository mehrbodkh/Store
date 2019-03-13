class Messages:
    start_conversation = "سلام!\nبه بازوی مدیریت فروشگاه خود خوش آمدید.\nبا استفاده از این بازو می‌توانید اجناس داخل " \
                         "فروشگاه خود به آدرس @BazovanStore_Bot را مدیریت کنید. "
    start_conversation_tour = "برای مدیریت اجناس فروشگاه یکی از گزینه‌های زیر را انتخاب نمایید:"


class Keyboards:
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"


class ConversationStates:
    ADD_ITEM, REMOVE_ITEM = range(2)

