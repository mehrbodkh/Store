class Messages:
    start_conversation = "سلام!\nبه بازوی مدیریت فروشگاه خود خوش آمدید.\nبا استفاده از این بازو می‌توانید اجناس داخل " \
                         "فروشگاه خود به آدرس @BazovanStore_Bot را مدیریت کنید. "
    start_conversation_tour = "برای مدیریت اجناس فروشگاه یکی از گزینه‌های زیر را انتخاب نمایید:"
    end_add_conversation = "محصول شما با موفقیت به فروشگاه اضافه شد."

    add_item_name_tutorial = "نام محصول خود را وارد کنید:"
    add_item_price_tutorial = "قیمت محصول خود را به عدد وارد کنید:"
    add_item_photo_tutorial = "تصویر محصول را ارسال کنید:"
    add_item_description_tutorial = "توضیحات محصول خود را وارد کنید:"
    add_item_tag_tutorial = "دسته‌ی محصول خود را انتخاب کنید:\nبرای افزودن دسته‌ی جدید نام دسته‌ی جدید را ارسال " \
                            "کنید. "
    add_item_inventory_tutorial = "تعداد باقیمانده‌ی محصول را وارد نمایید:"

    remove_item_name_tutorial = "نام محصول مورد نظر را وارد کنید:"
    remove_item_not_found = "محصول مورد نظر در لیست محصولات فروشگاه شما موجود نمی‌باشد."
    remove_item_deleted = "محصول مورد نظر با موفقیت از لیست محصولات حذف شد."


class Keyboards:
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"


class ConversationStates:
    NAME, PRICE, PHOTO, DESCRIPTION, INVENTORY, TAG, DELETE_PRODUCT_ID = range(7)
