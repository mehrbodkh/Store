class Messages:
    start_conversation = "سلام!\nبه بازوی مدیریت فروشگاه خود خوش آمدید.\nبا استفاده از این بازو می‌توانید اجناس داخل " \
                         "فروشگاه خود به آدرس @BazovanStore_Bot را مدیریت کنید. "
    start_conversation_tour = "برای مدیریت اجناس فروشگاه یکی از گزینه‌های زیر را انتخاب نمایید:"
    end_add_conversation = "محصول شما با موفقیت به فروشگاه اضافه شد."

    add_item_name_tutorial = "لطفا نام محصول خود را وارد کنید:"
    add_item_price_tutorial = "لطفا قیمت محصول خود را وارد کنید:"
    add_item_photo_tutorial = "لطفا تصویر محصول را ارسال کنید:"
    add_item_description_tutorial = "لطفا توضیحات محصول خود را وارد کنید:"
    add_item_tag_tutorial = "لطفا دسته‌ی محصول خود را انتخاب کنید:\nبرای افزودن دسته‌ی جدید نام دسته‌ی جدید را ارسال " \
                            "کنید. "


class Keyboards:
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"


class ConversationStates:
    NAME, PRICE, PHOTO, DESCRIPTION, INVENTORY, TAG = range(6)
