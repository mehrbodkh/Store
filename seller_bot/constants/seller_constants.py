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

    change_store_card_tutorial = "شماره کارت فروشگاه خود را وارد کنید:"
    change_store_card_success = "شماره کارت فروشگاه شما با موفقیت تنظیم شد."
    change_store_card_fail = "شماره کارت شما باید ۱۶ رقمی باشد."

    help_message = "سلام! به بازو مدیریت فروشگاهتان خوش‌آمدید.\nبا استفاده از این بازو می‌توانید فروشگاه خود به آدرس " \
                   "@BazoveanStore_Bot را مدیریت کنید.\n\n-با انتخاب گزینه‌ی *افزودن محصول* می‌توانید محصول جدید را به " \
                   "فروشگاه خود اضافه کنید.\n\n-با انتخاب گزینه‌ی *حذف کردن محصول* می‌توانید محصولات موجود در فروشگاه " \
                   "را حذف نمایید.\n\n-بااستفاده از گزینه‌ی *نمایش تمام محصولات* می‌توانید لیست تمامی محصولات موجود " \
                   "در فروشگاه را ملاحظه نمایید.\n\n- با استفاده از گزینه‌ی *تنظیم شماره‌ کارت فروشگاه* می‌توانید " \
                   "برای فروشگاه خود شماره کارتی تنظیم کنید یا آن‌را تغییر دهید. توجه داشته باشید که مبلغ خرید‌ها از " \
                   "فروشگاه به این کارت واریز خواهد شد. "

    charge_remaining_times_title = "افزایش تعداد دفعات افزودن"
    charge_remaining_times_description = "افزودن ۲۰ عدد تعداد دفعات باقی‌مانده اضافه کردن محصول"


class Keyboards:
    add_item = "افزودن محصول"
    remove_item = "حذف کردن محصول"
    show_all_items = "نمایش تمام محصولات"
    change_store_card_number = "تنظیم شماره کارت فروشگاه"
    return_to_main_menu = "/start"


class ConversationStates:
    NAME, PRICE, PHOTO, DESCRIPTION, INVENTORY, TAG, DELETE_PRODUCT_ID, CARD_NUMBER = range(8)
